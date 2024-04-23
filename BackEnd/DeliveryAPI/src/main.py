from functools import lru_cache
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends

from src.configs.settings import Settings


@lru_cache
def get_settings():
    return Settings()


def main(settings: Settings = Annotated[Settings, Depends(get_settings)]) -> None:
    try:
        app = FastAPI()
        uvicorn.run(app, host=settings.app_settings.app_host, port=settings.app_settings.app_port)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main(get_settings())
