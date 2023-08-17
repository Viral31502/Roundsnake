from turtle import Turtle
Start_pos = [0, -10, -20]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


def newparts():
    new_part = Turtle(shape="circle")
    new_part.color("yellow")
    new_part.penup()
    new_part.shapesize(stretch_wid=0.5, stretch_len=0.5)
    return new_part


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.moving = True
        self.move()

    def create_snake(self):
        for i in range(0,3):
            new_part = newparts()
            new_part.setx(Start_pos[i])
            self.body.append(new_part)

    def move(self):
        if self.moving:
            for i in range (len(self.body) - 1, 0, -1):
                new_x = self.body[i-1].xcor()
                new_y = self.body[i - 1].ycor()
                self.body[i].setpos(new_x, new_y)
            self.head.forward(10)

    def grow(self):
        new_part = newparts()
        new_x = self.body[len(self.body) -1].xcor()
        new_x = int(new_x -10)
        new_y = self.body[len(self.body) -1].ycor()
        new_part.goto(new_x, new_y)
        self.body.append(new_part)

    def upward(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def downward(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
     if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)

    def bite(self):
        for i in self.body:
            if i != self.head:
                if self.head.distance(i) < 8:
                    return True