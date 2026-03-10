# E-Commerce System Example

from pydantic import BaseModel, Field
from typing import List, Optional

# User Information

class User(BaseModel):
    name: str = Field(
        ...,
        min_length= 5,
        max_length= 50,
    )
    
    email: str = Field(
        ...,
        pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    )
    
    phone: str = Field(
        ...,
        pattern=r'^\+?[1-9]\d{1,14}$',
    )
    
#Product detail's
    
class Product(BaseModel):
    id: int
    name: str
    price: int = Field(
        ...,
        ge=0
    )
    in_stock: bool = True
    
#Order Details

class Order(BaseModel):
    order_id: int
    user: User
    product: List[Product]
    total_price: float = Field(
        ...,
        ge=0
    )
    
# company Details

class Company(BaseModel):
    company_name: str
    orders: List[Order]
    
company_data = {
    "company_name" : "RJ Privae Ltd.",
    "orders": [
        {
            "order_id" : 101,
            "user" : {
                "name": "Rakshith",
                "email": "rakshi@gmail.com",
                "phone": "+91111223344"
            },
            "product" : [
                {
                    "id" : 1,
                    "name" : "laptop",
                    "price" : 20000,
                },
                {
                    "id": 2,
                    "name": "Mouse",
                    "price": 2000
                },
            ],
            "total_price" : 22000
        },
        
        {
            "order_id" : 102,
            "user" : {
                "name": "Jayanth",
                "email": "jay@gmail.com",
                "phone": "+9111122998"
            },
            "product" : [
                {
                    "id" : 3,
                    "name" : "Mobile",
                    "price" : 22000,
                },
                {
                    "id": 4,
                    "name": "Mobile Cover",
                    "price": 1000
                },
            ],
            "total_price" : 23000
        },
    ]
}

company = Company(**company_data)
print("Company:", company.company_name)
print()

for order in company.orders:
    print(f"Order ID: {order.order_id}")

    print("Customer:")
    print(f"Name: {order.user.name}")
    print(f"Email: {order.user.email}")
    print(f"Phone: {order.user.phone}")

    print("Products:")
    for product in order.product:
        print(f"Product ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Price: {product.price}")
        print(f"In Stock: {product.in_stock}")
        print()

    print(f"Total Price: {order.total_price}")
    print("-" * 40)