import dependency_injector.containers
import dependency_injector.providers
import sqlalchemy.ext.asyncio

import src.configs.settings.Settings


class Gateways(dependency_injector.containers.DeclarativeContainer):
    config = dependency_injector.providers.Configuration()
    config.from_dict(src.configs.settings.Settings.get_settings().model_dump())

    postgres_client = dependency_injector.providers.Singleton(
        sqlalchemy.ext.asyncio.create_async_engine,
    )


