"""
full name 
lab 3, Python review
"""

print("-----Example 1: control flow-----")
labs = int(input("Enter labs 'grade:'"))
exams = int(input("Enter exams' grade:"))

gpa = 0
finalgrade=0

if (0<=labs<=100 and 0<=exams<=100):
    finalgrade = (labs+exams) / 2
    if (100>=finalgrade>=90):
    gpa = 'A'
    elif (90>finalgrade>=80):
    gpa = 'B'
    elif (80>finalgrade>=70):
    gpa = 'C'      
    elif (70>finalgrade>=60):
    gpa = 'D'
    elif (60>finalgrade>=00):
    gpa = 'F' 
else:
    print(f"your final grade for labs = {labs} and exams = {exams} are invalid")
    gpa = 'undefined'
    
print(f"Your final grade for the classis {gpa}")                   