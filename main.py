import time
import random
from turtle import Turtle, Screen
from player import Player
from cars import CarManager
from text import Scoreboard, GameOver


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")
player = Player()
score = 0
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.turtle_move_up, "Up")
screen.onkey(player.turtle_move_down, "Down")
car_manager = CarManager()
car_manager.create_car()
game_on = True

while game_on:
    scoreboard.write(f"Score: {score}", font=("Arial", 24, "bold"))
    car_manager.move_cars()
    screen.update()
    time.sleep(0.1)
    for car in car_manager.car_list:
        if car.distance(player) < 30:
            game_on = False
            gm = GameOver()
        elif car.xcor() < -320:
            car.goto(x=random.randrange(300, 360, 20), y=random.randrange(-200, 270, 20))
    if player.ycor() > 280:
        scoreboard.clear()
        player.player_reset()
        score += 1
        car_manager.speedup_cars()


screen.exitonclick()
