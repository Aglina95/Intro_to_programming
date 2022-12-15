# Write your code here :-)
import sys
from turtle import forward, left, color
import time

#color("orange")

turn_walk = ""

for line in sys.stdin:
    argument = line.rstrip()

    if argument == "Walk":
        turn_walk = argument

    elif argument == "Turn":
        turn_walk = argument
    elif argument == "Color":
        turn_walk = argument
    else:
        print(turn_walk)
        if turn_walk == "Walk":
            forward(int(argument))
        elif turn_walk == "Color":
            color(argument)
        else:
            left(int(argument))

#steps_forward = forward(100)
#turn_left = left(90)
#new_steps_forward = forward(50)

#print(steps)

