from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
    
class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    
    
cart_data = {
    "user_id": 123,
    "items" : ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"Laptop": 1, "Mouse": 2, "Keyboard": 1}
}

blog_data = {
    "title": "Welcome to my first Blog!",
    "content": "This is the content of my first blog post.",
    "image_url": None
}

cart = Cart(**cart_data)
print(cart)

blog = BlogPost(**blog_data)
print(blog)