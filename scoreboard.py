from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1, clear the precedent score and write the updated one on the screen"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Write the new score on the screen"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays Game Over message"""
        self.goto(x=0, y=0)
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)
