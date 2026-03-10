from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
    
product_one = Product(
    id=101, 
    name="Laptop",
    price=999.99,
    in_stock = True
    )

product_two = Product(
    id=102, 
    name="keyboard",
    price=24.99,
    )

product_three = Product(
    id=103, 
    name="mouse",
    price=19.99,
    in_stock = False
    )

product = Product(product_one.dict().values())
print(product_one)