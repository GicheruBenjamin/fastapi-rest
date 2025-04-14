from fastapi import FastAPI
from app.routes import router
'''
Main FastAPI app Entry point
'''

app = FastAPI()
app.include_router(router)

