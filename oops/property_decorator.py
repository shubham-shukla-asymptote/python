#property_decorator is a built-in function that allows us to define getter and setter methods for class attributes, providing a way to control access to those attributes.

class car:
    counter = 0
    def __init__(self, brand, model):
        self.__brand = brand  
        self.__model = model 
        car.counter += 1
    @property
    def model(self):
        return self.__model
    
    @property
    def brand(self):
        return self.__brand

car1 = car("Toyota", "Camry")


#car1.model = "Corolla"  # This will not change the __model attribute of car1, it will create a new attribute named model in the instance's namespace
#print(car1.model) # this will print "Corolla" bcause we have created a new attribute named model in the instance's namespace

# print(car1.__brand)  # This will raise an AttributeError because __brand is a private attribute

car1.__brand = "Honda"  # This will not change the __brand attribute of car1, it will create a new attribute named __brand in the instance's namespace but after apllying the property decorator, it will not create a new attribute named __brand in the instance's namespace, it will change the value of the __brand attribute of car1 to "Honda"

print(car1.__brand)  # now it will print "Honda" beacuase we have created a new attribute named __brand until we apply the property decorator
print(car1.model)  # this will print "Camry" because we have defined a property for model
print(car1.__dict__)  #{'_car__brand': 'Toyota', '_car__model': 'Camry', '__brand': 'Honda'}
    