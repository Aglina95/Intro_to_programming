# Write your code here :-)
class Restaurant:
    def __init__(self, name, cuisine_type, number_served):

        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        print(f"{self.name}'s cuisine type is {self.cuisine_type}")

    def open_restaurant(self):

        print(f"{self.name} is open!")

    def number_of_customers(self):
        print(f"{self.number_served} customers have been served in a business day!")

    def set_number_served(self, customers_served):
        if customers_served >= self.number_served:
            self.number_served = customers_served
        else:
            print("This is wrong")

    def increment_number_served(self, customers):
         """Add the given amount to the odometer reading."""
         self.number_served += customers


my_restaurant = Restaurant("Lee's Kitchen", "Chinese", 10)
my_restaurant.set_number_served(15)
my_restaurant.increment_number_served(25)
my_restaurant.number_of_customers()
