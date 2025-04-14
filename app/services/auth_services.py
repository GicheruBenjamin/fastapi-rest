

'''
Auth services
Login, Register, Logout , forgot-password, refresh-token
'''

import bcrypt
from ..db.repos import CreateUser, GetUserByUsername, GetUserByEmail
from ..utils.Tokens import GenerateToken
from ..utils.Email import send_email

def Login(email, password):
    user = GetUserByEmail(email)
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        token = GenerateToken(user.id)
        return {"message": "Login Successful", "token": token}
    else:
        return {"message": "Invalid Credentials"}
        
def Register(email, password, name, phone):
    user = GetUserByEmail(email)
    if user:
        return {"message": "User already exists"}
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = CreateUser(email, hashed_password, name, phone)
        token = GenerateToken(user.id)
        send_email(email, "Welcome to FastAPI-REST", "Welcome to FastAPI-REST")
        return {"message": "Register Successful", "token": token}

def Logout(token):
    return {"message": "Logout Successful"}

def ForgotPassword(email):
    user = GetUserByEmail(email)
    if user:
        token = GenerateToken(user.id)
        send_email(email, "Reset Password", "Reset Password")
        return {"message": "Forgot Password Successful", "token": token}
    else:
        return {"message": "User not found"}

def RefreshToken(refresh_token):
    return {"message": "Refresh Token Successful"}