from pydantic import BaseModel, Field

class Order(BaseModel):
    
    product_price: float = Field(
        ...,
        ge = 0
    )
    
    tax: float = Field(
        ...,
        ge=0
    )
    
    discount: float = Field(
        ...,
        ge=0
    )
    
    def final_price(self):
        return self.product_price + self.tax - self.discount
    
order = Order(
    product_price=1000,
    tax=100,
    discount=200     
)

print("Order Details:", order)
print("Final Price:", order.final_price())


#### Age 

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    
    def is_adult(self):
        return self.age >= 18
    
user = User(name="Rkashith", age=21)

print(user.is_adult())


#### Product Model

from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(
        ...,
        ge=0
    )
    
    discount: float = Field(
        ...,
        ge=0
    )
    
    def final_product(self):
        return self.price - self.discount
    
product = Product(
    name = "Laptop",
    price = 1000,
    discount=200
)

print("Order Details:", product)
print("Final Price of Product:", product.final_product())


# combined Example

from pydantic import BaseModel, Field, field_validator

class Order(BaseModel):
    
    price: float = Field(
        ...,
        ge=0
    )
    discount: float = Field(
        ...,
        ge=0
    )
    
    @field_validator("discount")
    def check_discount(cls, value, info):
        price = info.data.get("price")
        
        if price and value > price:
            raise ValueError("Discount cannot exceed price")
        return value
    
    
    def final_price(self):
        return self.price - self.discount
    
order = Order(
    price = 10000,
    discount= 200
)

print(order.final_price())