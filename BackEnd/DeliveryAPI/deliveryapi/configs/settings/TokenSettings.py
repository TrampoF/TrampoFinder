import pydantic_settings 

class TokenSettings(pydantic_settings.BaseSettings): 
    sign_algorithm:str = "RS256"
    encryption_algorithm:str = "ECDH-ES"
    cek_encryption_algorithm:str = "A128GCM"