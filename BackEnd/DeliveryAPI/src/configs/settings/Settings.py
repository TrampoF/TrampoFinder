import functools

import pydantic

import TelethonSettings


class Settings(pydantic.BaseModel):
    telethon_settings: TelethonSettings = TelethonSettings.TelethonSettings()


@functools.lru_cache
def get_settings(env: pydantic.Optional[str] = None) -> Settings:
    if env is None:
        return Settings()

    return Settings(_env_file=f".env.{env}")
