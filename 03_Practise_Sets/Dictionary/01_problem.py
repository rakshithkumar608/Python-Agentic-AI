# Create a dictionary of 5 students & marks and print the topper

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Students:", students)

# find topper manually
topper = ""
top_marks = -1

for name in students:
    if students[name] > top_marks:
        top_marks = students[name]
        topper = name

print("Topper is", topper, "with", top_marks, "marks")
