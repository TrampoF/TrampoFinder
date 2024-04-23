from src.configs.PikaConfig import PikaConfig


class PikaService:
    def __init__(self, pika_config: PikaConfig):
        self.pika_config = pika_config

    async def send_message(self, message: str):

