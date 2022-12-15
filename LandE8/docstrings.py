# Write your code here :-)
from turtle import Turtle, forward, left


class SquareTurtle(Turtle):
    """A special kind of Turtle, which can do everything that a "normal" Turtle
    instance can do but possesses one new special method `draw_square`, which
    lets this turtle draw a square of given edge length.
    """

    def __init__(self, color_str="black"):
        """Constructor of all SquareTurtles.

        It will call the constructor of the Turtle super-class and subsequently
        will initialize this turtle's color, drawing color and set this turtle's
        shape from the default triangle to one resembling a real turtle seen
        from above.

        Args:
            color_str (string): A string containing the color that will become
                                the color of this turtle and everything that it
                                draws. Example values are "red", "green", and
                                "blue".
        """
        super().__init__()
        self.color(color_str)
        self.pen(pencolor=color_str)
        self.shape("turtle")

    def draw_square(self, edge_length):
        """Method that draws a square of given edge length, where the edges will
        be parallel to the container window boundaries.

        Args:
            edge_length (int): The length of each of the square's edges.
        """
        for _ in range(4):
            self.forward(edge_length)
            self.left(90)
