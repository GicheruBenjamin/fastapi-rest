

'''
Crud operations for posts
'''

from sqlalchemy.orm import Session
from ..Models import Post
from ..Settings import InitDb

db = InitDb()

def CreatePost(title, content, user_id):
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    return post

def GetPostById(id):
    post = db.query(Post).filter(Post.id == id).first()
    return post

def GetPostByUserId(user_id):
    post = db.query(Post).filter(Post.user_id == user_id).all()
    return post

def GetPostByTitle(title):
    post = db.query(Post).filter(Post.title == title).first()
    return post

def GetPosts():
    posts = db.query(Post).all()
    return posts

def UpdatePost(id, title, content):
    post = db.query(Post).filter(Post.id == id).first()
    post.title = title
    post.content = content
    db.commit()
    return post

def DeletePost(id):
    post = db.query(Post).filter(Post.id == id).first()
    db.delete(post)
    db.commit()
    return post