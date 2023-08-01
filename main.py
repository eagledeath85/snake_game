from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn animation off
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


### CONTROLING THE SNAKE ###
# Listening to the keys tapped
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


is_game_on = True
# Move the segments forward
while is_game_on:
    # Update the screen before all the segments moved. This way, it'll appear as a snake moving
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    scoreboard.update_scoreboard()

    # Detect collision with food by checking the distance that separates head of snake and food
    if snake.head_of_snake.distance(food) < 15:
        food.refresh_food_location()
        snake.extend_snake()
        scoreboard.increase_score()


    # Detect collision with wall
    if snake.head_of_snake.xcor() > 290 or snake.head_of_snake.xcor() < -290 or snake.head_of_snake.ycor() > 290 or snake.head_of_snake.ycor() < -290:
        scoreboard.reset()
        snake.reset()


    # Detect collision with tail
    # if head collides with any segment in the tail, then trigger game over
    # head _of_snake segment should be ignored from the check
    for segment in snake.segments[1:]:
        if snake.head_of_snake.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()