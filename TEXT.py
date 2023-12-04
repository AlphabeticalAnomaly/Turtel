from turtle import  Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

        self.goto(-260, 260)


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
