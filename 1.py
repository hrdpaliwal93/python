# create a class CARS with attributes brand and model, create an instance of this class

class Car:
    def __init__(self, brand, model):
        # this init function is mainly used to establish a connection between the class and the called object of this class. it is a constructor used to initialize the object 

        #the object has the access of itself using the SELF keyword
        #self recceives the object that called the method, stores the value inside the specific object that called the method.
        self.brand = brand
        self.model = model
car = Car("bmw", "m4")

print("the model ",car.model,"belongs to the ",car.brand,"brand")