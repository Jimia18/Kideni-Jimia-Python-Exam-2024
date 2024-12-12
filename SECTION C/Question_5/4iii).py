class Car:
    def __init__(self,brand,color,name):
        
        self.brand = brand
        self.color = color
        self.name = name

    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} {self.name} has started.")

car = Car("Toyota", "Red", "corona")
car.start_engine()