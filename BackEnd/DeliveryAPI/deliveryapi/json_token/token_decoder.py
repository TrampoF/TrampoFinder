from typing import Any
from fastapi import HTTPException, status
from joserfc import jwt, jwe, errors

SIGN_ALGORITHM = "RS256"

class TokenDecoder:
    '''The token decoder object, which contains ``main_claims``.

    :param main_claim: The claim of the main information being traded by the token.
    '''
    def __init__(self, main_claim: str): 
        self.main_claim = main_claim 
    
    def decode_nested_token(self, token: str, signing_key: str, encryption_private_key: str, sign_algorithm: str = SIGN_ALGORITHM) -> Any: 
        try: 
            decrypted_token = self.decrypt_token(token, encryption_private_key) 
            verified_token_claims = self.verify_signed_token(decrypted_token.plaintext, signing_key, sign_algorithm) 
            claim_value = verified_token_claims.get(self.main_claim, None)  
            return claim_value
        
        except (errors.BadSignatureError, errors.InvalidKeyTypeError, errors.MissingClaimError, errors.InvalidPayloadError, ValueError, errors.DecodeError) as e: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unknown exception")        
    
    def verify_signed_token(self, signed_token: str, key: str, sign_algorithm: str) -> dict: 

         # TODO: claim obrigatoria: aud = {"essential": True, value: "example.com/token"},  # the url ?? iss= {}, # seria a url do servidor de "autenticacao"?
        claims_request = jwt.JWTClaimsRegistry(
            sub={"essential": True},
            **{self.main_claim: {"essential": True}}
        )
        try: 
            decoded_token = jwt.decode(signed_token, key, sign_algorithm)
            claims_request.validate(decoded_token.claims) 
            return decoded_token.claims
        except (errors.BadSignatureError, errors.MissingClaimError, ValueError, errors.InvalidKeyTypeError):
            raise 

    def decrypt_token(self, token: str, private_key: str) -> Any: 
        try: 
            decrypted_token = jwe.decrypt_compact(token, private_key)
            return decrypted_token
        except (errors.InvalidKeyTypeError, errors.DecodeError):
            raise
