from json_token.token_generator import TokenGenerator
from json_token.token_decoder import TokenDecoder
import base64
import json
from fastapi import HTTPException
from joserfc import errors, jwk, jwt

private_key_file = open("./id_rsa", "r") 
pem_data = private_key_file.read() 
rsa_private_key = jwk.RSAKey.import_key(pem_data)
private_key_file.close() 

public_key_file = open("./id_rsa.pub", "r") 
pem_data = public_key_file.read() 
rsa_pub_key = jwk.RSAKey.import_key(pem_data)
public_key_file.close()

private_key_file_EC = open("./ec-p256-private.pem", "r" )
pem_data = private_key_file_EC.read()
ec_private_key = jwk.ECKey.import_key(pem_data) 
private_key_file_EC.close() 

public_key_file_EC = open("./ec-p256-public.pem", "r" )
pem_data = public_key_file_EC.read()
ec_public_key = jwk.ECKey.import_key(pem_data)
public_key_file_EC.close()


def add_padding(encoded_str):
    """Ensure the Base64 encoded string has the correct padding."""
    padding = len(encoded_str) % 4
    if padding != 0:
        encoded_str += '=' * (4 - padding)
    return encoded_str


def test_alg_change_none(): 
    '''Changes token algorithm claim in order to verify if the token processor accepts only tokens with the pre-defined algorithm. 

    token: A signed JWT <br>
    new_algorithm (str): The new algorithm to be placed in the alg claim.  
    ''' 
    token_gen = TokenGenerator("api_id", 12345) 
    token = token_gen.generate_signed_token(1, rsa_private_key,SIGN_ALGORITHM)

    token_chunks = token.split('.')

    encoded_header= token_chunks[0]
    encoded_header = add_padding(encoded_header)

    decoded_header = base64.urlsafe_b64decode(encoded_header)

    dict_header = json.loads(decoded_header)

    dict_header["alg"] = "none"

    string_header = json.dumps(dict_header) 

    encoded_header = base64.urlsafe_b64encode(string_header.encode())

    encoded_header = encoded_header.decode('utf-8').rstrip("=") # remove padding

    malicious_token = f"{encoded_header}.{token_chunks[1]}." # you can check in jwt.io if this token is valid
    error_found = 0 
    
    try: 
        registry = jwt.JWTClaimsRegistry() 
        registry.options.update({"verify_signature": False})
        token_decoder = TokenDecoder("api_id")
        token_decoder.verify_signed_token(malicious_token, key= "", sign_algorithm="none")
        error_found += 1

    except errors.ConflictAlgorithmError:
        pass
    except errors.InvalidTokenError:
        pass
    except (errors.BadSignatureError , errors.MissingClaimError, Exception) as e: 
        pass

    assert not error_found
    

def test_main_claim_essentiality(): 
    main_claim = "api_id" 
    fake_main_claim1 = "sub"
    fake_main_claim2 = "sushi"
    main_claim_value = 12345
    uid = 1
    token_gen = TokenGenerator(main_claim, main_claim_value)
    encoded_token = token_gen.generate_signed_token(uid, rsa_private_key, SIGN_ALGORITHM) 
    token_decoder1 = TokenDecoder(fake_main_claim1) 
    token_decoder2 = TokenDecoder(fake_main_claim2) 
    count = 0
    try: 
        token_decoder1.verify_signed_token(encoded_token, rsa_pub_key, SIGN_ALGORITHM)
    except (errors.MissingClaimError, TypeError) as e: 
        count += 1

    try: 
        token_decoder2.verify_signed_token(encoded_token, rsa_pub_key, SIGN_ALGORITHM)
    except errors.MissingClaimError: 
        count += 1 
    
    assert count == 2
 


def test_encryption(): 
    try: 
        plaintext = "information"
        token_gen = TokenGenerator("user_id", 12345)
        encrypted_token = token_gen.generate_encrypted_token(plaintext, ec_public_key, ENCRYPTION_ALGORITHM, CEK_ENCRPYTION_ALGORITHM)
        token_decoder = TokenDecoder("user_id") # in this case, the main_claim does not matter
        decrypted_token = token_decoder.decrypt_token(encrypted_token, ec_private_key)

    except Exception: 
        assert 0
    
    #token with wrong key
    try: 
        fake_key = jwk.ECKey.generate_key()
        decrypted_token = token_decoder.decrypt_token(encrypted_token, fake_key)   
        
        assert 0
    except errors.InvalidKeyTypeError as e:
        pass
    except errors.DecodeError as e: 
        pass

    #  with non encrypted token
    signed_token = token_gen.generate_signed_token(1, rsa_private_key, SIGN_ALGORITHM)
    try: 
        token_decoder.decrypt_token(signed_token, rsa_pub_key)
        
        assert 0
    except ValueError: 
        pass
    

    assert 1
    



def test_nested_token(): 
    main_claim = "api_id" 
    main_claim_value = 12345
    uid = 1
    token_gen = TokenGenerator(main_claim, main_claim_value)
    nested_token = token_gen.generate_nested_token(uid, rsa_private_key, ec_public_key) 
    token_decoder = TokenDecoder(main_claim) 
    wrong_token_decoder = TokenDecoder(main_claim="sushi")
    try:
        decoded_claim = token_decoder.decode_nested_token(nested_token, rsa_pub_key, ec_private_key)
    except Exception:
        assert 0
    #nasty case
    try: 
        decoded_claim = wrong_token_decoder.decode_nested_token(nested_token, rsa_pub_key, ec_private_key)
        print(decoded_claim)
       
        assert 0
    except HTTPException: 
        pass 
    
    assert 1






test_alg_change_none()
test_main_claim_essentiality()
test_encryption()
test_nested_token()