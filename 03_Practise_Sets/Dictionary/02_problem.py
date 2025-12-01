# Create a nested dictionary & print specific values

students = {
    "S1": {"name": "Rahul", "age": 18, "marks": 88},
    "S2": {"name": "Priya", "age": 17, "marks": 92},
    "S3": {"name": "Karan", "age": 18, "marks": 85},
}

for s in students:
    print(students[s]["name"], "-", students[s]["marks"])
