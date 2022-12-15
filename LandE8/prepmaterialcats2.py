class Cat:
    def __init__(self, name="", color="grey", sound="Miau!"):
        self.name = name
        self.color = color
        self.sound = sound

    def make_sound(self):
        return self.sound

    def caress(self):
        return self.make_sound()

class Fox:
    def make_sound(self):
        return "RIKA DING-DING-DING"

class Cow:
    def make_sound(self):
        return "Moooo"


a_cat = Cat()
a_fox = Fox()
a_cow = Cow()
another_cow = Cow()

animals = [a_cat, a_fox, a_cow, another_cow]
for animal in animals:
    print(animal.make_sound())
