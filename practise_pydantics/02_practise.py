#1.Company Employee System

from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import re

class User(BaseModel):
    email: str = Field(
        ...,
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        description="The user's email address"
    )
    
    phone: str = Field(
        ...,
        pattern = r'^\+?[1-9]\d{1,14}$',
        description="The user's phone number"
    )
    
    age: int = Field(
        ...,
        ge = 20,
        description="The User's age",
    )
    
    discount: float = Field(
        ...,
        ge = 0,
        le = 100,
        description="The discount percentage for the user",
        json_schema_extra={"example": 15.5}
    )
    
class Employee(BaseModel):
    id: int
    
    name: str = Field(
        ...,
        min_length = 3,
        max_length= 50,
        description="The employee's full name",
    )
    
    department: Optional[str] = "General"
    
    salary: float = Field(
        ...,
        ge = 15000,
        description="The employee's salary",
        json_schema_extra={"example": 50000}
    )
    
    contact: User
    
class Company(BaseModel):
    company_name: str
    employees: List[Employee]
    
    
company_data = {
    "company_name" : "Tech Solutions Inc.",
    "employees" : [
        {
            "id" : 1,
            "name": "rakshith",
            "department" : "IT",
            "salary": 50000.0,
            "contact" : {
                "email" : "rakshith@example.com",
                "phone" : "+1234567890",
                "age" : 25,
                "discount" : 10.0
            }
        },
        
        {
            "id" : 2,
            "name": "Smit",
            "department" : "HR",
            "salary": 45000.0,
            "contact" : {
                "email" : "smit@example.com",
                "phone" : "+1234567891",
                "age" : 30,
                "discount" : 15.0
            }
        }
    ],
    "description": "A leading technology company specializing in software development and IT services."
}

company = Company(**company_data)
print("Company:", company.company_name)
print()

for emp in company.employees:
    print(f"Employee ID: {emp.id}")
    print(f"Name: {emp.name}")
    print(f"Department: {emp.department}")
    print(f"Salary: {emp.salary}")
    
    print("Contact Information:")
    print(f"Contact Email: {emp.contact.email}")
    print(f"Contact Phone: {emp.contact.phone}")
    print(f"Contact Age: {emp.contact.age}")
    print(f"Contact Discount: {emp.contact.discount}%")
    print("-"*60)