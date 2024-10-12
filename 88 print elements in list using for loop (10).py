class Student:
    def __init__(self):
        print("default constructor")
        pass
    
    def __init__(self,fullname,age):
        self.name=fullname
        self.age= age
        print("Adding a new database")
s1 = Student("divya",23)
print(s1.name,s1.age)
s2= Student("Avnish",22)
print(s2.name,s2.age)