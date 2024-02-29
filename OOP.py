class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.odometer_reading = 0
        
  
    def get_description(self):
        return f"{self.year} {self.make} {self.model} {self.color}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car("Toyota", "Camry", 2020, "Black")


print(my_car.get_description())
print(my_car.read_odometer())

my_car.update_odometer(15000)
print(my_car.read_odometer())

my_car.increment_odometer(100)
print(my_car.read_odometer())