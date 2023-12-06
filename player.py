from turtle import Turtle

START_POS = (0, -280)
MOVE_SPEED = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto((START_POS))
        self.setheading(90)

    def turtle_move_up(self):
        self.forward(MOVE_SPEED)

    def turtle_move_down(self):
        self.backward(MOVE_SPEED)

    def player_reset(self):
        self.goto((START_POS))
        return self.ycor()


