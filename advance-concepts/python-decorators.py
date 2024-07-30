# Functions are object
# Inner function

# def parent():
#     print("Hi from parent..")

#     # locally scope
#     def child():
#         print("Hi from child")
#     child()


# parent()
# # child() # calling child will give error









# 1. defining simple decorator: without parameters
# def do_something(func):
#     def something():
#         print("Doing something...")
#         func()
#         print("Done")  
#     return something


# # wrapping hello func with do_something decorator
# @do_something
# def hello(name):
#     print(f"hello {name}")

# hello = do_something(hello)
# hello()






# 2. defining simple decorator: with parameters
# def do_something(func):
#     def something(*args, **kwargs):
#         print("Doing something...")
#         func(*args, **kwargs)
#         print("Done")  
#     return something

# # wrapping hello func with do_something decorator
# @do_something
# def hello(name):
#     print(f"hello {name}")

# hello("Guys")
# # return func from inner func

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner


# def percent(func):
#     def inner(*args, **kwargs):
#         print("/" * 30)
#         func(*args, **kwargs)
#         print("/" * 30)
#     return inner

# @percent
# @star
# def printer(msg):
#     print(msg)

# # printer = percent(star(printer))
# printer("tell me...")














import functools
# 2. defining simple decorator: with parameters
def do_something(func):
    @functools.wraps(func)
    def something(*args, **kwargs):
        print("Doing something...")
        func(*args, **kwargs)
        print("Done")  
    return something

# wrapping hello func with do_something decorator
@do_something
def hello(name):
    print(f"hello {name}")








# base decorator boilerplate
# import functools
# def decorator(func):
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return inner





# Few real life use case
# import functools
# import time

# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__}() in {run_time:.4f} secs")
#         return value
#     return wrapper_timer

# @timer
# def do_somethign():
#     for _ in range(100):
#         print("....")

# do_somethign()



# import functools
# def debug(func):
#     """Print the function signature and return value"""
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__}() returned {repr(value)}")
#         return value
#     return wrapper_debug

# @debug
# def add(a, b):
#     return a + b
    

# add(2, 4)




# Decorator is a function that wraps another function
# A decorator is a function that takes a function as argument
# and returns a function