import time
from turtle import Turtle, Screen
from player import Player
from cars import Car
from text import Scoreboard, GameOver

CARS = ["car1", "car2", "car3", "car4", "car5", "car6", "car7", "car8", "car9", "car10", "car11", "car12", "car13", "car14"]

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
car_manager = Car()
game_on = True

while game_on:
    scoreboard.write(f"Score: {score}", font=("Arial", 24, "bold"))
    car_manager.create_car()
    car_manager.car_move()
    screen.update()
    time.sleep(0.1)
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_on = False
            gm = GameOver()
    if player.ycor() > 280:
        scoreboard.clear()
        player.player_reset()
        score += 1
        car_manager.car_speedup()


screen.exitonclick()
