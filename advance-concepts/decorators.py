"""
This file contains the basic examples of decorators.
-->  how to definde decorators
-->  Different ways to implement decorators
-->  Using multiple decorators
-->  Using argumnet based decorators
"""

# 1. defining simple decorator: without parameters
def do_something(func):
    def something():
        print("Doing something...")
        func()
        print("Done")  
    return something

# wrapping hello func with do_something decorator
@do_something
def hello():
    print("hello")

# Calling hello funtion
# hello()

# 2. defining argument decorator: without parameters
def print_numbers(func):
    def inner(a,b):
        print("-------------------------------------------------")
        print("The two numbers are {} and {}".format(a, b))
        return func(a,b)
    return inner

# Different ways to implement decorator

# 1. using @ syntax
@print_numbers
def sum(a, b):
    print( a + b )

def subtract(a, b):
    print( a - b)

# sum(5, 4)

# 2. by passing function name as a param to decorator
# output = print_numbers(sum) # return print_numbers object
# output(10, 5) # notice that we are passing the input to this object


"""
########################################CHAINING DECORATORS/ USING MULTIPLE DECORATORS##################################
"""
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("/" * 30)
        func(*args, **kwargs)
        print("/" * 30)
    return inner


# @percent
# @star
def printer(msg):
    print(msg)

printer_sk = percent(star(printer))
printer_sk("Hello")