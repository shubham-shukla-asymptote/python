#encapsulation is the concept of bundling data and methods that operate on that data within  a single unit such as a class.
class car:
    __brand=None
    __model=None
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
    # def set_brand(self,brand):
    #     self.__brand=brand
    # def get_brand(self):
    #     return self.__brand
    # def get_model(self):
    #     return self.__model
    # def set_model(self, model):
    #     self.__model=model
    # def get_model(self):
    #     return self.__model
# my_car=car('Toyota', 'Camry')
# # my_car.set_brand("Toyota")
# print(my_car.get_brand()) 
# print(my_car.__brand) ## this will give an error because __brand is a private attribute and cannot be accessed directly from outside the class. We have to use the getter method get_brand() to access the value of __brand.





my_car=car('Toyota', 'Camry')


print(my_car.model) #AttributeError: 'car' object has no attribute 'model'
