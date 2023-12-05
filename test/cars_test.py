import pytest
from cars import Car, CAR_COLORS


class TestCar:

    def setup_method(self):
        self.test_car = Car()
        self.xcor = 0

    def test_car_speed(self):
        assert self.test_car.speed == 5, "Car speed does not match the specified one"

    def test_car_penup(self):
        assert self.test_car.isdown() == False, "Turtle pen currently on"

    def test_car_color(self):
        assert self.test_car.color()[0] in CAR_COLORS, "Car color is not present in the current colors options"

    def test_car_shape(self):
        assert self.test_car.shape() == "square", "Car does not have the correct shape"

    def test_car_start_pos(self):
        assert self.test_car.xcor() in range(-300, 360) and self.test_car.ycor() in range(-200, 270), "Car starting position is not in the correct range"

    def test_car_move_function(self):
        cur_pos = self.test_car.xcor()
        self.test_car.car_move()
        new_pos = self.test_car.xcor()
        assert cur_pos - new_pos == self.test_car.speed, "Car did not move in the intended direction or at the specified speed"

    def test_car_speed_up_function(self):
        result = self.test_car.car_speedup()
        assert result == 25, "Car acceleration does not match the increment"
