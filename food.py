from turtle import Turtle
import random
Limit = 228


class SnakeFood(Turtle):
    def __init__(self):
        super().__init__()
        self.position = []
        self.commence_food()

    def commence_food(self):
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.up
        self.reposition()

    def reposition(self):
        self.setx(self.random_cordinate())
        self.sety(self.random_cordinate())

    def random_cordinate(self):
        return random.randint(-Limit, Limit)

