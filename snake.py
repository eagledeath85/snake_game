from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head_of_snake = self.segments[0]

    def create_snake(self):
        """Creates the snake with 3 squares"""
        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def move_snake(self):
        """Getting the snake to move. We'll use the following method to do this
        Last segment -> go to position of the second segment.
        Second segment -> go to position of the first segment.
        First segment -> go forward of 20 pix"""
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head_of_snake.forward(MOVING_DISTANCE)

    def add_segment(self, position):
        """Adds up a new segment to the current one"""
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        # Put the segments in a list
        self.segments.append(new_segment)

    def extend_snake(self):
        """Extend the end of the snake by calling add_segment method"""
        # Getting the position of segment at -1
        # Add a new segment to the end of the snake
        self.add_segment(self.segments[-1].position())

    def up(self):
        """Heads the snake up"""
        if self.head_of_snake.heading() != DOWN:
            self.head_of_snake.setheading(UP)

    def down(self):
        """Heads the snake down"""
        if self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)

    def left(self):
        """Heads the snake left"""
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)

    def right(self):
        """Heads the snake right"""
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)
