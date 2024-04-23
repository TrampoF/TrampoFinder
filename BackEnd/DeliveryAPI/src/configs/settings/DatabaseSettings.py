from pydantic import SecretStr

from src.configs.settings.GlobalSettings import GlobalSettings


class DatabaseSettings(GlobalSettings):
    db_host: str
    db_port: int
    db_database: str
    db_username: str
    db_password: SecretStr
