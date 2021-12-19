
def isDivisible(x):
    if x < 0:
        return "Please enter number greater than zero"
    if x % 9 == 0 or x % 3 ==0:
        return "Yes"
    else:
        return "No"

x = isDivisible(5)
print(x)