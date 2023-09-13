import random


def numberWise(names):
    numbers = list(range(1, len(names)+1))
    result = []
    for name in names:
        number = random.choice(numbers)
        numbers.remove(number)
        result.append((name, number))
    return sorted(result, key=lambda x: x[1])


names = ["yash", "taher", "fazal", "prathamesh", "naved", "sikander"]

print(numberWise(names))