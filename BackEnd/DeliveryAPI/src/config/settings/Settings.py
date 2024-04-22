from pydantic import BaseModel

from src.config.settings.AppSettings import AppSettings
from src.config.settings.DatabaseSettings import DatabaseSettings
from src.config.settings.RabbitMQSettings import RabbitMQSettings
from src.config.settings.SwaggerSettings import SwaggerSettings


class Settings(BaseModel):
    app_settings: AppSettings = AppSettings()
    database_settings: DatabaseSettings = DatabaseSettings()
    rabbitmq_settings: RabbitMQSettings = RabbitMQSettings()
    swagger_settings: SwaggerSettings = SwaggerSettings()
