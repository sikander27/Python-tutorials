def recurHelper(n):
    if n <= 1:
        return n
    return recurHelper(n-1) + recurHelper(n-2)

def validateNumber(func):
    def inner(*args, **kwargs):
        # import pdb; pdb.set_trace()
        n = args[0]
        if n <= 0:
            print("Please enter positive number.")
            return
        return func(*args, **kwargs)
    return inner

@validateNumber
def fibonacci(n):
    for i in range(n):
        print(recurHelper(i))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


fibonacci(0)
# print(factorial(2))
