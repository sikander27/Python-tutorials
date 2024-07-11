from .classess import Employee


class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, salary, language):
        super().__init__(first, last, salary)
        self.language = language
e1 = Developer('Sikander', 'khan', 5000, 'python')
e2 = Developer('saba', 'khan', 8000, 'javascript')

print(e1.first)
print(e2.language)
# print(e1.raise_amount)