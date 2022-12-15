# Write your code here :-)
from turtle import circle, right, speed

speed('fastest')

nr_half_circles = int(input("Give me an ODD num "))
radius = 10

tentatives = 1

while nr_half_circles % 2 == 0:
    nr_half_circles = int(input("Come " + tentatives * "o" + "n I said Odd "))
    tentatives = tentatives + 1


for i in range(nr_half_circles):
    if i % 2 == 0: #if the remainder in the division of i by 2 is...
        circle(radius, 180)
    else:
        circle(radius, -180)
    right(180)



right(180)
circle( radius * nr_half_circles,180)
