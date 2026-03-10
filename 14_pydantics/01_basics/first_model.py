from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
user_data = {
    "id": 1,
    "name": "Alice",
    "is_active": True
}

user = User(**user_data)
print(user) 