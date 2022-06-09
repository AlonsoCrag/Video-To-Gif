from venv import create
import jwt
import datetime
import secrets

now = datetime.datetime.utcnow()
exp = now + datetime.timedelta(days=364)
# key = secrets.token_hex(16)
key = "df25a92ea67de6e789926f1d00d9835c"

def create_token(req_new_token=None):
    if req_new_token:
        token = jwt.encode({"username": "elmer", "password": "elmercabezon123", "exp": exp}, key=key, algorithm="HS256")
        print("Your new Token is", token)
        return
    token = jwt.encode({"username": "alonso", "password": "elmercabezon123", "exp": exp}, key=key, algorithm="HS256")
    print("Token", token)

def decode_token(token):
    decoded = jwt.decode(token, key=key, algorithms=["HS256"])
    print("Decoded", decoded)

token = "akskas"

try:
    decode_token(token)
except:
    create_token(req_new_token=True)