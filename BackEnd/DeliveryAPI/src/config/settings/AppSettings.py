from src.config.settings.GlobalSettings import GlobalSettings


class AppSettings(GlobalSettings):
    app_name: str
    app_version: str
    app_host: str
    app_port: int
    app_env: str
