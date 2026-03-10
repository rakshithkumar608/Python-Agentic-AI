
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


class Address(BaseModel): 
    street: str 
    city: str
    postal_code: str
    
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    createdAt: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v:v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    
user = User(
    id = 1,
    name = "Rakshith",
    email = "rakshi@example.com",
    is_active = True,
    createdAt = datetime(2026, 1, 1, 12, 0, 0),
    address=Address(
        street="123 Main St",
        city="Anytown",
        postal_code="12345"
    ),
    tags=["premium", "subscribers"]
)

python_dict = user.model_dump()
print(user)
print("-"*60)
print(python_dict)

json_str = user.model_dump_json()
print("-"*60)
print(json_str)