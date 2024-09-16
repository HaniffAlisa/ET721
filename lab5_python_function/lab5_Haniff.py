"""
Alisa Haniff
Sept 16, 2024
Python Functions
"""
import math
import random

# Example 1 define a function to print a message. The function doesn't return nor pass a value
def hellofunction():
    print("Welcome to the hello function!")

#Example 2: function that passes a name as an argument but doesn't return a value 
def greeting(username):
    print(f"Good afternoon {username}")

#Example 3: funtion with default parameter, but doesn't return a value
def usercountry(countryname="USA"):
    print(f"I am from {countryname}")

#Example 4- function that passes and returns a value
def triplenumber(num=0):
    return 3*num   

#Example 5: function that passes two numbers and checks if the two numbers are divisible by each other and false if not divisible
def isDivisible(n1,n2):
    if(n1%n2 == 0 or n2%n1 == 0):
        return True
    else:
        return False

 #Example 6: function that passes a radius and returns the circumference   
def circumference(radius=0):
    return 2*math.pi*radius
    
#Example 8: function that returns a Random numbers btw 1-6
def rollDice():
    return random.randint(1,6)


#call a function
print("\n----Example 1------")
hellofunction()    

print("\n----Example 2------")
username = "peterpan123"
greeting(username)    

print("\n----Example 3:function with default parameter------")
usercountry("guyana")
usercountry()

print("\n----Example 4: triple the number------")
n=9
print(f"THe triple of the number {n} is {triplenumber(n)}")

print("\n -----Example 5: function that passes two numbers and checks if the two numbers are divisible by each other and false if not divisible-------")
n1=10
n2=50
check1 = isDivisible(n1,n2)
print(f"Is {n1} and {n2} divisible? {check1}")

print("\n ---------#Example 6: function that passes a radius and returns the circumference-----")
r=5
c=circumference(r)
print(f"A circle with a radius {r} has a circumference of {c:.2f}") #c:.2f makes 2 decial places

print("\n -------#Example 7: Random numbers---------")
print(f"random number {random.random()}")
print(f"rndom uniform {random.uniform(-5,5)}")
print(f"random.randint {random.randint(-10,10)}")

print("\n------Example 8: function that returns a Random numbers btw 1-6-------")
print(f"dice number = {random.randint(1,6)}")


