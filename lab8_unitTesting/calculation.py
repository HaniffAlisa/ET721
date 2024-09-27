""" Alisa Haniff
    Example 2: calculation testing
"""

def addThreeNumbers(n1=0,n2=0,n3=0):
    return n1+n2+n3
    
def subtractTwoNumbers(n1=0,n2=0):
    return n1-n2

def multiplyThreeNumbers(n1=1, n2=1, n3=1):
    return n1*n2*n3

def divideTwoNumbers(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("Error! can't divide by zero")        
    except ValueError:
        print("Error! not a numerical value")            
    except:
        print("Error! can't divide the numbers")            