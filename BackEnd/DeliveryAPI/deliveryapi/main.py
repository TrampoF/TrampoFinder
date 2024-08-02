from deliveryapi.configs.settings.Settings import Settings


def main():
    print(Settings().model_dump())


if __name__ == "__main__":
    main()
