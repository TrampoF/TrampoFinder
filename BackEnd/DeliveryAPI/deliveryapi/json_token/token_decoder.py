from typing import Any
from fastapi import HTTPException, status
from joserfc import jwt, jwe, errors, util
from ..configs.settings.TokenSettings import TokenSettings
from ast import literal_eval
import jwe_payload

token_settings = TokenSettings() 
SIGN_ALGORITHM = token_settings.sign_algorithm

class TokenDecoder:
    '''The token decoder object, which contains ``main_claims``.

    :param main_claim: The claim of the main information being traded by the token.
    '''
    def __init__(self, main_claim: str): 
        self.main_claim = main_claim 
    
    def decode_nested_token(self, token: str, encryption_private_key: str) -> Any: 
        try: 
            decrypted_token = self.decrypt_token(token, encryption_private_key) 
            verified_token_claims = self.verify_signed_token(decrypted_token.plaintext) 
            claim_value = verified_token_claims.get(self.main_claim, None)  
            return claim_value
        
        except (errors.BadSignatureError, errors.InvalidKeyTypeError, errors.MissingClaimError, errors.InvalidPayloadError, ValueError, errors.DecodeError) as e: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Unknown exception: {e}")        
    
    def verify_signed_token(self, signed_token_bytes: bytes) -> dict: 
        jwe_payload.JwePayload.from_bytes_token(signed_token_bytes) 
        decoded_token:dict = literal_eval(signed_token_bytes.decode("utf-8"))
        essential_claims = [self.main_claim, ]

        return decoded_token.get("claims")

    def decrypt_token(self, token: str, private_key: str) -> Any: 
        try: 
            decrypted_token = jwe.decrypt_compact(token, private_key)
            return decrypted_token
        except (errors.InvalidKeyTypeError, errors.DecodeError):
            raise
