import os
import pydantic_settings

from deliveryapi.configs.settings.TelethonSettings import TelethonSettings


class Settings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=os.getenv("ENV_FILE", ".env"),
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )
    telethon: TelethonSettings
