

'''
Crud operations for users
'''

from sqlalchemy.orm import Session
from ..Models import User
from ..Settings import InitDb

db = InitDb()

def CreateUser(username, email):
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    return user

def GetUserById(id):
    user = db.query(User).filter(User.id == id).first()
    return user

def GetUserByUsername(username):
    user = db.query(User).filter(User.username == username).first()
    return user

def GetUsers():
    users = db.query(User).all()
    return users

def UpdateUser(id, username, email):
    user = db.query(User).filter(User.id == id).first()
    user.username = username
    user.email = email
    db.commit()
    return user

def DeleteUser(id):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return user