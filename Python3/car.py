class Car():
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.odo_reading = 1000

    def describe_car(self):
        brand = f"{self.make} {self.model} {self.color}"
        return brand
    
    def read_odometer(self):
        print(f"The car has driven {self.odo_reading} miles.")
    
    def meter_reading(self,mileage):
        self.odo_reading = mileage

my_car = Car('Audi', 'Q3', 'Black')
print(my_car.describe_car())
my_car.odo_reading = '11k'
my_car.read_odometer()
my_car.meter_reading(11000)
my_car.read_odometer()


