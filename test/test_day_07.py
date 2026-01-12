from pytest import mark, fixture
from src.day_01 import get_input
from src.day_07 import split_row, analyse_manifold


@fixture
def test_input():
    return [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]


@fixture
def day_07_input():
    return get_input("input/day_07.txt")


class Testsplit_row:
    @mark.it("beams stay in same place when there are no splitters")
    def test_1(self):
        input_row = "..............."
        input_beams = [1, 3, 4]
        expected = [1, 3, 4]
        assert split_row(input_row, input_beams)[0] == expected

    @mark.it("beams split by splitters")
    def test_2(self):
        input_row = ".....^.^.^....."
        input_beams = [1, 3, 5, 9]
        expected = [1, 3, 4, 6, 8, 10]
        assert split_row(input_row, input_beams)[0] == expected

    @mark.it("no duplicate beams")
    def test_3(self):
        input_row = ".....^.^.^....."
        input_beams = [1, 3, 5, 7]
        expected = [1, 3, 4, 6, 8]
        assert split_row(input_row, input_beams)[0] == expected

    @mark.it("no beams off side of grid")
    def test_4(self):
        input_row = "^....^.^.^....^"
        input_beams = [0, 3, 5, 7, 14]
        expected = [1, 3, 4, 6, 8, 13]
        assert split_row(input_row, input_beams)[0] == expected


class Testanalyse_manifold:
    @mark.it("part 1 with the test input")
    def test_1(self, test_input):
        expected = 21
        assert analyse_manifold(test_input) == expected

    @mark.it("part 1 with the day 7 input")
    def test_2(self, day_07_input):
        expected = 1585
        assert analyse_manifold(day_07_input) == expected
