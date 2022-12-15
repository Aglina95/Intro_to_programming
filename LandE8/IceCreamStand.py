# Write your code here :-)
class Restaurant:


    def __init__(self, name, cuisine_type):

        self.name = name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):

        print(f"{self.name}'s cuisine type is {self.cuisine_type}")

    def open_restaurant(self):

        print(f"{self.name} is open!")

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
            """Initialize attributes of the parent class."""
            super().__init__(name, cuisine_type)
            self.flavors = ["strawberry", "chocolate", "pistachio"]

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


my_restaurant = IceCreamStand("Angelina's", "Ice-cream shop")
my_restaurant.show_flavors()
