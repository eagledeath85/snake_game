from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1, clear the precedent score and write the updated one on the screen"""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Write the new score on the screen"""
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        """Update the high_score value with the last highest score obtained"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Displays Game Over message"""
    #     self.goto(x=0, y=0)
    #     self.write(f"Game Over.", align=ALIGNMENT, font=FONT)

    def get_high_score(self):
        with open("score_data.txt", mode='r', encoding='utf-8', newline='') as score_file:
            self.high_score = score_file.read()
        return int(self.high_score)

    def write_high_score(self):
        with open("score_data.txt", mode='w', encoding='utf-8', newline='') as score_file:
            score_file.write(str(self.high_score))
