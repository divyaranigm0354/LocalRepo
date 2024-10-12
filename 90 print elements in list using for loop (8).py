#methods dont use parameter and they work at class level
#Decorators can be used for both regular functions and class methods. When used with class methods, decorators like @staticmethod and @classmethod are common in Python.
class student:
    @staticmethod
    def college():
        print("ABC College")