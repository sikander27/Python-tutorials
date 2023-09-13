# 0 1 1 2 3 5 

def fibonacci(n):
    count, a, b = 0, 0, 1
    if n <= 1:
        return
    while count < n:
        print(a)
        t = a
        a = t + b
        b = t
        count += 1
    return


def recurFib(n):
    if n <= 1:
        return n
    return recurFib(n-1) + recurFib(n-2)

def printFibo(n):
    for i in range(n):
        print(f"-------------{i}----------------")
        print(recurFib(i))


print(fibonacci(4))
print(printFibo(5))