from pydantic import SecretStr

from src.settings.GlobalSettings import GlobalSettings


class RabbitMQSettings(GlobalSettings):
    rabbitmq_host: str
    rabbitmq_port: int
    rabbitmq_username: str
    rabbitmq_password: SecretStr
