from pytest import mark, fixture
from src.day_01 import get_input
from src.day_09 import (
    prepare_input,
    get_rectangle_area,
    find_biggest_rectangle,
    get_furthest_corner,
    get_blank_floor_map,
    fill_between,
    produce_outline,
    fill_shape,
)

from pprint import pprint


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


class Testget_furthest_corner:
    @mark.it("gets furthest corner of test data")
    def test_1(self, test_input):
        expected = [11, 7]
        result = get_furthest_corner(test_input)
        assert result == expected

    @mark.it("gets furthest corner when biggest x and y are in different corners")
    def test_2(self):
        test_data = [[11, 3], [4, 7]]
        expected = [11, 7]
        result = get_furthest_corner(test_data)
        assert result == expected


class Testget_blank_floor_map:
    @mark.it("produces correct blank floor map for test data")
    def test_1(self, test_input):
        result = get_blank_floor_map(get_furthest_corner(test_input), "!")
        assert len(result) == 8
        assert len(result[0]) == 12
        assert len(result[-1]) == 12
        assert result[5][6] == "!"


@mark.skip
class Testfill_between:
    @mark.it("makes outline between two points, forward, horizontal")
    def test_1(self):
        corner_0 = [5, 3]
        corner_1 = [5, 7]
        floor_map = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "#"],
        ]
        expected = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", "X", "X", "X", "#"],
        ]
        floor_map[corner_0[0]][corner_0[1]] = "#"
        result = fill_between(floor_map, corner_0, corner_1)
        assert result == expected

    @mark.it("makes outline between two points, backward, horizontal")
    def test_2(self):
        corner_0 = [5, 3]
        corner_1 = [5, 7]
        floor_map = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "#"],
        ]
        expected = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", "X", "X", "X", "#"],
        ]
        floor_map[corner_0[0]][corner_0[1]] = "#"
        result = fill_between(floor_map, corner_1, corner_0)
        assert result == expected

    @mark.it("makes outline between two points, upward")
    def test_3(self):
        corner_0 = [5, 3]
        corner_1 = [1, 3]
        floor_map = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "."],
        ]
        expected = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", "X", ".", ".", ".", "."],
            [".", ".", ".", "X", ".", ".", ".", "."],
            [".", ".", ".", "X", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "."],
        ]
        floor_map[corner_0[0]][corner_0[1]] = "#"
        result = fill_between(floor_map, corner_0, corner_1)
        assert result == expected

    @mark.it("makes outline between two points, downward")
    def test_4(self):
        corner_0 = [0, 6]
        corner_1 = [4, 6]
        floor_map = [
            [".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected = [
            [".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", "X", "."],
            [".", ".", ".", ".", ".", ".", "X", "."],
            [".", ".", ".", ".", ".", ".", "X", "."],
            [".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        floor_map[corner_0[0]][corner_0[1]] = "#"
        result = fill_between(floor_map, corner_0, corner_1)
        assert result == expected


class Testproduce_outline:
    @mark.it("produces correct outline for test data")
    def test_1(self, test_input):
        expected = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "X", "X", "X", "#"],
            [".", ".", ".", ".", ".", ".", ".", "X", ".", ".", ".", "X"],
            [".", ".", "#", "X", "X", "X", "X", "#", ".", ".", ".", "X"],
            [".", ".", "X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
            [".", ".", "#", "X", "X", "X", "X", "X", "X", "#", ".", "X"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "X", ".", "X"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "X", "#"],
        ]
        result = produce_outline(test_input)
        pprint(result)
        assert result == expected


class Testfill_shape:
    @mark.it("square")
    def test_1(self):
        floor_map = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", "X", "X", "#", "."],
            [".", ".", ".", "X", ".", ".", "X", "."],
            [".", ".", ".", "X", ".", ".", "X", "."],
            [".", ".", ".", "X", ".", ".", "X", "."],
            [".", ".", ".", "#", "X", "X", "#", "."],
        ]
        expected = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", "X", "X", "#", "."],
            [".", ".", ".", "X", "X", "X", "X", "."],
            [".", ".", ".", "X", "X", "X", "X", "."],
            [".", ".", ".", "X", "X", "X", "X", "."],
            [".", ".", ".", "#", "X", "X", "#", "."],
        ]
        assert fill_shape(floor_map) == expected

    @mark.it("shape with two fill regions on the same row")
    def test_2(self):
        floor_map = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["#", "X", "#", ".", "#", "X", "#", "."],
            ["X", ".", "X", ".", "X", ".", "X", "."],
            ["X", ".", "#", "X", "#", ".", "X", "."],
            ["X", ".", ".", ".", ".", ".", "X", "."],
            ["#", "X", "X", "X", "X", "X", "#", "."],
        ]
        expected = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["#", "X", "#", ".", "#", "X", "#", "."],
            ["X", "X", "X", ".", "X", "X", "X", "."],
            ["X", "X", "#", "X", "#", "X", "X", "."],
            ["X", "X", "X", "X", "X", "X", "X", "."],
            ["#", "X", "X", "X", "X", "X", "#", "."],
        ]
        result = fill_shape(floor_map)
        pprint(result)
        assert result == expected

    @mark.it("fills the test data")
    def test_3(self, test_input):
        expected = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "X", "X", "X", "#"],
            [".", ".", ".", ".", ".", ".", ".", "X", "X", "X", "X", "X"],
            [".", ".", "#", "X", "X", "X", "X", "#", "X", "X", "X", "X"],
            [".", ".", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            [".", ".", "#", "X", "X", "X", "X", "X", "X", "#", "X", "X"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "X", "X", "X"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "X", "#"],
        ]
        result = fill_shape(produce_outline(test_input))
        pprint(result)
        assert result == expected
