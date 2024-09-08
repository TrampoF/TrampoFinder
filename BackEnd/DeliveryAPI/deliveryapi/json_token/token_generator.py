from typing import Any
from joserfc import jwt, jwe, jwk, util
from ..configs.settings.TokenSettings import TokenSettings
from datetime import datetime
import jwe_payload

token_settings = TokenSettings() 
SIGN_ALGORITHM = token_settings.sign_algorithm
ENCRYPTION_ALGORITHM = token_settings.encryption_algorithm
CEK_ENCRYPTION_ALGORITHM = token_settings.cek_encryption_algorithm

class TokenGenerator:
    '''The token generator object, which contains ``main_claims`` and ``main_claim_value``.

    :param main_claim: The claim of the main information being traded by the token. Don't put registered claims. 
    :param main_claim_value: The main information being traded by the token.
    '''
    def __init__(self, main_claim: str, main_claim_value: Any): 
        self.main_claim = main_claim 
        self.main_claim_value = main_claim_value 

    def generate_nested_token(self, user_id: int, encryption_public_key: str
                                , encryption_algorithm: str = ENCRYPTION_ALGORITHM, cek_encryption_algorithm: str = CEK_ENCRYPTION_ALGORITHM) -> str: 
        plain_text = self.generate_plain_text(user_id) 
        encrypted_token = self.generate_encrypted_token(plain_text, encryption_public_key, encryption_algorithm, cek_encryption_algorithm)
        return encrypted_token 

    def generate_plain_text(self, user_id: int, signing_key: str|None = None, sign_algorithm: str|None = None) -> str: 
        header = {
            "iat": str(datetime.now())
        }
        claims = {
            self.main_claim: self.main_claim_value, 
        }

        jwe_payload_obj = jwe_payload.JwePayload.from_dict_token(header, claims) 
        str_plain_text = jwe_payload_obj.get_unsigned_jwt_dumped()

        return str_plain_text 

    def generate_encrypted_token(self, payload: str, encrypting_public_key: str, encryption_algorithm: str, cek_encryption_algorithm: str) -> str:
        protected_header = {
            "alg": encryption_algorithm, 
            "enc": cek_encryption_algorithm
        }
        algorithms_list = ["ECDH-ES", "A128GCM"]
        return jwe.encrypt_compact(protected=protected_header, plaintext=payload, public_key=encrypting_public_key, algorithms=algorithms_list)
