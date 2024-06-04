from robusta.core.sinks.sink_base_params import SinkBaseParams
from robusta.core.sinks.sink_config import SinkConfigBase


class KafkaSinkParams(SinkBaseParams):
    kafka_url: str
    topic: str
    auth: dict = {}

    @classmethod
    def _get_sink_type(cls):
        return "kafka"


class KafkaSinkConfigWrapper(SinkConfigBase):
    kafka_sink: KafkaSinkParams

    def get_params(self) -> SinkBaseParams:
        return self.kafka_sink
