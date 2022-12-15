# Write your code here :-)
from turtle import Turtle

class MyTurtle(Turtle):
    def draw_triangle(self, edge_length):
        for _ in range(3):
            self.forward(edge_length)
            self.left(120)


    def draw_square(self, edge_length):
        for _ in range(4):
            self.forward(edge_length)
            self.left(90)


a_turtle = MyTurtle()

a_turtle.draw_triangle(100)
a_turtle.draw_square(200)
