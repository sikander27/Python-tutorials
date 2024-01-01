class A:
    def m(self):
        print("Class A")


class B(A):
    def m(self):
        print("Class B")
        super().m()


class C(B):
    def m(self):
        print("Class C")
        super().m()


instance = C()

instance.m()
