from fastapi import APIRouter

router = APIRouter()

# Sample CRUD routes
@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": "Item details"}

@router.post("/items/")
def create_item(name: str, description: str):
    return {"name": name, "description": description}
