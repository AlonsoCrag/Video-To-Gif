from flask import request, jsonify
import jwt
import secrets
from datetime import datetime, timedelta, time

from dotenv import load_dotenv
from os import getenv

load_dotenv()

private_key = getenv('PRIVATE_KEY')
username = getenv('USERNAME')
password = getenv('PASSWORD')

def check_token():

    try:
        token = request.form.get('token')
        print("Data", token)
        # token = data["token"]
        #jwt will decode and check if the time has expired
        res = jwt.decode(token, private_key, algorithms=["HS256"])
    except:
        print("No token provided or it has expired")
        resp = jsonify({ "message": "token expired or not found, request another one to the developer" })
        resp.status_code = 404
        return (resp, False)
        
    if res["username"] == username and password == res["password"]:
        return res
    
    print('Wrong credentials provided...')
    resp = jsonify({ "message": "token expired or not found, request another one" })
    resp.status_code = 404
    return (resp, False) 
        