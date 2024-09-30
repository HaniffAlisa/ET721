"""
Alisa HAniff
unit testing student grades
lab 9"""

def main():
    while True: 
        try: 
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                break
            else: 
                print("Invalid input. Please enter a positive number.")
        except ValueError: 
            print("Invalid input. Try again.")

    # Nested loop to collect the grades for each student
    total_sum_grade = 0
    for i in range(num_students):
        while True: 
            try: 
                grade = int(input(f"Enter a grade for student {i + 1}: "))
                if 0 < grade <= 100:
                    total_sum_grade += grade
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = total_sum_grade / num_students
    print(f"The class average is {average:.2f}")

if __name__ == "__main__":
    main()

