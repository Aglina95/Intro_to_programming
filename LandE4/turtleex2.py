# Write your code here :-)
from turtle import forward, left, right, speed


speed("fastest")

edge_length = 200
count = 0
while count < 36:
    for idx in range(3):
        if count % 4 == 0:
            edge_length = 100
        else:
            edge_length = 200
        forward(edge_length)
        left(120)

    right(20)
    count += 1
