"""---------Example 3------------
            Alisa Haniff
verify if the email, full name, and salary fields are correctly formatted"""

class Employee:
    raise_amt = 1.05
    
    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary
    
    #property decorator indicates that the methos will behave like an attribute
    @property    
    def emailEmployee(self):
        return f"{self.first}{self.last}@email.com"
    
    @property
    def fullname(self):
        return f" {self.last}, {self.first}"
    
    def apply_raise(self):
        self.salary = int(self.salary*self.raise_amt)
        