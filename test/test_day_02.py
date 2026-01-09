from src.day_01 import get_input
from src.day_02 import get_invalid_total_1, get_invalid_total_2
from pytest import mark, fixture


@fixture
def day_02_input():
    return get_input("input/day_02.txt")[0].split(",")


class TestPart1:
    @mark.it(
        "gets the correct answer for range containing single two-digit invalid value"
    )
    def test_1(self):
        assert get_invalid_total_1(["22-22"]) == 22

    @mark.it(
        "gets the correct answer for range containing single six-digit invalid value"
    )
    def test_2(self):
        assert get_invalid_total_1(["335334-335336"]) == 335335

    @mark.it("gets the correct answer for all examples")
    def test_3(self):
        assert get_invalid_total_1(["11-22"]) == 33
        assert get_invalid_total_1(["95-115"]) == 99
        assert get_invalid_total_1(["1188511880-1188511890"]) == 1188511885
        assert get_invalid_total_1(["222220-222224"]) == 222222
        assert get_invalid_total_1(["1698522-1698528"]) == 0
        assert get_invalid_total_1(["446443-446449"]) == 446446
        assert get_invalid_total_1(["38593856-38593862"]) == 38593859

    @mark.it("gets the correct answer for puzzle input")
    def test_99(self, day_02_input):
        assert get_invalid_total_1(day_02_input) == 18_700_015_741


class TestPart2:
    @mark.skip
    @mark.it("gets the correct answer for all examples")
    def test_1(self):
        assert get_invalid_total_2(["11-22"]) == 33
        assert get_invalid_total_2(["95-115"]) == 99 + 111
        assert get_invalid_total_2(["998-1012"]) == 999 + 1010
        assert get_invalid_total_2(["1188511880-1188511890"]) == 1188511885
        assert get_invalid_total_2(["222220-222224"]) == 222222
        assert get_invalid_total_2(["1698522-1698528"]) == 0
        assert get_invalid_total_2(["446443-446449"]) == 446446
        assert get_invalid_total_2(["38593856-38593862"]) == 38593859
        assert get_invalid_total_2(["565653-565659"]) == 565656
        assert get_invalid_total_2(["824824821-824824827"]) == 824824824
        assert get_invalid_total_2(["2121212118-2121212124"]) == 2121212121

    @mark.skip
    @mark.it("gets the correct answer for an example")
    def test_2(self):
        assert get_invalid_total_2(["4050-4876"]) == 35956

    @mark.skip
    @mark.it("gets the correct answer for reversed range")
    def test_3(self):
        assert get_invalid_total_2(["373-300"]) == 0

    @mark.skip
    @mark.it("gets the correct answer for range containing single invalid")
    def test_4(self):
        assert get_invalid_total_2(["3434-3434"]) == 3434

    @mark.it("gets the correct answer for an example")
    def test_5(self):
        assert get_invalid_total_2(["908922-976419"]) == 69752865

    # @mark.skip
    @mark.it("gets the correct answer for input data")
    def test_99(self, day_02_input):
        assert get_invalid_total_2(day_02_input) == 20_077_273_032
