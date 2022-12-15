animals = ["chicks", "ducks", "turkeys", "pigs", "cows", "donkeys"]

sounds = ["chick", "quack", "gobble", "oink", "moo", "hee", "h"]

def start():
    print("Old MacDonald had a farm, ", end='')
    ee()

def ee():
    print("Ee-igh, Ee-igh, oh!")

def onthis(x):
    start()
    print("And on this farm he had some " + x + ". ", end = '')
    ee()
    print("With a ", end="")

def first_sound_line(x, y):
    print(x, y, "here and a", x, y, "there;")

def other_sound_line(x, y):
    print(x, "here a ", y, sep = "",)

def make_sounds(x, y):
    first_sound_line(x, y)
    other_sound_line('', x)
    other_sound_line('t', y)
    other_sound_line('everyw', (y + " ") * 3)

for i in range(len(animals)):
    onthis("donkeys")
    make_sounds("hee", "haw")
    print() # new line at the end of each verse
