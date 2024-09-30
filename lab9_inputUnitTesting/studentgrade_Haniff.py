"""
Alisa HAniff
unit testing 
lab 9"""

def main():
    while True: 
        try: 
            num_students = int(input("Enter the number of students: "))
            if num_students >0:
                break
            else: 
                    print("Invalid inpit.")
        except ValueError: 
            print("Invalid input. Try again")

#nested loop to collect the grade for each students
totalSumGrade =0
for i in range(num_students):
    while True: 
        try: 
            grade = int(input(f"Enter a grade for student {i +1}"))
            if 0< grade <=100:
                totalSumGrade+=grade
                break
            else: print("grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. ")

average = totalSumGrade/num_students
print(f"The class average is [average:.2f]")
if __name__=="__main__":
    main()