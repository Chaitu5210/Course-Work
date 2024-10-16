class Father:
    def __init__(self):
        self.fat_fathername="TOM"
        self.fat_mothername="TIMTOM"
        super().__init__()


class Mother:
    def __init__(self):
        self.mot_fathername="Bab"
        self.mot_mothername="Baby"
        super().__init__()

class Son(Father,Mother):
    def __init__(self):
        super().__init__()

son=Son()
print("Father side Father Name: ",son.fat_fathername)
print("Father side Mother Name: ",son.fat_mothername)
print("Mother side Father Name: ",son.mot_fathername)
print("Mother side Mother Name: ",son.mot_mothername)