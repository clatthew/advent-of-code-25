from pytest import mark, fixture
from src.day_01 import get_input
from src.day_09 import prepare_input, get_rectangle_area, find_biggest_rectangle


@fixture
def day_09_input():
    return prepare_input(get_input("input/day_09.txt"))


@fixture
def test_input():
    return [
        [7, 1],
        [11, 1],
        [11, 7],
        [9, 7],
        [9, 5],
        [2, 5],
        [2, 3],
        [7, 3],
    ]


class Testprepare_input:
    @mark.it("splits into list of ints")
    def test_1(self):
        input_data = ["97579,50266", "97579,51480", "97846,51480"]
        expected = [[97579, 50266], [97579, 51480], [97846, 51480]]
        assert prepare_input(input_data) == expected


class Testget_rectangle_area:
    @mark.it("rectangle with one side of length 1")
    def test_1(self):
        corner_1 = [555, 565]
        corner_2 = [555, 575]
        expected = 11
        result = get_rectangle_area(corner_1, corner_2)
        assert result == expected

    @mark.it("bigger rectangle")
    def test_2(self):
        corner_1 = [7, 1]
        corner_2 = [11, 7]
        expected = 35
        result = get_rectangle_area(corner_1, corner_2)
        assert result == expected


class Testfind_biggest_rectangle:
    @mark.it("test input")
    def test_1(self, test_input):
        expected = 50
        result = find_biggest_rectangle(test_input)
        assert result == expected

    @mark.it("day 9 input")
    def test_2(self, day_09_input):
        expected = 4737096935
        result = find_biggest_rectangle(day_09_input)
        assert result == expected
