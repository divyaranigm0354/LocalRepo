from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# This will work because both Dog and Cat implement the abstract method `sound`
dog = Dog()
dog.sound()  # Output: Bark

# Attempting to instantiate Animal will raise an error
# animal = Animal()  # Raises TypeError: Can't instantiate abstract class

#An abstract method is a method declared in an abstract class, which does not provide any concrete implementation. Subclasses inheriting from the abstract class are required to implement these abstract methods, otherwise, the subclass will also be treated as abstract.

