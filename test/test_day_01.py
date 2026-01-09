from src.day_01 import get_input, get_number_of_zeroes
from pytest import mark, fixture


@fixture
def day_01_input():
    return get_input("input/day_01.txt")


class Testget_input:
    @mark.it("returns a list")
    def test_1(self, day_01_input):
        assert isinstance(day_01_input, list)

    @mark.it("returns an object with correct first element")
    def test_2(self, day_01_input):
        assert day_01_input[0] == "R46"

    @mark.it("returns an object with correct number of elements")
    def test_3(self, day_01_input):
        assert len(day_01_input) == 4510


class TestPart_1:
    @mark.it("returns 0 if no instructions given and start pos is not zero")
    def test_1(self):
        assert get_number_of_zeroes(50, []) == 0

    @mark.it("returns 1 if no instructions given and start pos is zero")
    def test_2(self):
        assert get_number_of_zeroes(0, []) == 1

    @mark.it("returns correct answer for simple set of instructions")
    def test_3(self):
        assert get_number_of_zeroes(50, ["R50", "R24", "L24", "L1"]) == 2

    @mark.it("returns correct answer for input")
    def test_99(self, day_01_input):
        assert get_number_of_zeroes(50, day_01_input) == 1084


class TestPart_2:
    @mark.it("returns correct answer for simple set of instructions (positive)")
    def test_1(self):
        assert get_number_of_zeroes(50, ["R75", "L25", "L80"], True) == 2

    @mark.it("returns correct answer for simple set of instructions (negative)")
    def test_2(self):
        assert get_number_of_zeroes(50, ["L75", "R20", "R10"], True) == 2

    # @mark.skip
    @mark.it("returns correct answer for input")
    def test_99(self, day_01_input):
        assert get_number_of_zeroes(50, day_01_input, every_zero=True) == 6475
