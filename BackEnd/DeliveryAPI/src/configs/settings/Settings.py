import os
import pydantic_settings

from configs.settings.TelethonSettings import TelethonSettings


class Settings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", "..",".env"),
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )
    telethon: TelethonSettings