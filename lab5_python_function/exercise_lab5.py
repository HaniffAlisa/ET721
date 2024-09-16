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

def guess_num():
    guess = random.randint(10, 20)
    num_2 = random.randint(10, 20)
    return guess, num_2

# Generate the guess and num_2
guess, num_2 = guess_num()

print("Guess number:", guess)
print("The second number:", num_2)    

def compare_guess(guess, num_2):
    if num_2 < guess:
        print("The number is smaller than the guess number")
    elif num_2 > guess:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")

# Compare the numbers
compare_guess(guess, num_2)
