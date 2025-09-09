from turtle import Screen
import time, sys
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game v1.0")
screen.tracer(0)

snake = Snake()

screen.listen()
def init_keys():
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.extend, "space")
    screen.onkey(quit_game, "Escape")
    
    
init_keys()


game_is_on = True

def quit_game():
    global game_is_on
    game_is_on = False
    sys.exit()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

screen.exitonclick()