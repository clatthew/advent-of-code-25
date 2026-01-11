from src.day_04 import (
    prepare_input,
    adjacent_rolls,
    count_accessible_rolls,
    accessible_roll_locations,
    repeated_removals,
    count_possible_removals,
)
from src.day_01 import get_input
from pytest import mark, fixture


@fixture
def day_04_input():
    return prepare_input(get_input("input/day_04.txt"))


@fixture
def test_input():
    return prepare_input(
        [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
    )


class Testinput:
    @mark.it("converts simple sample input into 2d list")
    def test_1(self):
        test_input = ["..@@.@@@@.", "@@@.@.@.@@", "@@@@@.@.@@", "@.@@@@..@."]
        expected = [
            [".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
            ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
            ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
            ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
        ]
        assert prepare_input(test_input) == expected


class Testadjacent_rolls:
    @mark.it("return number of adjacent rolls for a roll not near the edge of the grid")
    def test_1(self, test_input):
        input_data = {"roll_grid": test_input, "row": 2, "col": 6}
        expected = 2
        assert adjacent_rolls(**input_data) == expected

    @mark.it("return number of adjacent rolls for left edge of the grid")
    def test_2(self, test_input):
        input_data = {"roll_grid": test_input, "row": 4, "col": 0}
        expected = 3
        assert adjacent_rolls(**input_data) == expected

    @mark.it("return number of adjacent rolls for right edge of the grid")
    def test_3(self, test_input):
        input_data = {"roll_grid": test_input, "row": 1, "col": 9}
        expected = 4
        assert adjacent_rolls(**input_data) == expected

    @mark.it("return number of adjacent rolls for top edge of the grid")
    def test_4(self, test_input):
        input_data = {"roll_grid": test_input, "row": 0, "col": 6}
        expected = 3
        assert adjacent_rolls(**input_data) == expected

    @mark.it("return number of adjacent rolls for bottom edge of the grid")
    def test_5(self, test_input):
        input_data = {"roll_grid": test_input, "row": 9, "col": 5}
        expected = 5
        assert adjacent_rolls(**input_data) == expected

    @mark.it("return number of adjacent rolls for corners of grid")
    def test_6(self, test_input):
        input_data = {"roll_grid": test_input, "row": 0, "col": 0}
        expected = 2
        assert adjacent_rolls(**input_data) == expected
        input_data = {"roll_grid": test_input, "row": 0, "col": 9}
        expected = 3
        assert adjacent_rolls(**input_data) == expected
        input_data = {"roll_grid": test_input, "row": 9, "col": 0}
        expected = 1
        assert adjacent_rolls(**input_data) == expected
        input_data = {"roll_grid": test_input, "row": 9, "col": 9}
        expected = 2
        assert adjacent_rolls(**input_data) == expected


class Testadjacent_roll_locations:
    @mark.it("returns locations of accessible adjacent rolls")
    def test_1(self, test_input):
        expected = [
            [0, 2],
            [0, 3],
            [0, 5],
            [0, 6],
            [0, 8],
            [1, 0],
            [2, 6],
            [4, 0],
            [4, 9],
            [7, 0],
            [9, 0],
            [9, 2],
            [9, 8],
        ]
        assert accessible_roll_locations(test_input) == expected


class Testpart_1:
    @mark.it("returns correct number of accessible rolls for the test data")
    def test_1(self, test_input):
        expected = 13
        assert count_accessible_rolls(test_input) == expected

    @mark.it("returns correct number of accessible rolls for the day_4 input")
    def test_2(self, day_04_input):
        expected = 1578
        assert count_accessible_rolls(day_04_input) == expected


class Testrepeated_removals:
    @mark.it("correct resulting grid for the test input")
    def test_01(self, test_input):
        expected = [
            [".", ".", 1, 1, ".", 1, 1, 2, 1, "."],
            [1, 3, 4, ".", 2, ".", 2, ".", 3, 2],
            [2, 4, 5, 7, 8, ".", 1, ".", 3, 3],
            [2, ".", 6, 9, "@", "@", ".", ".", 2, "."],
            [1, 3, ".", "@", "@", "@", "@", ".", 2, 1],
            [".", 2, 4, "@", "@", "@", "@", "@", ".", 2],
            [".", 2, ".", "@", ".", "@", ".", "@", "@", 3],
            [1, ".", 4, "@", "@", ".", "@", "@", "@", 4],
            [".", 2, 3, "@", "@", "@", "@", "@", 5, "."],
            [1, ".", 1, ".", "@", "@", "@", ".", 1, "."],
        ]
        assert repeated_removals(test_input) == expected


class Testpart_2:
    @mark.it("correct number of removals for test input")
    def test_1(self, test_input):
        expected = 43
        assert count_possible_removals(test_input) == expected

    @mark.it("correct number of removals for day 4 input")
    def test_2(self, day_04_input):
        expected = 10132
        assert count_possible_removals(day_04_input) == expected
