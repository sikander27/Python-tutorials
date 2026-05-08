"""
Core Quality for Life
"""

class Confidence:
    def __init__(self):
        pass

class Communication(Confidence):
    def __init__(self):
        pass

    def read(self):
        print("Reading...")
        
    def write(self):
        print("Writing...")
        
    def speak(self):
        print("Speaking...")
        
    def listen(self):
        print("Listening...")


class Math:
    def __init__(self):
        pass

    def add(self, a, b):
        print(f"Adding {a} and {b}")
        return a + b

    def subtract(self, a, b):
        print(f"Subtracting {a} and {b}")
        return a - b

    def multiply(self, a, b):
        print(f"Multiplying {a} and {b}")
        return a * b

    def divide(self, a, b):
        print(f"Dividing {a} and {b}")
        return a / b

    def modulo(self, a, b):
        print(f"Modulo {a} and {b}")
        return a % b

    def tables(self, a):
        print(f"Tables of {a}")
        for i in range(1, 11):
            print(f"{a} x {i} = {a * i}")

    def rules(self):
        print("Math Rules")


class HowToLearn:
    def __init__(self):
        pass

    def steps(self):
        print("How to Learn")
        pass

    def tips(self):
        print("Tips")
        pass

    def resources(self):
        print("Resources")
        pass

    def learn(self):
        print("Learn")
        pass

class Etiquette:
    def __init__(self):
        pass

    def dressing(self):
        print("Dressing")
        pass

    def eating(self):
        print("Eating")
        pass

    def manners(self):
        print("Manners")
        pass

    def social(self):
        print("Social")
        pass

class BasicCore(Communication, Math, HowToLearn, Etiquette):

    def __init__(self):
        super().__init__()
    
    def display(self):
        print("---------Basic Core---------")
        print("Communication:")
        print("Math:")
        print("HowToLearn:")
        print("Etiquette:")
        print("-----------------------------")

core = BasicCore()
# core.display()
