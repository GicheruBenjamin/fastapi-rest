
'''
met -GET /users - all users
met -GET /users/{user_id} - single user details
met -POST /users - create new user
met -PUT /users/{user_id} - update user
met -PATCH /users/{user_id} - partial update user
met -DELETE /users/{user_id} - delete user
'''

from fastapi import APIRouter
from ..services import CreateUser, GetUserById, GetUserByUsername, GetUsers, UpdateUser, DeleteUser

router = APIRouter()

@router.get("")
def getusers():
    return GetUsers()

@router.get("/{user_id}")
def get_user(user_id: int):
    return GetUserById(user_id)

@router.post("")
def create_user():
    return CreateUser(username, email)

@router.put("/{user_id}")
def update_user(user_id: int):
    return UpdateUser(user_id, username, email)

@router.patch("/{user_id}")
def partial_update_user(user_id: int):
    return UpdateUser(user_id, username, email)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return DeleteUser(user_id)