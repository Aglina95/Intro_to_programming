# Write your code here :-)
import sys
from random import randint
from turtle import forward, left


for idx, argument in enumerate(sys.argv):
    if idx == 0:
        # In case of the first argument -the Python program name- do nothing in
        # this iteration, jump over it with `continue`
        continue

    turtle_steps = int(argument)
    forward(turtle_steps)
    # take an int argument for turtle_steps
    #move forward accordingly(given the turtle steps the user gave you)


    random_angle = randint(45, 135)
    left(random_angle)
    #select a random number between 45 and 135
    #rotate left based on the given random number


vf = input() #story an empty input into a random variable to make your porgram stop

# this program ignores first argument(name of the program)
#and then takes int inputs as steps to move forward and a random angle between 45 and 135(degrees) to rotate left.
#(takes as many arguments as the user gives i.e 10 3 10 or more/less)

#for each argument, if index is zero(i.e if it's the first argument) then ignore it(continue), else convert the argument into an integer which will be the turtle steps, move forward according to the given turtle steps,
#take a random angle from 45 to 135 and rotate left according to that angle.

