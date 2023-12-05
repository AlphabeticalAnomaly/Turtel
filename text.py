from turtle import Turtle

COLOR = "black"
ALIGN = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.align = ALIGN
        self.text = "GAME OVER"
        self.font = FONT
        self.write(arg=self.text, align=self.align, font=self.font)
