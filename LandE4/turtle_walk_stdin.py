# Write your code here :-)
import sys
from random import randint
from turtle import forward, left
import time


for line in sys.stdin:
    argument = line.rstrip()

    turtle_steps = int(argument)
    forward(turtle_steps)
    # take an int argument for turtle_steps
    #move forward accordingly(given the turtle steps the user gave you)


    random_angle = randint(45, 135)
    left(random_angle)
    #select a random number between 45 and 135
    #rotate left based on the given random number

time.sleep(5)

