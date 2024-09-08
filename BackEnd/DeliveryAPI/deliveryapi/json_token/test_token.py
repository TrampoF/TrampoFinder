from ..json_token.token_generator import TokenGenerator
from ..json_token.token_decoder import TokenDecoder
from joserfc import jwk, errors
import base64
import json
from fastapi import HTTPException
from ..configs.settings.TokenSettings import TokenSettings

token_settings = TokenSettings() 
SIGN_ALGORITHM = token_settings.sign_algorithm
ENCRYPTION_ALGORITHM = token_settings.encryption_algorithm
CEK_ENCRYPTION_ALGORITHM = token_settings.cek_encryption_algorithm 

test_keys_root = "test_keys"
private_key_file = open(f"./{test_keys_root}/private-key.pem", "r") 
pem_data = private_key_file.read() 
rsa_private_key = jwk.RSAKey.import_key(pem_data)
private_key_file.close() 

public_key_file = open(f"./{test_keys_root}/public-key.pem", "r") 
pem_data = public_key_file.read() 
rsa_pub_key = jwk.RSAKey.import_key(pem_data)
public_key_file.close()


private_key_file_EC = open(f"./{test_keys_root}/ec-p256-private.pem", "r" )
pem_data = private_key_file_EC.read()
ec_private_key = jwk.ECKey.import_key(pem_data) 
private_key_file_EC.close() 

public_key_file_EC = open(f"./{test_keys_root}/ec-p256-public.pem", "r" )
pem_data = public_key_file_EC.read()
ec_public_key = jwk.ECKey.import_key(pem_data)
public_key_file_EC.close()

# Load test keys
def load_keys():
    test_keys_root = "test_keys"

    with open(f"./{test_keys_root}/private-key.pem", "r") as file:
        rsa_private_key = jwk.RSAKey.import_key(file.read())
    
    with open(f"./{test_keys_root}/public-key.pem", "r") as file:
        rsa_pub_key = jwk.RSAKey.import_key(file.read())
    
    with open(f"./{test_keys_root}/ec-p256-private.pem", "r") as file:
        ec_private_key = jwk.ECKey.import_key(file.read())
    
    with open(f"./{test_keys_root}/ec-p256-public.pem", "r") as file:
        ec_public_key = jwk.ECKey.import_key(file.read())
    
    return rsa_private_key, rsa_pub_key, ec_private_key, ec_public_key

rsa_private_key, rsa_pub_key, ec_private_key, ec_public_key = load_keys()

def add_padding(encoded_str):
    """Ensure the Base64 encoded string has the correct padding."""
    padding = len(encoded_str) % 4
    if padding != 0:
        encoded_str += '=' * (4 - padding)
    return encoded_str


def test_main_claim_essentiality(): 
    main_claim = "api_id" 
    fake_main_claim1 = "sub"
    fake_main_claim2 = "sushi"
    main_claim_value = 12345
    uid = 1
    token_gen = TokenGenerator(main_claim, main_claim_value)
    encoded_token = token_gen.generate_nested_token(uid, ec_public_key)
    token_decoder1 = TokenDecoder(fake_main_claim1)
    token_decoder2 = TokenDecoder(fake_main_claim2)
    count = 0

    try: 
        token_decoder1.decode_nested_token(encoded_token, None, ec_private_key)
    except (errors.MissingClaimError, TypeError):
        count += 1
        print("ERRO1")

    try: 
        token_decoder2.decode_nested_token(encoded_token, None, ec_private_key)
    except (errors.MissingClaimError, Exception):
        count += 1


    assert count == 2

def test_encryption(): 
    try: 
        plaintext = "information"
        token_gen = TokenGenerator("user_id", 12345)
        encrypted_token = token_gen.generate_encrypted_token(plaintext, ec_public_key, ENCRYPTION_ALGORITHM, CEK_ENCRYPTION_ALGORITHM)
        token_decoder = TokenDecoder("user_id")
        decrypted_token = token_decoder.decrypt_token(encrypted_token, ec_private_key)

    except Exception: 
        assert 0
    
    # Test with wrong key
    try: 
        fake_key = jwk.ECKey.generate_key()
        token_decoder.decrypt_token(encrypted_token, fake_key)   
        assert 0
    except (errors.InvalidKeyTypeError, errors.DecodeError):
        pass

    # Test with non-encrypted token
    signed_token = token_gen.generate_plain_text(user_id=1)
    try: 
        token_decoder.decrypt_token(signed_token, ec_private_key)
        assert 0
    except ValueError:
        pass
    
    assert 1

def test_nested_token(): 
    main_claim = "api_id" 
    main_claim_value = 12345
    uid = 1
    token_gen = TokenGenerator(main_claim, main_claim_value)
    nested_token = token_gen.generate_nested_token(uid, ec_public_key) 
    token_decoder = TokenDecoder(main_claim) 
    wrong_token_decoder = TokenDecoder(main_claim="sushi")
    
    try:
        decoded_claim = token_decoder.decode_nested_token(nested_token, None, ec_private_key)
    except Exception:
        assert 0
    
    # Wrong main claim case
    try: 
        decoded_claim = wrong_token_decoder.decode_nested_token(nested_token, None, ec_private_key)
        print(decoded_claim)
        assert 0
    except HTTPException: 
        pass 
    
    assert 1

def test_new_token():
    token_gen = TokenGenerator(main_claim="api-id", main_claim_value=12345)
    nested_token = token_gen.generate_nested_token(user_id=1, encryption_public_key=ec_public_key) 
    token_decoder = TokenDecoder(main_claim="api-id") 
    decoded_information = token_decoder.decode_nested_token(nested_token, None, ec_private_key)
    print(decoded_information)

def json_token_tests(): 
    test_main_claim_essentiality()
    test_encryption()
    # test_nested_token() TTODO: ambos relativos a validacao por claim essencial
    test_new_token()
