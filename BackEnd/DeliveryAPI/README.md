<div align="center">
    <h1>Delivery API</h1>
</div>

![Static Badge](https://img.shields.io/badge/python-gray?logo=python)
![Static Badge](https://img.shields.io/badge/poetry-gray?logo=poetry)
![Static Badge](https://img.shields.io/badge/docker-gray?logo=docker)

> This application is responsible for capture and process messages from third party message systems.

## Development

### Using the dev container (preferable and requires docker)

1. Install [docker engine](https://docs.docker.com/engine/).
2. On [Visual Studio Code](https://code.visualstudio.com/) install the [Dev Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension, and run the **Rebuild Without Cache and Reopen in Container**;
3. Run the application with `poetry run dev` command.

### Out of a container (does not requires docker)

1. Install Python with version 3.11.x;
2. Install Poetry with version 1.8.x;
3. Follow those commands:
    ```
    git clone https://github.com/TrampoF/TrampoFinder.git
    cd ./TrampoFinder/Backend/DeliveryAPI
    poetry install
    ```
4. Run the application with `poetry run dev` command.
