class Method:
    def Main_Method1(self,a,b,c):
        return self.a+self.b+self.c
    def Main_Method1(self,a,b):
        return self.a+self.b

med=Method()
print(med.Main_Method1(1,2))
print(med.Main_Method1(1,2,3))