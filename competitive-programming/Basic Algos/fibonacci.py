def fibonacci(n):
    i = 0
    a, b = 0, 1
    while i < n:
        print(a)
        a, b = a + b, a
        i += 1

    return 

def fibonacci_list(n):
    i = 0
    a, b = 0, 1
    result = []
    while i < n:
        result.append(a)
        a, b = a + b, a
        i += 1
    print(result)
    return result

# 3 -> 2(1) + 1(1)
# 2 -> 1 + 0
def fibonacci_recursion(n):
    """
    This function return the fibonacci number at nth position
    """
    if n < 2:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_series_recursin(n):
    res = []
    for i in range(n):
        res.append(fibonacci_recursion(i))
    return res

a = fibonacci_series_recursin(7)
print(a)