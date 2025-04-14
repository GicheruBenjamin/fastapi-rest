

'''
met -GET /posts - all posts
met -GET /posts/{post_id} - single post details
met -POST /posts - create new post
met -PUT /posts/{post_id} - update post
met -PATCH /posts/{post_id} - partial update post
met -DELETE /posts/{post_id} - delete post
'''

from fastapi import APIRouter
from ..services import CreatePost, GetPostById, GetPostByUserId, GetPostByTitle, GetPosts, UpdatePost, DeletePost

router = APIRouter()

@router.get("/")
def get_posts():
    return GetPosts()

@router.get("/{post_id}")
def get_post(post_id: int):
    return GetPostById(post_id)

@router.post("/")
def create_post():
    return CreatePost(title, content, user_id)

@router.put("/{post_id}")
def update_post(post_id: int):
    return UpdatePost(post_id, title, content)

@router.patch("/{post_id}")
def partial_update_post(post_id: int):
    return UpdatePost(post_id, title, content)

@router.delete("/{post_id}")
def delete_post(post_id: int):
    return DeletePost(post_id)