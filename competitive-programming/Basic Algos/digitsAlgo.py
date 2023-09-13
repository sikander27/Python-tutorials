def sumOfDigits(n):
    """
        Function to Calculate Sum of Digits of a number
        args:
            - n : number(int)
    """
    result = 0
    while n > 0:
        digit = n % 10
        result += digit
        n = n // 10
    return result


def productOfDigits(n):
    """
        Function to Calculate Product of Digits of a number
        args:
            - n : number(int)
    """
    result = 1
    while n > 0:
        digit = n % 10
        result *= digit
        n = n // 10
    return result


print(sumOfDigits(345))
print(productOfDigits(3445))
