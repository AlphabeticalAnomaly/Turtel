
from turtle import Turtle
import random


CAR_SPEED = 5
CAR_SPEED_INCREMENT = 20
CAR_COLORS = ["green", "gold", "yellow", "red", "black", "brown", "orange", "blue"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = CAR_SPEED

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 4:
            new_car = Turtle()
            new_car.penup()
            new_car.speed("fastest")
            new_car.color(random.choice(CAR_COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=random.randrange(300, 360, 20), y=random.randrange(-200, 270, 20))
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def car_speedup(self):
        self.speed += CAR_SPEED_INCREMENT


