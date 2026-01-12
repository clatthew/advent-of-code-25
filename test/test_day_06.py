from src.day_01 import get_input
from src.day_06 import prepare_input, solve_worksheet, prepare_input_2
from pytest import mark, fixture


@fixture
def day_06_input():
    return prepare_input(get_input("input/day_06.txt"))


@fixture
def day_06_input_2():
    return prepare_input_2(get_input("input/day_06.txt"), 4)


@fixture
def test_input():
    return prepare_input(
        [
            "123 328  51 64",
            "45 64  387 23 ",
            "6 98  215 314",
            "*   +   *   + ",
        ]
    )


@fixture
def test_input_2():
    return prepare_input_2(
        [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]
    )


class Testprepare_input:
    @mark.it("test worksheet")
    def test_1(self, test_input):
        expected = [
            [123, 45, 6, "*"],
            [328, 64, 98, "+"],
            [51, 387, 215, "*"],
            [64, 23, 314, "+"],
        ]
        assert test_input == expected


class Testpart_1:
    @mark.it("test input")
    def test_1(self, test_input):
        expected = 4277556
        assert solve_worksheet(test_input) == expected

    @mark.it("day 6 input")
    def test_2(self, day_06_input):
        expected = 4805473544166
        assert solve_worksheet(day_06_input) == expected


class Testprepare_input_2:
    @mark.it("produces problems in alternative format")
    def test_1(test_input_2):
        expected = [
            [1, 24, 356, "*  "],
            [369, 248, 8, "+  "],
            [32, 581, 175, "*  "],
            [623, 431, 4, "+  "],
        ]
        test_input = [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]
        assert prepare_input_2(test_input) == expected


class Testpart_2:
    @mark.it("test data")
    def test_1(self, test_input_2):
        expected = 3263827
        assert solve_worksheet(test_input_2) == expected

    @mark.it("input data")
    def test_2(self, day_06_input_2):
        expected = 8907730960817
        assert solve_worksheet(day_06_input_2) == expected
