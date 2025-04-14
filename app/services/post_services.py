

'''
Post services
Create, Get, Update, Delete
'''

from ..db.repos import CreatePost, GetPostById, GetPostByUserId, GetPostByTitle, GetPosts, UpdatePost, DeletePost

def CreatePost(title, content, user_id):
    post = CreatePost(title, content, user_id)
    return post

def GetPostById(id):
    post = GetPostById(id)
    return post

def GetPostByUserId(user_id):
    posts = GetPostByUserId(user_id)
    return posts

def GetPostByTitle(title):
    post = GetPostByTitle(title)
    return post

def GetPosts():
    posts = GetPosts()
    return posts

def UpdatePost(id, title, content):
    post = UpdatePost(id, title, content)
    return post

def DeletePost(id):
    post = DeletePost(id)
    return post