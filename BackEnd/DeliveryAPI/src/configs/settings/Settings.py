import functools

import pydantic

import AppSettings
import DatabaseSettings
import RabbitMQSettings
import SwaggerSettings
import TelethonSettings


class Settings(pydantic.BaseModel):
    app_settings: AppSettings = AppSettings.AppSettings()
    database_settings: DatabaseSettings = DatabaseSettings.DatabaseSettings()
    rabbitmq_settings: RabbitMQSettings = RabbitMQSettings.RabbitMQSettings()
    swagger_settings: SwaggerSettings = SwaggerSettings.SwaggerSettings()
    telethon_settings: TelethonSettings = TelethonSettings.TelethonSettings()


@functools.lru_cache
def get_settings(env: pydantic.Optional[str] = None) -> Settings:
    if env is None:
        return Settings()

    return Settings(_env_file=f".env.{env}")
