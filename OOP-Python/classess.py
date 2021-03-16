#OOP -> Classes
class Employee:
    # pass #if class is empty use 
    # Class variable
    num_of_emps = 0
    raise_amount = 2.07

    def __init__(self, first, last, salary):
        # Instance variable
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@sk.com'
        self.salary = salary

        Employee.num_of_emps += 1

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.salary)

    def __str__(self):
        return f'{self.first} {self.last}'
    #each method inside a class 
    #always take first argument as instant i.e. self
    def info(self):
        return '{} {} get paid {} on email: {}'.format(self.first,
        self.last,
        self.salary,
        self.email
        )

    #regular method
    def raise_salary(self):
        self.salary = int(self.salary * self.raise_amount)#can also use Employee.raise_amount
        
    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amount = amt

    @classmethod #alternative constructor method
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod #when have logical connection, don't take first argument as instance
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 

    #few special methods
    def __add__(self, other):
        return self.salary + other.salary

'''--------Class method----------'''
# import datetime
# my_date = datetime.date(2016, 7, 12)
# print(Employee.is_workday(my_date))

'''--------Class method----------'''
# emp_1 = 'sikander-shakil-9000'
# #from_stringis like an alternative construct where 
# # we are performing some function on it.
# new_emp = Employee.from_string(emp_1)
# print(new_emp.__dict__)

# Employee.set_raise_amt(3)
# print(Employee.raise_amount)
# print(new_emp.raise_amount)



'''--------Creating Instance----------'''
e1 = Employee('Sikander', 'khan', 5000)
e2 = Employee('saba', 'khan', 8000)

# print(e2 +e1)
# print(repr(e1))
# print(str(e1))
 
'''--------Calling methods----------'''
# print(Employee.__dict__)
# print(e2.__dict__)

'''--------Calling methods----------'''
#Need to pass the instance(self) argument on Class
# print(Employee.info(e2)) 

# We don't have to pass instance(self) argument on instance
# print(e1.info()) #don't forget to add parenthesis/bracket
# print(e2)



'''--------Manual Assignment----------'''
# manual assignment
# e1.name = "sikander"
# e2.name =" saba"