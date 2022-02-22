from __future__ import annotations
import json

class JSONReporter:

    def __init__(self, config):
        self.format = 'json'

        self.reporter_config = config

        self.output_path = self.reporter_config.get('path', './results.json')
        self.events = {}
        self.metrics = {}

    @classmethod
    def about(cls):
        return '''
        JSON Reporter - (json)

        The JSON reporter allows you to dump events and metrics to JSON file locally. Events
        and metrics are written as items in a JSON array and grouped by their respective
        event/metric name.

        '''

    async def init(self) -> JSONReporter:
        pass

    async def update(self, event) -> list:

        event_name = event.data.get('event_name')
        event_dict = {
            'time': event.get_utc_time(),
            **event.to_dict()
        }

        if self.events.get(event_name) is None:
            self.events[event_name] = [ event_dict ]

        else:
            self.events[event_name] += [ event_dict ]

        return list(self.events.values())

    async def merge(self, connector) -> JSONReporter:
        return self

    async def fetch(self, key=None) -> list:
        return [ self.events.get(key) ]

    async def submit(self, metric) -> JSONReporter:

        metric_name = metric.metric.name

        metric_dict = {
            'utc_time': metric.get_utc_time(),
            'local_time': metric.get_local_time(),
            **metric.to_dict()
        }

        if self.metrics.get(metric_name) is None:    
            self.metrics[metric_name] = [ metric_dict ]

        else: 
            self.metrics[metric_name] += [ metric_dict ]

        return self

    async def close(self) -> JSONReporter:
        with open(self.output_path, 'w') as data_file:
            json.dump(self.metrics, data_file, indent=4)

        return self