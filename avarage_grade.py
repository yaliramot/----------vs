from youngfrotech import student_grades, sum
student_grades={"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
student_grades["noam"]=48 # Add a new student's grade

student_grades["Alice"]=95  # Update Alice's grade


avarage_grade = sum(student_grades.values()) / len(student_grades) # Calculate the average grade
print(f"Average grade: {avarage_grade:.2f}")

del student_grades["Charlie"]  # Remove Charlie's grade

# Check if a student is in the class
# This code checks if a specific student is in the class and prints a message accordingly
student_name = "ema"
if student_name in student_grades:
    print(f"{student_name} is in the class.")
else:
    print(f"{student_name} is not in the class.")   
