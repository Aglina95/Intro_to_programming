# Write your code here :-)
class Cat:
    def __init__(self, name, color, sound="Miau!"):
        self.name = name
        self.color = color
        self.sound = sound

    def make_sound(self):
        return self.sound

    def caress(self):
        return self.make_sound()


garfield = Cat("garfield", "orange")
grumpy = Cat("grumpy", "black-and-white", "Grrrm!")

print(garfield.caress())
print(grumpy.caress())
print(garfield.color)
print(grumpy.color)
