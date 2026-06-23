class car:
    def __init__(self, brand, model):
        self.__brand = brand  
        self.__model = model


class engine:
    pass
class battery:
    pass
class electric_car(car,engine,battery):
    def __init__(self,brand,model,engine,battery):
        super().__init__(brand,model)
        self.engine=engine
        self.battery=battery
print(isinstance(electric_car("Tesla", "Model S", "Electric Engine", "Lithium-ion Battery"), car))  # True
print(isinstance(electric_car("Tesla", "Model S", "Electric Engine", "Lithium-ion Battery"), engine))  # True
print(isinstance(electric_car("Tesla", "Model S", "Electric Engine", "Lithium-ion Battery"), battery))  # True