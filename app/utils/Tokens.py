
'''
Token functions 
'''

from datetime import datetime, timedelta
import jwt
import os
import configparser

def GenerateToken(user_id):
    # Load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # Setup token data
    secret_key = config['TOKENS']['SECRET_KEY']
    algorithm = config['TOKENS']['ALGORITHM']
    expires_delta = timedelta(minutes=config['TOKENS']['EXPIRES_DELTA'])
    
    # Generate token
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + expires_delta
    }
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token

def VerifyToken(token):
    # Load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # Setup token data
    secret_key = config['TOKENS']['SECRET_KEY']
    algorithm = config['TOKENS']['ALGORITHM']
    
    # Verify token
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        return {"message": "Token expired"}
    except jwt.InvalidTokenError:


def GetUserIdFromToken(token):
    payload = VerifyToken(token)
    return payload['user_id']

