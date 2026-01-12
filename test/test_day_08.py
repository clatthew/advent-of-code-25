from pytest import mark, fixture
from src.day_01 import get_input
from src.day_08 import (
    prepare_input,
    straight_line_distance,
    sqrt,
    get_distance_matrix,
    get_closest_pairings,
    triangular_matrix,
    wire_junction_boxes,
)

from pprint import pprint


@fixture
def test_input():
    # x y z
    return prepare_input(
        [
            "162,817,812",
            "57,618,57",
            "906,360,560",
            "592,479,940",
            "352,342,300",
            "466,668,158",
            "542,29,236",
            "431,825,988",
            "739,650,466",
            "52,470,668",
            "216,146,977",
            "819,987,18",
            "117,168,530",
            "805,96,715",
            "346,949,466",
            "970,615,88",
            "941,993,340",
            "862,61,35",
            "984,92,344",
            "425,690,689",
        ]
    )


@fixture
def day_08_input():
    return prepare_input(get_input("input/day_08.txt"))


class Testprepare_input:
    def test_1(self):
        test_data = ["162,817,812", "57,618,57"]
        expected = [[162, 817, 812], [57, 618, 57]]
        assert prepare_input(test_data) == expected


class Teststraight_line_distance:
    @mark.it("distance between two of the same point is 0")
    def test_1(self):
        input = {"a": [500, 500, 500], "b": [500, 500, 500]}
        assert straight_line_distance(**input) == 0

    @mark.it("difference of 1 in one dimension")
    def test_2(self):
        input = {"a": [255, 256, 256], "b": [256, 256, 256]}
        assert straight_line_distance(**input) == 1

    @mark.it("differences in all dimensions")
    def test_3(self):
        input = {"a": [255, 256, 256], "b": [122, 444, 943]}
        assert straight_line_distance(**input) == sqrt(525002)


class Testget_distance_matrix:
    # @mark.skip
    @mark.it("returns 2d triangular array of correct dimensions")
    def test_1(self, test_input):
        result = get_distance_matrix(test_input)
        assert len(result) == 19
        assert len(result[0]) == 19
        assert len(result[-1]) == 1

    @mark.it("returns matrix with correct distances")
    def test_2(self):
        test_data = [[500, 500, 500], [500, 500, 500], [122, 444, 943], [255, 256, 256]]
        result = get_distance_matrix(test_data)
        expected = [
            [0, 585.0376056289032, 423.1985349691088],
            [585.0376056289032, 423.1985349691088],
            [724.5702174392762],
        ]
        assert result == expected

    # @mark.skip
    @mark.it("can compute distance matrix for day's input")
    def test_3(self, day_08_input):
        get_distance_matrix(day_08_input)
        assert True


class Testget_closest_pairings:
    @mark.it("returns single closest pairing")
    def test_1(self):
        test_input = (
            get_distance_matrix(
                [[500, 500, 500], [500, 500, 500], [122, 444, 943], [255, 256, 256]]
            ),
            1,
        )
        result = get_closest_pairings(*test_input)
        expected = [{"connection": [0, 1], "distance": 0.0}]
        assert result == expected

    @mark.it("returns three closest pairings")
    def test_2(self):
        test_input = (
            get_distance_matrix(
                [[500, 500, 500], [500, 500, 500], [122, 444, 943], [255, 256, 256]]
            ),
            3,
        )
        result = get_closest_pairings(*test_input)
        expected = [
            {"connection": [0, 1], "distance": 0.0},
            {"connection": [0, 3], "distance": 423.1985349691088},
            {"connection": [1, 2], "distance": 423.1985349691088},
        ]
        assert result == expected


class Testwire_junction_boxes:
    @mark.skip
    @mark.it("small example")
    def test_1(self):
        box_positions = [
            [432, 500, 777],
            [500, 500, 500],
            [122, 444, 943],
            [255, 256, 256],
        ]
        expected = [[1, 1, 0], [0, 1], [0]]
        result = wire_junction_boxes(box_positions, 3)
        assert result == expected

    @mark.it("test data")
    def test_2(self, test_input):
        expected = [[1, 1, 0], [0, 1], [0]]
        result = wire_junction_boxes(test_input, 10)
        pprint(result)
        assert result == expected
