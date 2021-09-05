from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.add_score(0)

    def add_score(self, score):
        self.clear()
        self.write(arg=f'Score: {score}', align='center', font=("Arial", 14, "bold"))



