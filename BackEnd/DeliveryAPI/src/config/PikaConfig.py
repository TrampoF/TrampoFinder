from typing import AsyncIterator

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.credentials import PlainCredentials

from src.config.settings import RabbitMQSettings


class PikaConfig:
    def __init__(self, rabbitmq_settings: RabbitMQSettings):
        self.rabbitmq_settings = rabbitmq_settings

    async def create_connection(self) -> AsyncIterator[BlockingChannel]:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.rabbitmq_settings.rabbitmq_host,
            port=self.rabbitmq_settings.rabbitmq_port,
            virtual_host=self.rabbitmq_settings.rabbitmq_virtual_host,
            credentials=self.__credentials()
        ))
        yield connection.channel()
        connection.close()

    def __credentials(self) -> PlainCredentials:
        credentials = pika.PlainCredentials(
            username=self.rabbitmq_settings.rabbitmq_username,
            password=self.rabbitmq_settings.rabbitmq_password
        )
        return credentials
