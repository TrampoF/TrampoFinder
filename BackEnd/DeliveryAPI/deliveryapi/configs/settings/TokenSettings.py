import pydantic_settings 

class TokenSettings(pydantic_settings.BaseSettings): 
    sign_algorithm = "RS256"
    encryption_algorithm = "ECDH-ES"
    cek_encryption_algorithm = "A128GCM"