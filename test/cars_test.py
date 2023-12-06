import pytest
from cars import Car, CarManager, CAR_COLORS
from player import Player


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
        expected_pos = self.test_car.xcor() - self.test_car.speed
        self.test_car.car_move()
        actual_pos = self.test_car.xcor()
        assert actual_pos == expected_pos, "Car did not move in the intended direction or at the specified speed"

    def test_car_speed_up_function(self):
        result = self.test_car.car_speedup()
        assert result == 25, "Car acceleration does not match the increment"


class TestCarManager:

    def setup_method(self):
        self.car_manager = CarManager()

    def test_car_manager_car_creation(self):
        expected_value = 30
        self.car_manager.create_cars(0)
        actual_value = len(self.car_manager.car_list)
        assert expected_value == actual_value, "Car manager did not spawn the proper number of cars"

    def test_car_collision(self):
        test_player = Player()
        self.car_manager.create_cars()
        test_car = self.car_manager.car_list[1]
        test_player.goto(test_car.xcor(), test_car.ycor())
        expected_result = self.car_manager.check_collision(test_player)
        assert expected_result == True, "Player collision is not detected or the distance collision trigger has been modified from the default value"
