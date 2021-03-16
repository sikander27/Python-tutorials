
class Employee:
    def __init__(self, first, last):
        # Instance variable
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@sk.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter #nameofmethod.setter ->convention
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter #nameofmethod.deleter ->convention
    def fullname(self):
        print(f"Deleting employee {self.first}")
        self.first = None
        self.last = None

    
e1 = Employee('Sikande', 'khan')
e1.fullname = "Sikander Khan"
print(e1.email)
print(e1.fullname)
del e1.fullname