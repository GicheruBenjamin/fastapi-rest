

from .auth_routes import router as auth_router
from .post_routes import router as post_router
from .user_routes import router as user_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(post_router, prefix="/post", tags=["post"])
router.include_router(user_router, prefix="/user", tags=["user"])

