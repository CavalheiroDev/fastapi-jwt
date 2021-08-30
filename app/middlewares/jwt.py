import hmac
from hashlib import sha256
from base64 import urlsafe_b64decode, urlsafe_b64encode
from json import dumps, loads
from os import getenv



def generate_jwt_token(header, payload):

    SECRET_KEY_JWT = getenv('SECRET_KEY_JWT')

    header_json = dumps(header).encode()
    payload_json = dumps({'email': payload.email, 'password': payload.password}).encode()

    encoded_header = urlsafe_b64encode(header_json).decode()
    encoded_payload = urlsafe_b64encode(payload_json).decode()

    signature = hmac.new(
        key=SECRET_KEY_JWT.encode(),
        msg=f'{encoded_header}.{encoded_payload}'.encode(),
        digestmod=sha256
    ).digest()

    jwt_token = f'{encoded_header}.{encoded_payload}.{urlsafe_b64encode(signature).decode()}'

    return jwt_token

def validate_jwt_token(jwt_token: str):

    SECRET_KEY_JWT = getenv('SECRET_KEY_JWT')

    encoded_header, encoded_payload, encoded_signature = jwt_token.split('.')

    encoded_signature_check = urlsafe_b64encode(
        hmac.new(
            key=SECRET_KEY_JWT.encode(),
            msg=f'{encoded_header}.{encoded_payload}'.encode(),
            digestmod=sha256
        ).digest()
    ).decode()

    payload = loads(urlsafe_b64decode(encoded_payload))

    if encoded_signature_check != encoded_signature:
        return False
    return payload