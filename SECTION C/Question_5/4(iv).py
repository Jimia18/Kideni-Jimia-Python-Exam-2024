class Car:
    def __init__(self,brand,color,name):
        
        self.brand = brand
        self.color = color
        self.name = name

car = Car("Toyota", "Red",'corona' )
print(car.brand)
print(car.color)
print(car.name)