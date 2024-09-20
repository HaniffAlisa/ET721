"""
Alisa Haniff
Sept 20, 2024 Python Classes
"""

print("/n-------Example 1: exception handling-----")
def hour_ratio():
    try:
        hours = 24
        h = int(input("Please enter a number to divide 24 hours: "))

        hours /=h #hours = hours/h
        return hours
    except ZeroDivisionError:
        print(f"The number {h} can't be divided by 24. Result is undefined")
    except ValueError:
        print(f"Input value was not a number.")
    except:
        print(f"Program has an error.")


print(hour_ratio())
print("/n ------End of program--------/n")


print("/n-------Example 2: classes-----")
#define a class named 'complex'
class Complex:
    def __init__(self, realpart, imgpart):
        self.r = realpart
        self.i = imgpart
# create an instance of the class
point1 = Complex(3.0, -4.5)

# calling the instance object
real1 = point1.r
imag1 = point1.i

# prompt result
print(f"real number = {real1} with imaginary number = {imag1} ")        
