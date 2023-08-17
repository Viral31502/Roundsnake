from turtle import Screen
from turtle import Turtle
import time
from board_display import Board
from snake import Snake
from food import SnakeFood



def area():
    blue_screen = Turtle(shape="square")
    blue_screen.color("green")
    blue_screen.shapesize(stretch_wid=28, stretch_len=28)



game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("blue")
area()
game_screen.tracer(0)
player_food = SnakeFood()
player_snake = Snake()
game_screen.listen()

game_screen.onkey(player_snake.upward, "Up")
game_screen.onkey(player_snake.downward, "Down")
game_screen.onkey(player_snake.left, "Left")
game_screen.onkey(player_snake.right, "Right")

score_board = Board()
game_running = True

while game_running:
    game_screen.update()
    time.sleep(0.1)
    player_snake.move()

    if player_snake.head.distance(player_food) < 10:
        player_food.reposition()
        player_snake.grow()
        score_board.update_text()
    if player_snake.bite():
        game_running = False
    if player_snake.head.xcor() == 280 or player_snake.head.xcor() == -280:
        game_running = False
    if player_snake.head.ycor() == 280 or player_snake.head.ycor() == -280:
        game_running = False


score_board.game_over()
game_screen.exitonclick()

