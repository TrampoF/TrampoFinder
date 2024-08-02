import pydantic_settings


class TelethonSettings(pydantic_settings.BaseSettings):
    api_id: str
    api_hash: str
