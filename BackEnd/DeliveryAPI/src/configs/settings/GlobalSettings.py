import pydantic_settings


class GlobalSettings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file="env",
        env_file_encoding="utf-8",
        extra='ignore'
    )
