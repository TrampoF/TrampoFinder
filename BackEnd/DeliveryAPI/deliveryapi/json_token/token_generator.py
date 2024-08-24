from typing import Any
from joserfc import jwt, jwe, jwk
import os

SIGN_ALGORITHM = "RS256"
ENCRYPTION_ALGORITHM = "ECDH-ES"
CEK_ENCRYPTION_ALGORITHM = "A128GCM"

# Cada user_id tera duas chaves: uma publica para verificacao de tokens assinados e uma privada para decriptar o token
jwk.ECKey
jwk.RSAKey
class TokenGenerator:
    '''The token generator object, which contains ``main_claims`` and ``main_claim_value``.

    :param main_claim: The claim of the main information being traded by the token. Don't put registered claims. 
    :param main_claim_value: The main information being traded by the token.
    '''
    def __init__(self, main_claim: str, main_claim_value: Any): 
        self.main_claim = main_claim 
        self.main_claim_value = main_claim_value 

    def generate_nested_token(self, user_id: int, signing_key: str, encryption_public_key: str, 
                              sign_algorithm: str = SIGN_ALGORITHM, encryption_algorithm: str = ENCRYPTION_ALGORITHM, cek_encryption_algorithm: str = CEK_ENCRYPTION_ALGORITHM) -> str: 
        signed_token = self.generate_signed_token(user_id, signing_key, sign_algorithm) 
        encrypted_token = self.generate_encrypted_token(signed_token, encryption_public_key, encryption_algorithm, cek_encryption_algorithm)
        return encrypted_token 

    def generate_signed_token(self, user_id: int, signing_key: str, sign_algorithm: str) -> str: 
        header = {
            "alg": sign_algorithm, 
        }
        claims = {
            self.main_claim: self.main_claim_value, 
            "sub": user_id 
        }
        return jwt.encode(header, claims, signing_key, sign_algorithm) 

    def generate_encrypted_token(self, payload: str, encrypting_public_key: str, encryption_algorithm: str, cek_encryption_algorithm: str) -> str:
        protected_header = {
            "alg": encryption_algorithm, 
            "enc": cek_encryption_algorithm
        }
        algorithms_list = ["ECDH-ES", "A128GCM"]
        return jwe.encrypt_compact(protected=protected_header, plaintext=payload, public_key=encrypting_public_key, algorithms=algorithms_list)
