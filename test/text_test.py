import pytest
from text import Scoreboard, GameOver


class TestScoreboard:

    def setup_method(self):
        self.test_scoreboard = Scoreboard()

    def test_scoreboard_color(self):
        assert self.test_scoreboard.color() == ('black', 'black'), "The scoreboard does not have the correct color"

    def test_scoreboard_pos(self):
        assert self.test_scoreboard.xcor() == -260 and self.test_scoreboard.ycor() == 260, "Scoreboard is not placed correctly"

    def test_scoreboard_penup(self):
        assert self.test_scoreboard.isdown() == False, "Turtle pen currently on"

    def test_scoreboard_no_turtle(self):
        assert self.test_scoreboard.isvisible() == False, "Scoreboard turtle is still visible"


class TestGameOverText:

    def setup_method(self):
        self.game_over_text = GameOver()

    def test_game_over_text_color(self):
        assert self.game_over_text.color() == ('black', 'black'), "Incorrect text color used"

    def test_game_over_text_penup(self):
        assert self.game_over_text.isdown() == False, "Turtle pen currently on"

    def test_game_over_text_no_turtle(self):
        assert self.game_over_text.isvisible() == False, "Text turtle is still visible"

    def test_game_over_message(self):
        assert self.game_over_text.font == ("Arial", 20, "bold")
        assert self.game_over_text.text == "GAME OVER"
        assert self.game_over_text.align == "center"





