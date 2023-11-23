import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Level
        self.penup()
        self.setposition(x=-280, y=255)
        self.hideturtle()
        self.update_scoreboard()

    # Level display
    def update_scoreboard(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    # Update the score
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
