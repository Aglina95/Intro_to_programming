# Write your code here :-)
class Restaurant:


    def __init__(self, name, cuisine_type):

        self.name = name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):

        print(f"{self.name}'s cuisine type is {self.cuisine_type}")

    def open_restaurant(self):

        print(f"{self.name} is open!")

my_restaurant = Restaurant("Lee's Kitchen", "Chinese")
your_restaurant = Restaurant("20A", "Danish")
other_restaurant = Restaurant("Crete", "Greek")

print(f"My restaurant's name is {my_restaurant.name}.")
print(f"My restautant's cuisine type is {my_restaurant.cuisine_type}.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"My restaurant's name is {your_restaurant.name}.")
print(f"My restautant's cuisine type is {your_restaurant.cuisine_type}.")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

print(f"My restaurant's name is {other_restaurant.name}.")
print(f"My restautant's cuisine type is {other_restaurant.cuisine_type}.")
other_restaurant.describe_restaurant()
other_restaurant.open_restaurant()
