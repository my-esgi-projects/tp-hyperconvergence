class A:
    def __init__(self, B=None) -> None:
        self.A = 2
        self.B = B
        self.C = None


obj = A()

print(vars(obj))
