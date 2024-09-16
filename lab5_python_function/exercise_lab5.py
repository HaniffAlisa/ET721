"""
Alisa Haniff
Exercise for Lab 5
Exercise (Guess a number) description: 

define a function that generates and returns a random integer between two numbers, one number is the minimum and the other number is the maximum number. The minimum and maximum number is passed to the function as arguments.
define a function that compares a guess number. The guess number is defined as a constant. The function to print a message as the following:
"The number is smaller than the guess number" if the number is smaller than the guess number.
"The number is bigger than the guess number" if the number is bigger than the guess number.
"You got it!" if the number is equal to the guess number
Submission: 
"""
import random

def guessNum(min,max):
    if(min<max):
        return True
    else:
        return False
print(f"The guess nummber is: {random.randint(10,20)}")