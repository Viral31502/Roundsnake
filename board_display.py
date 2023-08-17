from turtle import Turtle

with open("score.txt", "r") as doc:
    high_score = int(doc.read())


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("SkyBlue")
        self.goto(-50, 280)
        self.score = -1
        self.update_text()

    def update_text(self):
        self.score_updater()
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 12, "normal"))

    def score_updater(self):
        self.score += 1

    def game_over(self):
        self.color("White")
        self.goto(0, 50)
        self.write(f"Game Over", align="center", font=("Ariel", 48, "normal"))
        self.goto(0, 0)
        self.write(f"High Score: {high_score}   Your score: {self.score}", align="center", font=("Ariel", 24, "normal"))
        if self.score > high_score:
            with open("score.txt", "w") as doc1:
                doc1.write(str(self.score))
                self.color("Blue")
            self.goto(0, -150)
            self.write(f"New high Score\n {self.score}!", align="center",
                       font=("Ariel", 48, "normal"))
