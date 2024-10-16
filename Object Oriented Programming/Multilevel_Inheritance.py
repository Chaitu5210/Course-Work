class GrandFather:
    def __init__(self):
        self.surname="Gokaraju"
        super().__init__()


class Father(GrandFather):
    def __init__(self):
        super().__init__()


class Son(Father):
    def __init__(self):
        super().__init__()


son=Son()
print("surname is ",son.surname)
