

'''
/login
/register
/logout
/forgot-password
/refresh-token
'''

from fastapi import APIRouter
from pydantic import BaseModel
from ..services import Login, Register, Logout, ForgotPassword, RefreshToken

router = APIRouter()

class Login(BaseModel):
    email: str
    password: str

@router.post("/login")
def login():
    return Login(email, password)

class RegisterRequest(BaseModel):
    email: str
    password: str
    name: str
    phone: str


@router.post("/register")
def register():
    return Register(email, password, name, phone)


@router.post("/logout")
def logout():
    return Logout(token)

class ForgotPassword(BaseModel):
    email: str
@router.post("/forgot-password")
def forgot_password():
    return ForgotPassword(email)

class RefreshToken(BaseModel):
    refresh_token: str
@router.post("/refresh-token")
def refresh_token():
    return RefreshToken(refresh_token)
