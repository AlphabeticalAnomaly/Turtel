import pytest

from player import Player


class TestPlayer:

    def setup_method(self):
        self.test_player = Player()

    def test_player_start_pos(self):
        assert self.test_player.xcor() == 0 and self.test_player.ycor() == -280, "Player did not start in the specified starting position"

    def test_player_move_up(self):
        expected_pos = self.test_player.ycor() + 10
        self.test_player.turtle_move_up()
        actual_pos = self.test_player.ycor()
        assert expected_pos == actual_pos, "Player did not move 10 units up"

    def test_player_move_down(self):
        expected_pos = self.test_player.ycor() - 10
        self.test_player.turtle_move_down()
        actual_pos = self.test_player.ycor()
        assert expected_pos == actual_pos, "Player did not move 10 units down"

    def test_player_reset_pos(self):
        assert self.test_player.player_reset() == -280, "Player did not go to the specified starting position"

    def test_player_shape(self):
        assert self.test_player.shape() == "turtle", "Player shape is incorrect"

    def test_player_color(self):
        assert self.test_player.color() == ('green', 'green'), "Player color is incorrect"

    def test_player_heading(self):
        assert self.test_player.heading() == 90, "Player heading is incorrect"

    def test_player_penup(self):
        assert self.test_player.isdown() == False, "Turtle pen currently on"

