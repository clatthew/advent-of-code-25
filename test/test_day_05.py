from src.day_05 import (
    prepare_input,
    get_no_fresh_ingredients,
    sort_by,
    get_final_ranges,
    range_to_no_ids,
    deepcopy,
)
from src.day_01 import get_input
from pytest import mark, fixture


@fixture
def day_05_input():
    return prepare_input(get_input("input/day_05.txt"))


@fixture
def test_input():
    return prepare_input(
        [
            "3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32",
        ]
    )


class Testinput:
    @mark.it("correctly processes the test input")
    def test_1(self, test_input):
        expected = ([[3, 5], [10, 14], [12, 18], [16, 20]], [1, 5, 8, 11, 17, 32])
        assert test_input == expected

    @mark.it("correctly processes input where second elements follow different order")
    def test_2(self):
        test_data = ["3-5", "2-8", "", "3", "7"]
        expected = ([[2, 8], [3, 5]], [3, 7])
        assert prepare_input(test_data) == expected


class Testpart_1:
    @mark.it("correct number of fresh ingredients for the test input")
    def test_1(self, test_input):
        expected = 3
        assert get_no_fresh_ingredients(test_input[1], test_input[0]) == expected

    @mark.it("correct number of fresh ingredients for day 5 input")
    def test_2(self, day_05_input):
        expected = 840
        assert get_no_fresh_ingredients(day_05_input[1], day_05_input[0]) == expected


class Testsort_by:
    @mark.it("sort short list")
    def test_1(self):
        test_data = [[5, 3], [2, 2]]
        expected = [[2, 2], [5, 3]]
        result = sort_by(test_data, lambda x: x[0])
        assert result == expected

    @mark.it("sort longer list")
    def test_3(self):
        test_data = [[5, 3], [2, 2], [6, 4], [1, 2], [3, 2], [5, 7]]
        expected = [[1, 2], [2, 2], [3, 2], [5, 3], [5, 7], [6, 4]]
        result = sort_by(test_data, lambda x: x[0])
        assert result == expected

    @mark.it("sorting input data doesn't change the sum")
    def test_4(self, day_05_input):
        expected = sum(sum(i) for i in day_05_input[0])
        result = sum(sum(i) for i in sort_by(day_05_input[0], lambda x: x[0]))
        assert result == expected

    @mark.it("does not mutate input list")
    def test_2(self):
        test_data = [[5, 3], [2, 2]]
        test_data_copy = deepcopy(test_data)
        assert sort_by(test_data, lambda x: x[0]) is not test_data
        assert test_data == test_data_copy


class Testget_final_ranges:
    @mark.it("correct number of fresh ids for the test input")
    def test_1(self, test_input):
        expected_number = 14
        expected_ranges = [[3, 5], [10, 20]]
        final_ranges = get_final_ranges(test_input[0])
        result = range_to_no_ids(final_ranges)
        assert final_ranges == expected_ranges
        assert result == expected_number

    @mark.it("correct number of fresh ids for the day 5 input")
    def test_2(self, day_05_input):
        expected = 359913027576322
        final_ranges = get_final_ranges(day_05_input[0])
        result = range_to_no_ids(final_ranges)
        assert result == expected

    @mark.it("non-overlapping ranges")
    def test_3(self, day_05_input):
        final_ranges = get_final_ranges(day_05_input[0])
        last_upper = 0
        for id_range in final_ranges:
            current_lower = id_range[0]
            assert current_lower > last_upper
            last_upper = id_range[1]

    @mark.it("output is still sorted")
    def test_4(self, day_05_input):
        final_ranges = get_final_ranges(day_05_input[0])
        assert final_ranges == sort_by(final_ranges, lambda x: x[0])
        assert final_ranges == sort_by(final_ranges, lambda x: x[1])
