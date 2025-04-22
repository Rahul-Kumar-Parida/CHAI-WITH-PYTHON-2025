"""
#1)Basic Class and Object
#Create a car class with attributes like brand and model. Then create an instance of this class.
class car:   #Class
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_class=car("Toyota","Corolla")
print(my_class.brand)
print(my_class.model)

my_new_car=car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)
"""
"""
#2)Class Method and Self
#Add a method to the Car Class That displays the full name of the car (Brand and Model)


class car:   #Class
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.model}"

my_class=car("Toyota","Corolla")
print(my_class.display())
"""

"""
#3)Inheritance
#Create an ElectricCar class that inherits from the Car Class and has an additional attribute battery_size.

class Car:   #Class
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_Ecar=ElectricCar("Tata","Safari",230)
print(my_Ecar.battery_size)
print(my_Ecar.model)
print(my_Ecar.brand)
print(my_Ecar.display())

"""
"""
#4)Encapsulation
#Modify the Car Class to Encapsulate the brand attribute, making it private, provide a getter method for it.

class Car:   #Class
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return self.__brand +" ! "
    def display(self):  #methods
        return f"The car name is {self.__brand} and model is {self.model}"

my_car=Car("Tata","Safari")
# print(my_car.brand)
print(my_car.get_brand())
print(my_car.display())
"""

"""
#5)Polymorphism
#Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar Classes, but with different behaviours.

class Car:   #Class
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.model}"
    def fuel_type(self):
        return f"Petrol or Disel"
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return f"Electric Charge"
    

my_tesla=ElectricCar("Tesla","Model","89KWh")
print(my_tesla.fuel_type())

safari=Car("Tata","Safari")
print(safari.fuel_type())

"""
"""
#6)Class Variable
#Add a class Variable to Car that keeps track of the numbers of cars created.
class Car:   #Class
    total_Car=0

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_Car+=1
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.model}"
    def fuel_type(self):
        return f"Petrol or Disel"
    

safari1=Car("Tata","Safari")
safari2=Car("Tata","Safari")
safari3=Car("Tata","Safari")
Car("Tata","Safari")
print(safari1.fuel_type())
print(Car.total_Car)
"""

"""
#7)Static Method
# Add a static method to the car Class that returns a general description of a car

class Car:   #Class
    total_Car=0

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_Car+=1
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.model}"
    def fuel_type(self):
        return f"Petrol or Disel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport! "


my_car = Car("Tata","Safari")
Car("Tata","Nexon")

print(my_car.general_description())
print(Car.general_description())
"""
"""
#8) Property Decorators
#Use a property decorator in the Car Class to make the model attribute read_only.


class Car:   #Class
    total_Car=0

    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
        Car.total_Car+=1
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.__model}"
    def fuel_type(self):
        return f"Petrol or Disel"
        
    @staticmethod
    def general_description():
        return "Cars are means of transport! "
    
    @property
    def model(self):
        return self.__model


my_car = Car("Tata","Safari")
# my_car.model="City"
Car("Tata","Nexon")
print(my_car.model)

"""

"""
#9)Class Inheritance and Isinstance() Functions
#Demonstrate the use of isinstance() to check if my_tesla is an instance of car and electricCar.


class Car:   #Class
    total_Car=0

    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
        Car.total_Car+=1
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.__model}"
    def fuel_type(self):
        return f"Petrol or Disel"
        
    @staticmethod
    def general_description():
        return "Cars are means of transport! "
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return f"Electric Charge"


my_tesla=ElectricCar("Tesla","Model","89KWh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla,ElectricCar))

"""
"""
#10)Multiple Inheritance
#Create two classes Battery and Engine, and let the ElectricCar Class inherit from both, demonstrating multiple inheritance.
class Car:   #Class
    total_Car=0

    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
        Car.total_Car+=1
    def display(self):  #methods
        return f"The car name is {self.brand} and model is {self.__model}"
    def fuel_type(self):
        return f"Petrol or Disel"
        
    @staticmethod
    def general_description():
        return "Cars are means of transport! "
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return f"Electric Charge"


# my_tesla=ElectricCar("Tesla","Model","89KWh")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla,ElectricCar))

class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla=ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

"""




