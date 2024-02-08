from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Models the initial scoreboard body."""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard at each point."""
        self.clear()
        self.goto(-220, 255)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def point(self):
        """Updates the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Shows 'GAME OVER' when turtle is crashed."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
