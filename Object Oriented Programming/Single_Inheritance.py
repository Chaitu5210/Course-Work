class Father:
    def __init__(self):
        self.familyname="Snowden"

# Child Is Inheriting From Father
class Child(Father):  
    pass

Son=Child()
print("Son's Family Name is ",Son.familyname)





