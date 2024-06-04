from logging import getLogger
from queue import Queue
import fnmatch
import json
import requests
import time
from typing import Optional, List
from yandextank.common.util import observetime
from yandextank.common.monitoring import MonitoringSensorProtocol


logger = getLogger(__name__)


class UnifiedAgentSensor(MonitoringSensorProtocol):
    """
    The UnifiedAgentSensor class is intended for obtaining actual discrete values and composing these data into a convenient format for further processing.
    """

    GET_DATA_URI = '/read?project={}&service={}'
    NEXT_SEQ_NUMBER_HEADER = 'X-Solomon-NextSequenceNumber'
    SEQ_NUMBER_HEADER = 'X-Solomon-SequenceNumber'

    def __init__(
        self,
        host,
        project,
        service,
        fetcher,
        config,
        queue: Queue,
        skip_metrics_before_ts: float = 0,
        preserve_underscore_in_sensors: bool = True,
        metric_labels: Optional[List] = None,
        priority_labels: Optional[List] = None,
        ignore_labels: Optional[List] = None,
    ):
        self.default_headers = {'Accept-Encoding': "application/json,zstd", 'X-Solomon-FetcherId': fetcher}
        self.data_url = "http://{0}{1}".format(host, self.GET_DATA_URI.format(project, service))
        self.skip_metrics_before_ts = skip_metrics_before_ts

        self._name_normalizer = str.maketrans('/.', '--')
        self._type_normalizer = str.maketrans('/.', '--')
        if not preserve_underscore_in_sensors:
            self._type_normalizer = str.maketrans('/._', '---')

        self.preserve_underscore_in_sensors = preserve_underscore_in_sensors
        self.queue = queue
        self.config = config
        self.priority_labels = priority_labels or []
        self.metric_labels = metric_labels or ['app', 'metric', 'name', 'path', 'sensor', 'signal']
        ignore_labels = ignore_labels or ['cluster', 'project', 'service', 'servant', 'os', 'instance']
        self.ignore_labels = (
            ignore_labels + self.metric_labels + self.priority_labels
        )
        self.next_seq_number = '0'

    def fetch_metrics(self):
        self.prepare_data(self.get_data())

    @observetime('UnifiedAgentSensor.prepare_data', logger)
    def prepare_data(self, data):
        if isinstance(data, dict) and 'sensors' in data:
            try:
                for sensor_item in data['sensors']:
                    if not self.match_metrics(sensor_item.get('labels')):
                        continue
                    if metrics := self.parse_metrics(sensor_item):
                        self.send_metrics(metrics)
            except KeyError as ke:
                logger.warning("Wrong data: {}. {}".format(data, ke), exc_info=True)
        else:
            logger.warning("Wrong data: {}".format(data))

    def match_metrics(self, labels) -> bool:
        if not labels:
            return False
        if not self.config:
            return True
        return any([self._match_metrics(metric, labels) for metric in self.config])

    def _match_metrics(self, metric: dict, labels: dict) -> bool:
        for k, v in metric.items():
            if not fnmatch.fnmatch(labels.get(k, ''), v):
                return False
        return True

    def parse_metrics(self, metrics):
        match metrics['kind']:
            case 'GAUGE':
                timeseries = metrics.get('timeseries')
                if timeseries is None:
                    timeseries = [{'ts': metrics['ts'], 'value': metrics['value']}]
                sensor = self.format_sensor(metrics['labels'])
                return [
                    {
                        'sensor': sensor,
                        'timestamp': m['ts'],
                        'value': m['value'],
                    }
                    for m in timeseries
                    if m['ts'] >= self.skip_metrics_before_ts
                ]
            case 'RATE':
                ts = int(time.time())
                value = metrics['value']
                return [
                    {
                        'sensor': self.format_sensor(metrics['labels']),
                        'timestamp': ts,
                        'value': value,
                    }
                ]
            case _:
                logger.warning('Unknown sensor kind %s', metrics['kind'])
                return None

    def send_metrics(self, data):
        try:
            self.queue.put(data)
        except (IOError, OSError) as error:
            logger.warning("Sensor {} send metrics error. {}".format(data.get('sensor'), error), exc_info=True)

    @observetime('UnifiedAgentSensor.get_data', logger)
    def get_data(self):
        try:
            logger.debug('Polling unified agent seq_number %s', self.next_seq_number)
            headers = {self.SEQ_NUMBER_HEADER: self.next_seq_number}
            headers.update(self.default_headers)
            response = requests.get(self.data_url, headers=headers)
            response.raise_for_status()
        except ConnectionError:
            logger.exception('Connection error during request')
        except Exception:
            logger.exception('request to unified agent failed')
        else:
            self.next_seq_number = response.headers.get(self.NEXT_SEQ_NUMBER_HEADER, '0')
            self.skip_metrics_before_ts = time.time()
            try:
                return response.json()
            except json.JSONDecodeError as e:
                logger.error('UnifiedAgent parse error: %s', e, exc_info=False)

    def get_sensors(self):
        sensors = set()
        data = self.get_data()
        if isinstance(data, dict) and 'sensors' in data.keys():
            for sensor in data['sensors']:
                if self.match_metrics(sensor.get('labels')):
                    sensors.add(self.format_sensor(sensor['labels']))
        return sensors

    def format_sensor(self, labels) -> str:
        if not isinstance(labels, dict):
            return 'Unknown'
        parts = []
        for label in self.metric_labels:
            if v := labels.get(label):
                parts.append(v)
                break
        else:
            logger.warning('Wrong labels %s', labels)
            parts.append('Summary')

        for label in self.priority_labels:
            if v := labels.get(label):
                parts.append(v)

        metric_type = '-'.join([p.strip('-*._/').translate(self._type_normalizer) for p in parts])

        parts = []
        for key, value in labels.items():
            if key in self.ignore_labels:
                continue
            else:
                parts.append(value)

        metric_name = '_'.join([p.strip('-*._/').translate(self._name_normalizer) for p in parts])
        return f'{metric_type}_{metric_name}'
