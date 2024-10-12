#Hiding unnecessary information and displaying only the data required
#Real time scenario we need not tp know the whole mechanism inside what happens in background take an exmple of car.A car has an accelerator, clutch, and break and we all know that pressing an accelerator will increase the speed of the car and applying the brake can stop the car but we don’t know the internal mechanism of the car and how these functionalities can work this detail hiding is known as data abstraction.

#Importance of Data Abstraction
#It enables programmers to hide complex implementation details while just showing users the most crucial data and functions. This abstraction makes it easier to design modular and well-organized code, makes it simpler to understand and maintain, promotes code reuse, and improves developer collaboration.
#Purpose: Abstract classes are used to create a blueprint for other classes. They define methods that must be implemented by any concrete subclass.

from abc import ABC ,abstractmethod

class Dog(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def bark(self):
        print("dog is barking")