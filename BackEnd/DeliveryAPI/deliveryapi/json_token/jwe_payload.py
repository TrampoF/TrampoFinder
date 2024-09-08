from joserfc import jwt , util, errors
from typing import Any
from ast import literal_eval

class JwePayload: 
    '''The JSON Web Encryption Payload, that is just like a jwt, but with no signature. 
    '''
    def __init__(self, unsigned_jwt): 
        self.unsigned_jwt = unsigned_jwt

    @classmethod 
    def from_bytes_token(cls, token_bytes:bytes): 
        decoded_token:dict = literal_eval(token_bytes.decode("utf-8"))
        return cls(decoded_token)

    @classmethod
    def from_dict_token(cls, header: dict[str, Any], claims: dict[str, Any]): 
        unsigned_jwt = {
            "header": header,
            "claims": claims
        } 
        return cls(unsigned_jwt)

    def get_unsigned_jwt(self) -> dict[str, dict]: 
        return self.unsigned_jwt 
    
    def get_unsigned_jwt_dumped(self) -> str: 
        return util.json_dumps(self.unsigned_jwt)
    
    def verify_claims(self, essential_claims: list[str]): 
        essential_claims = {claim: {"essential": True} for claim in essential_claims}
        claims_request = jwt.JWTClaimsRegistry(
            **essential_claims
        )
        try: 
            claims_request.validate(self.get_unsigned_jwt().get("claims"))
        except (Exception, errors.MissingClaimError): 
            raise
