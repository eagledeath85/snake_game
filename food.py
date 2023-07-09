from turtle import Turtle
import random


class Food(Turtle):
    """Class that inherits from Turtle class."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # divide the default size by 2
        self.color("red")
        self.speed("fastest")
        self.refresh_food_location()

    def refresh_food_location(self):
        """Calculates a new random location on the screen and set the food to go to this location"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
