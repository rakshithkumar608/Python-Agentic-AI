from pydantic import BaseModel, Field
from typing import  Optional
import re

class Employee(BaseModel):
    id: int
    
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="The employee's full name",
        example="Rakshith"
    )
    
    department: Optional[str] = 'General'
    
    salary: float = Field(
        ...,
        ge=15000,
        description="The employee's salary",
        example=50000.0
    )
    

class User(BaseModel):
    email: str = Field(
        ...,
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        description="The user's email address",
        example="john.doe@example.com"
    )
    phone: str = Field(
        ...,
        regex = r'^\+?[1-9]\d{1,14}$',
        description="The user's phone number",
        example="+1234567890"
    )
    age: int = Field(
        ...,
        ge=18,
        description="The user's age",
        example=30
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="The discount percentage for the user",
        example=15.5
    )