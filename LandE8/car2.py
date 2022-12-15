# Write your code here :-)
class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
         if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
         else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
         """Add the given amount to the odometer reading."""
         self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)

print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

"""
Now update_odometer() checks that the new reading makes sense before
modifying the attribute. If the new mileage, mileage, is greater than or equal
166 Chapter 9
to the existing mileage, self.odometer_reading, you can update the odometer
reading to the new mileage X. If the new mileage is less than the existing
mileage, you’ll get a warning that you can’t roll back an odometer Y."""

