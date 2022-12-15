# Write your code here :-)
class Jar:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cookies = 0

    def describe(self):
        return self.cookies * "🍪"

    def deposit(self, n):
        if self.cookies + n > self.capacity:
            self.cookies = self.capacity
            print("There was not enough space for the cookies in the jar!")
        else:
            self.cookies += n

    def withdraw(self, n):
        if self.cookies - n < 0:
            self.cookies = 0
            print("There were not enough cookies in the jar!")
        else:
            self.cookies -= n

    def get_capacity(self):
        return self.capacity

    def get_size(self):
        return self.cookies

jar = Jar(10)
assert jar.get_capacity() == 10
jar.deposit(10)
jar.withdraw(5)
assert jar.get_size() == 5
jar.withdraw(6)
assert jar.get_size() == 0
jar.deposit(20)
assert jar.get_size() == 10
assert jar.describe() == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
