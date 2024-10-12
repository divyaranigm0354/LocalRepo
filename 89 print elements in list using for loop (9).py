#Methods in python are the function of a object in the class
class Student:
    def __init__(self,name):
        self.name=name
    
    def hello(self):
        print("hello:",self.name)

S1=Student("avnish")
print(S1.name)
S1.hello()