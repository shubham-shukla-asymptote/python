# polymorphism can be achieved in python through method overriding and duck typing 
#it helps us to use a single interface to represent different types of data or objects. In method overriding, a child class can provide a specific implementation of a method that is already defined in its parent class. this allows us to call the same method on different objects and have it behave differently based on the object's class.
class car:
    brand=None
    @staticmethod   # this is a static method, which means it can be called on the class itself without needing an instance of the class. Static methods are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables. 
    def description():
        print("This is a car")
    def __init__(self,brand):
        self.brand=brand
    def fuel_type(self):
        return "petrol"

class electric_car(car):
    def __init__(self,brand):
        super().__init__(brand)
    def fuel_type(self):
        return "electricity"
    
car1=car("Toyota")
car2=electric_car("Tesla") 
print(car1.fuel_type(),car2.fuel_type()) 
# In this example, we have a parent class car with a method fuel_type that returns "petrol". The electric_car class inherits from the car class and overrides the fuel_type method to return "electricity". When we create instances of both classes and call the fuel_type method, we get different outputs based on the class of the object, demonstrating polymorphism.

#duck type example
class bird:
    def fly(self):
        return "I can fly"
class airplane: 
    def fly(self):
        return "I can fly too"
    def make_it_fly(thing):
        return thing.fly()
bird1=bird()
plane1=airplane()
print(airplane.make_it_fly(bird1))
print(airplane.make_it_fly(plane1))
