
from turtle import Turtle
import random


CAR_SPEED = 5
CAR_SPEED_INCREMENT = 20
CAR_COLORS = ["green", "gold", "yellow", "red", "black", "brown", "orange", "blue"]
CAR_COLLISION_TRIGGER = 30


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = CAR_SPEED
        self.color(random.choice(CAR_COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=random.randrange(-300, 360, 20), y=random.randrange(-200, 270, 20))
        self.speed_up = CAR_SPEED_INCREMENT

    def car_move(self):
        self.backward(self.speed)

    def car_speedup(self):
        self.speed += self.speed_up
        return self.speed


class CarManager(Car):
    def __init__(self):
        self.car_list = []

    def create_cars(self, test=0):
        if test == 0:
            for i in range(30):
                new_car = Car()
                self.car_list.append(new_car)
        elif test != 0:
            test_car = Car()
            test_car.goto(0, -280)
            self.car_list.append(test_car)
            print(type(test_car))

    def move_cars(self):
        for car in self.car_list:
            car.car_move()

    def speedup_cars(self):
        for car in self.car_list:
            car.car_speedup()

    def handle_traffic(self):
        for car in self.car_list:
            if car.xcor() < -320:
                car.goto(x=random.randrange(300, 360, 20), y=random.randrange(-200, 270, 20))

    def car_collision(self, player):
        for car in self.car_list:
            if car.distance(player) < CAR_COLLISION_TRIGGER:
                return True


