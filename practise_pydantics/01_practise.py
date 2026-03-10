#1. Online shooping Cart

from pydantic import BaseModel
from typing import List, Dict

class ShoopingCart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

cart_data = {
    "user_id": 101,
    "items": ["Shoes", "T-shirt", "Jeans"],
    "quantities": {
        "Shoes": 1,
        "T-shirt": 2,
        "Jeans": 1
    }
}

cart = ShoopingCart(**cart_data)
print(cart)


# 2.Student + Address

from pydantic import BaseModel
from typing import List, Dict, Optional

class Address(BaseModel):
    city: str
    state: str
    pincode: int
    
class Student(BaseModel):
    name: str
    age: int
    address: Address
    
student_data = {
    "name" : "Rakshith",
    "age": 20,
    "address": {
        "city" : "Devanahalli",
        "state": "Karnataka",
        "pincode": 562110
    }
}

student = Student(**student_data)
print(student)


#3.Teacher + Subject

from pydantic import BaseModel
from typing import List


class Subject(BaseModel):
    subject_name: str
    marks: str
    
class Teacher(BaseModel):
    name: str
    age: int
    subjects: List[Subject]
    
teacher_data = {
    "name": "Mr.Smit",
    "age": 25,
    "subjects" : [
        {
            "subject_name": "Maths", 
            "marks": "A"
        },
        
        {
            "subject_name": "Science", 
            "marks": "B"
        },
        
        {
            "subject_name": "History", 
            "marks": "A"
        }
    ]
}

teacher = Teacher(**teacher_data)
print(teacher)


#4. Blog Post + Comments

from pydantic import BaseModel
from typing import List, Optional

class Instructor(BaseModel):
    name: str
    email: str
    
class Student(BaseModel):
    name: str
    age: int

class Course(BaseModel):
    course_name: str
    instructor: Instructor
    students: List[Student]
    description: Optional[str] = None
    
course_data = {
    "course_name" : "Web Development",
    "instructor": {
        "name" : "rahul",
        "email" : "rahul@example.com",
    },
    "students" : [
        {
            "name": "Alice",
            "age": 22
        },
        {
            "name": "Bob",
            "age": 24
        },
        {
            "name": "Charlie",
            "age": 21
        }
    ],
    "description": "Learn web development from scratch!"
}

course = Course(**course_data)
print(course)