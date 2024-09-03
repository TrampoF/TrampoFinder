from deliveryapi.configs.settings.Settings import Settings
from deliveryapi.configs.settings.TelethonSettings import TelethonSettings
from deliveryapi.configs.settings.TokenSettings import TokenSettings
from deliveryapi.json_token.test_token import json_token_tests

def main():
    print(Settings(telethon= TelethonSettings(api_id= "12345", api_hash="seguro"), token= TokenSettings()).model_dump())
    json_token_tests() 


if __name__ == "__main__":
    main()
