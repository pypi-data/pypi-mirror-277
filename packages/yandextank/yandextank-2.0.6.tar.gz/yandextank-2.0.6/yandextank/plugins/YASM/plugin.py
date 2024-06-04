import re

import time
from queue import Empty

from multiprocessing import Queue, Event, Process

import logging

import signal
from yandextank.common.interfaces import MonitoringPlugin, MonitoringCollectorProtocol
from infra.yasm.yasmapi import RtGolovanRequest
from threading import Thread

logger = logging.getLogger(__name__)


DEFAULT_SIGNALS = {
    'portoinst-cpu_usage_cores_tmmv': 'cpu_usage',
    'portoinst-cpu_guarantee_cores_tmmv': 'cpu_guarantee',
    'portoinst-cpu_limit_cores_tmmv': 'cpu_limit',
    'portoinst-cpu_wait_cores_tmmv': 'cpu_wait',
    'portoinst-memory_usage_gb_tmmv': 'memory_usage',
    'portoinst-memory_limit_gb_tmmv': 'memory_limit',
    'portoinst-io_read_fs_bytes_tmmv': 'io_read',
    'portoinst-io_write_fs_bytes_tmmv': 'io_write',
    'portoinst-io_limit_bytes_tmmv': 'io_limit',
    'conv(unistat-auto_disk_rootfs_usage_bytes_axxx, Gi)': 'rootfs_usage',
    'conv(unistat-auto_disk_rootfs_total_bytes_axxx, Gi)': 'rootfs_total',
    'portoinst-net_mb_summ': 'net_mb',
    'portoinst-net_guarantee_mb_summ': 'net_guarantee',
    'portoinst-net_limit_mb_summ': 'net_limit'
}


def signals_stream(panel):
    '''
    :type yasmapi_cfg: Panel
    :return: Panel, float, dict
    '''
    for point in RtGolovanRequest(panel.as_dict):
        yield point.ts, point.values[panel.host][panel.tags]


def map_metric_name(name):
    NAME_MAP = {r'conv\(.+\)': r'(?<=conv\().+?(?=,)'}
    for pattern, mask in NAME_MAP.items():
        if re.match(pattern, name):
            name = re.findall(mask, name)[0]
            break
    return 'custom:{}'.format(name)


def convert_value(name, value):
    return value


def monitoring_data(ts, data, metric_map, comment=''):
    return {
        "timestamp": ts,
        "data": {
            host: {
                "comment": comment,
                "metrics": {map_metric_name(metric_map[name]): convert_value(name, value) for name, value in host_data.items()}
            }
            for host, host_data in data.items()}}


class YasmCfg(object):
    def __init__(self, panels):
        self.panels = [Panel(alias, **attrs) for alias, attrs in panels.items()]
        self._as_dict = None

    @property
    def as_dict(self):
        if self._as_dict is None:
            yasmapi_cfg = {}
            for panel in self.panels:
                yasmapi_cfg.setdefault(panel.host, {})[panel.tags] = panel.signals
            logger.info('yasmapi cfg: {}'.format(yasmapi_cfg))
            self._as_dict = yasmapi_cfg
        return self._as_dict


class Panel(object):
    def __init__(self, alias, host, tags, signals=None, default_signals=True):
        self.queue = Queue()
        self.alias = alias
        self.extend_signals = self._check_signals_(signals)
        self.signals = [signal.get('metric', '') if isinstance(signal, dict) else signal for signal in self.extend_signals] + (list(DEFAULT_SIGNALS.keys()) if default_signals else [])

        self.host = host
        self.tags = tags.strip(';')

        if len(self.signals) == 0:
            logger.warning('No signals specified for {} panel'.format(self.alias))
        self.as_dict = {self.host: {self.tags: self.signals}}
        self.metric_map = self._metrics_map_()

    def _check_signals_(self, signals):
        checked = []
        if isinstance(signals, list):
            for element in signals:
                if isinstance(element, str):
                    checked.append(element)
                elif isinstance(element, dict):
                    if element.get('metric'):
                        checked.append(element)
                    else:
                        logging.warning('Wrong signal: %s', element)
                else:
                    logging.warning('Wrong signal: %s', element)
        return checked

    def _metrics_map_(self):
        metrics_map = DEFAULT_SIGNALS
        assign_alias = set(metrics_map.values())
        for metric in self.extend_signals:
            key = metric.get('metric', '') if isinstance(metric, dict) else metric
            mark = metric.get('mark', '') if isinstance(metric, dict) else None
            value = '{}_signal'.format(mark) if mark and mark not in assign_alias else key
            if key:
                metrics_map.update({key: value})
        return metrics_map


class YasmMPReceiver(MonitoringCollectorProtocol):
    def __init__(self, yasm_cfg, yasmapi_timeout):
        """

        :type data_queue: Queue
        :type yasm_cfg: YasmCfg
        """
        self.panels = yasm_cfg.panels
        self.data_queue = Queue()
        self.timeout = yasmapi_timeout
        self._data_buffer = []
        self.start_event = Event()
        self.stop_event = Event()
        self.interrupted = Event()
        self.end_time = None
        self.ps_pool = {panel.alias: Process(target=self.single_receiver,
                                             args=(panel,))
                        for panel in self.panels}
        self.consumers = {panel.alias: Thread(target=self.single_consumer, args=(panel, self.ps_pool[panel.alias]))
                          for panel in self.panels}

    def poll(self):
        data, self._data_buffer = self._data_buffer, []
        return data

    def prepare(self):
        [p.start() for p in self.ps_pool.values()]

    def start(self):
        self.start_event.set()
        [consumer.start() for consumer in self.consumers.values()]

    def single_receiver(self, panel):
        # ignore SIGINT (process is controlled by .stop_event)
        """

        :type panel: Panel
        """
        signal.signal(signal.SIGINT, signal.SIG_IGN)

        stream = signals_stream(panel)
        try:
            while not self.stop_event.is_set():
                ts, data = next(stream)
                if self.start_event.is_set():
                    panel.queue.put((ts, {panel.alias: data}))
            else:
                logger.info('Stopped collecting metrics for panel {}'.format(panel.alias))
        except KeyboardInterrupt:
            pass
        finally:
            logger.info('Closing panel {} receiver thread'.format(panel.alias))

    def single_consumer(self, panel, ps):
        """

        :type ps: Process
        :type panel: Panel
        """
        while not self.interrupted.is_set():
            try:
                ts, data = panel.queue.get(timeout=self.timeout)
                self._data_buffer.append(monitoring_data(ts, data, panel.metric_map))
                if self.end_time is not None:
                    if ts > self.end_time:
                        logger.info('{} all yasm metrics received'.format(panel.alias))
                        self.stop_event.set()
                        break
                    else:
                        logger.info('Waiting for yasm metrics for panel {}'.format(panel.alias))
                else:
                    logger.debug('New ts: {}'.format(ts))
            except Empty:
                logger.warning(
                    'Not receiving any data for panel {} from YASM.'
                    'Probably your hosts/tags specification is not correct'.format(panel.alias))
                if ps.is_alive():
                    ps.terminate()
                break
        else:
            logger.info('Interrupting {}'.format(panel.alias))
            self.stop_event.set()
        logger.debug("Stopping panel {} controller")

    def stop(self):
        self.end_time = time.time()
        logger.info('Stopping yasm plugin')
        try:
            for panel in self.panels:
                if self.consumers[panel.alias].is_alive():
                    self.consumers[panel.alias].join()
                if self.ps_pool[panel.alias].is_alive():
                    self.ps_pool[panel.alias].terminate()
        except KeyboardInterrupt:
            self.interrupted.set()
            for panel in self.panels:
                if self.consumers[panel.alias].is_alive():
                    self.consumers[panel.alias].join()
                if self.ps_pool[panel.alias].is_alive():
                    self.ps_pool[panel.alias].terminate()


class Plugin(MonitoringPlugin):
    def __init__(self, core, cfg, name):
        super(Plugin, self).__init__(core, cfg, name)
        self.collector = YasmMPReceiver(YasmCfg(self.get_option('panels')),
                                        self.get_option('timeout'))

    def prepare_test(self):
        self.collector.prepare()
        return super().prepare_test()
