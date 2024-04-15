from pydantic import BaseModel

from src.settings.AppSettings import AppSettings
from src.settings.DatabaseSettings import DatabaseSettings
from src.settings.RabbitMQSettings import RabbitMQSettings
from src.settings.SwaggerSettings import SwaggerSettings


class Settings(BaseModel):
    app_settings: AppSettings = AppSettings()
    database_settings: DatabaseSettings = DatabaseSettings()
    rabbitmq_settings: RabbitMQSettings = RabbitMQSettings()
    swagger_settings: SwaggerSettings = SwaggerSettings()
