from pytest import mark, fixture
from src.day_03 import get_joltage_of_bank, get_total_output
from src.day_01 import get_input


@fixture
def day_03_input():
    return get_input("input/day_03.txt")


class TestPart1:
    @mark.it("correct joltages of each bank in example data")
    def test_1(self):
        assert get_joltage_of_bank("987654321111111") == 98
        assert get_joltage_of_bank("811111111111119") == 89
        assert get_joltage_of_bank("234234234234278") == 78
        assert get_joltage_of_bank("818181911112111") == 92

    @mark.it("correct total joltage in example data")
    def test_2(self):
        assert (
            get_total_output(
                [
                    "987654321111111",
                    "811111111111119",
                    "234234234234278",
                    "818181911112111",
                ]
            )
        ) == 357

    @mark.it("correct total joltage in input data")
    def test_99(self, day_03_input):
        assert (get_total_output(day_03_input)) == 17524


class TestPart2:
    @mark.skip
    @mark.it("correct joltage for 3 batteries, consecutive")
    def test_1(self):
        assert get_joltage_of_bank("987654321111111", 3) == 987

    @mark.skip
    @mark.it("correct joltage for 3 batteries, non-consecutive")
    def test_2(self):
        assert get_joltage_of_bank("811111111111119", 3) == 819

    @mark.skip
    @mark.it("correct joltages of each bank in example data")
    def test_3(self):
        assert get_joltage_of_bank("987654321111111", 12) == 987654321111
        assert get_joltage_of_bank("811111111111119", 12) == 811111111119
        assert get_joltage_of_bank("234234234234278", 12) == 434234234278
        assert get_joltage_of_bank("818181911112111", 12) == 888911112111

    @mark.skip
    @mark.it("correct joltages for first piece of input data")
    def test_4(self):
        assert (
            get_joltage_of_bank(
                "2353224242223333222212222212122232212325242222323234222233222242242213332433221534222221224132232122",
                12,
            )
            == 555443232122
        )

    # @mark.skip
    @mark.it("correct total joltage in input data")
    def test_99(self, day_03_input):
        assert (get_total_output(day_03_input, 12)) == 173848577117276
