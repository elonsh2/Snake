from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg='GAME OVER', align=ALIGNMENT, font=("Courier", 20, "bold"))
