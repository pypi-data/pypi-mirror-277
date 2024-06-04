from yandextank.common.interfaces import MonitoringPlugin
from yandextank.common.monitoring import DefaultCollector, MonitoringPanel
from yandextank.common.util import expand_to_seconds
from yandextank.plugins.Solomon.solomonsensor import SolomonSensor
from logging import getLogger
from queue import Queue


logger = getLogger(__name__)


class Plugin(MonitoringPlugin):

    def __init__(self, core, cfg, name):
        super(Plugin, self).__init__(core, cfg, name)
        try:
            self.timeout = int(self.get_option('timeout'))
        except ValueError:
            self.timeout = expand_to_seconds(self.get_option('timeout'))

    def prepare_test(self):
        error = 'No error'
        token = None
        try:
            with open(self.get_option('token_file'), 'r') as tfile:
                token = tfile.read().strip('\n')
        except (OSError, IOError):
            error = "Solomon plugin: Authorization token is not set! File {} is not found or can't be read.".format(self.get_option('token_file'))
            logger.warning(error)

        if not token and self.get_option('enforce_check_token'):
            raise RuntimeError(error)
        if token:
            self.collector = DefaultCollector(logger=logger, timeout=self.timeout, poll_interval=self.timeout)
            api_host = self.get_option('api_host')
            for name, data in self.get_option('panels').items():
                queue = Queue()
                panel = MonitoringPanel(name, self.timeout, queue)
                senset = set()
                for dto in data['sensors']:
                    sensor = SolomonSensor(api_host, data['project'], dto, panel.queue, token, data['priority_labels'])
                    senset.update(sensor.get_sensors())
                    self.collector.add_sensor(sensor)
                panel.add_sensors(senset)
                self.collector.add_panel(panel)
