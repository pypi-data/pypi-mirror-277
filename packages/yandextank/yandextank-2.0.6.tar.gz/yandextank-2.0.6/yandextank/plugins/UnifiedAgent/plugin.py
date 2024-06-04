import logging
import time
from typing import Dict, List
from queue import Queue
from yandextank.common.interfaces import MonitoringPlugin
from yandextank.common.monitoring import MonitoringPanel, DefaultCollector
from yandextank.common.util import expand_to_seconds
from yandextank.plugins.UnifiedAgent.sensor import UnifiedAgentSensor

LOGGER = logging.getLogger(__name__)


class Plugin(MonitoringPlugin):
    def __init__(self, core, cfg, name):
        super(Plugin, self).__init__(core, cfg, name)
        self.timeout = expand_to_seconds(self.get_option('timeout'))
        self.poll_interval = expand_to_seconds(self.get_option('poll_interval'))

    def prepare_test(self):
        hosts_cfg: List[Dict] = self.get_option('hosts')
        if not hosts_cfg:
            LOGGER.info('hosts config is empty; plugin will be idle')
            return
        self.collector = make_collector(
            hosts_cfg, self.timeout, self.poll_interval, time.time(),
        )


def as_list(value) -> list:
    if value is None or isinstance(value, list):
        return value
    return [value]


def make_collector(
    hosts_cfg: List[dict],
    timeout: float,
    poll_interval: float,
    skip_metrics_before_ts: float,
):
    collector = DefaultCollector(logger=LOGGER, timeout=timeout, poll_interval=poll_interval)
    LOGGER.debug('preparing ua plugin with config %s', hosts_cfg)
    panels = {}
    for host in hosts_cfg:
        host_address = host.get('address')
        panelname: str = host.get('panel', host_address)
        queue = Queue()
        panel = panels.get(panelname) or MonitoringPanel(panelname, poll_interval, queue)
        panels[panelname] = panel
        senset = set()
        # if no `sensors` provided - use sensor with all available metrics
        sensor = UnifiedAgentSensor(
            host=host_address,
            project=host['project'],
            service=host['service'],
            fetcher=host['fetcher'],
            config=host.get('sensors'),
            queue=queue,
            skip_metrics_before_ts=skip_metrics_before_ts,
            preserve_underscore_in_sensors=bool(host.get('preserve_underscore_in_sensors', False)),
            metric_labels=as_list(host.get('metric_type_labels')),
            priority_labels=as_list(host.get('metric_type_grouping_labels')),
            ignore_labels=as_list(host.get('ignore_labels')),
        )
        senset.update(sensor.get_sensors())

        collector.add_sensor(sensor)
        panel.add_sensors(senset)

    for panel in panels.values():
        collector.add_panel(panel)

    return collector
