from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    password: str
    
    @field_validator("password")
    def validate_password(cls, value):
        
        if len(value) < 8:
            raise ValueError("Password must br greater than 8 characters")
        
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain a number")
        
        return value
    
user = User(
    username="rakshi",
    password="rakshi17"
)

print(user)


# 2. Discountt

from dis import disco
from pydantic import BaseModel, field_validator


class Product(BaseModel):
    name: str
    price: float
    discount: float

    @field_validator("discount")
    def validate_discount(cls, value, info):

        price = info.data.get("price")

        if price and value > price:
            raise ValueError("Discount cannot exceed price")

        return value


product = Product(
    name="Laptop",
    price=50000,
    discount=5000
)

print(product)


# Order summery

from pydantic import BaseModel, field_validator, Field

class Order(BaseModel):
    product_price: float = Field(
        ...,
        ge=0
    )
    tax: float = Field(
        ...,
        ge=0
    )
    discount: float = Field(
        ...,
        ge=0
    )
    
    @field_validator("discount")
    def validate_tax(cls, value, info):
        
        price = info.data.get("product_price")
        
        if price is not None and value > price:
            raise ValueError("Discount cannot be greater then product price")
        
        return value
    
order = Order(
    product_price=1000,
    tax=100,
    discount=200
)

print(order)