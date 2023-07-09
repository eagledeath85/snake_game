from turtle import Screen
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn animation off
screen.tracer(0)

snake = Snake()

screen.update()

is_game_on = True
# Move the segments forward
while is_game_on:
    # Update the screen before all the segments moved. This way, it'll appear as a snake moving
    screen.update()
    time.sleep(0.5)
    snake.move_snake()

### CONTROLING THE SNAKE ###
# Listening to the keys tapped
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.exitonclick()