import pytest

from player import Player

test_player = Player()


def test_start_pos():

    assert test_player.xcor() == 0 and test_player.ycor() == -280


def test_player_move_up():
    assert test_player.turtle_move_up() == test_player.forward(10)


def test_player_move_down():
    assert test_player.turtle_move_down() == test_player.backward(10)


def test_player_reset_pos():
    assert test_player.player_reset() == test_player.goto(0, -280)


def test_player_color():
    assert test_player.color() == ('green', 'green')


def test_player_shape():
    assert test_player.shape() == "turtle"


def test_player_heading():
    assert test_player.heading() == 90


# class PlayerTest:
#
#     def test_player(self):
#         self.test_player = Player()
#
#     def test_player_start_pos(self):
#         assert self.test_player.xcor() == 0
#         assert self.test_player.ycor() == -280
#
#     def test_player_move_up(self):
#         assert self.test_player.turtle_move_up() == self.test_player.forward(10)
#
#     def test_player_move_down(self):
#         assert self.test_player.turtle_move_down() == self.test_player.backward(10)
#
#     def test_player_reset_pos(self):
#         assert self.test_player.player_reset() == self.test_player.goto(0, -280)
#
#     def test_player_shape(self):
#         assert self.test_player.shape() == "turtle"
#
#     def test_player_color(self):
#         assert self.test_player.color() == ('green', 'green')
#
#     def test_player_heading(self):
#         assert self.test_player.heading() == 90
