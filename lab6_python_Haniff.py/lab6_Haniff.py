"""
Alisa Haniff
Sept 20, 2024 Python Classes
"""

print("/n-------Example 1: exception handling-----")
def hour_ratio():
    hours = 24
    h = int(input("Please enter a number to divide 24 hours: "))

    hours /=h #hours = hours/h
    return hours
except ZeroDivisionError:
    print(f"The number {h} can't be divided by 24. Result is undefined")
except ValueError
    print(f"Input value was not a number.")
except:
    print(f"Program has an error.")


print(hour_ratio())
print("/n ------End of program--------/n")