# Write your code here :-)
from turtle  import forward, pencolor

pencolor = "purple"

speed("fastest")

edge_length = 200
angle = 10
total_angle = 0
circle_iteration = 0

while circle_iteration < 3:
    for idx in range(4):
        forward(edge_length)
        left(90)

    left(angle)
    edge_length = 0.97 * edge_length

    total_angle += angle
    if total_angle % 360 == 0:
        circle_iteration += 1
