"""
full name 
lab 3, Python review
"""

print("-----Example 1: control flow-----")
labs = int(input("Enter labs grade: "))
exams = int(input("Enter exams grade: "))

gpa = 'undefined'
finalgrade = 0

if 0 <= labs <= 100 and 0 <= exams <= 100:
    finalgrade = (labs + exams) / 2
    if 90 <= finalgrade <= 100:
        gpa = 'A'
    elif 80 <= finalgrade < 90:
        gpa = 'B'
    elif 70 <= finalgrade < 80:
        gpa = 'C'
    elif 60 <= finalgrade < 70:
        gpa = 'D'
    elif finalgrade < 60:
        gpa = 'F'
else:
    print(f"Your final grades for labs ({labs}) and exams ({exams}) are invalid.")

print(f"Your final grade for the class is {gpa}")

print("--------Example 2: Loops ----------")
SECRET = 9
userguess = int(input("Guess a number between 1 and 10: "))

while userguess != SECRET:
    userguess = int(input("Wrong guess. Guess again: "))

print(f"Congrats! {userguess} is the right number!")

print("-------Example 3 ------- Loops, break statement---------")
balance = 1000
widthdraw = 0
deposit = 0

while True:
    userinput = input("Do you want to withdraw, w, or deposit, d ? ")
    if userinput == 'w' or userinput == 'W' :
        w_amount = int(input('How much do you want to widthdraw? '))
        if w_amount>balance:
            print(f"Insuficient funds! You can't widthdraw more than {balance} ")
        else:
            balance -= w_amount
            print(f"Your new balance is {balance}")
    elif userinput == 'd' or userinput == 'D' :
        d_amount = int(input('Hpw much do you want to deposit? '))
        balance += d_amount
        print(f"Your new balance is {balance}")
    else:
        print("Invalid selection!")
    choice = input("Would you like to make another transaction? (y,n)")
    if not(choice=='y' or choice =='Y'):
        break    
    
print(f"Thank you for banking with us!")                   



print(f"------example 4: for loop as a counter -----")

for n in range(-5,3,2):
    print(f"counting = {n}")
    
print("-------example 5: for loop in a list--------") 
colors = ['magenta'. 'babyblue', 'olive']

for c in colors:
    print(f"color = {c}")
       