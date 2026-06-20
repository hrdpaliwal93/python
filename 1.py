# create a class CARS with attributes brand and model, create an instance of this class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
car = Car("bmw", "m4")

print("the model ",car.model,"belongs to the ",car.brand,"brand")