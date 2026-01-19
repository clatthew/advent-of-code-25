from pprint import pprint


def prepare_input(input_list):
    return [[int(i) for i in elt.split(",")] for elt in input_list]


def get_rectangle_area(corner_1, corner_2):
    return (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1)


def find_biggest_rectangle(corners):
    max_area = 0
    for i, corner_1 in enumerate(corners):
        for corner_2 in corners[i:]:
            area = get_rectangle_area(corner_1, corner_2)
            if area > max_area:
                max_area = area
    return max_area


def get_furthest_corner(corners):
    max_corner = [0, 0]
    for corner in corners[::-1]:
        max_corner[0] = max(max_corner[0], corner[0])
        max_corner[1] = max(max_corner[1], corner[1])
    return max_corner


def get_blank_floor_map(max_corner, blank="."):
    return [[blank for _ in range(max_corner[0] + 1)] for _ in range(max_corner[1] + 1)]


def fill_between(floor_map, prev_square, new_square):
    line_index = new_square[0] == prev_square[0]
    direction = 1 - 2 * (new_square[line_index] < prev_square[line_index])
    for i in range(
        prev_square[line_index] + direction,
        new_square[line_index],
        direction,
    ):
        if line_index:
            floor_map[i][new_square[1 - line_index]] = "X"
        else:
            floor_map[new_square[1 - line_index]][i] = "X"
    return floor_map


def produce_outline(squares):
    max_corner = get_furthest_corner(squares)
    floor_map = get_blank_floor_map(max_corner)
    prev_square = squares[0]
    floor_map[prev_square[1]][prev_square[0]] = "#"
    for square in squares[1:]:
        floor_map[square[1]][square[0]] = "#"
        floor_map = fill_between(floor_map, prev_square, square)
        prev_square = square
    floor_map = fill_between(floor_map, prev_square, squares[0])
    return floor_map


def fill_shape(outline):
    types = {".": 0, "#": 1, "X": 1}
    for j, row in enumerate(outline):
        inside = False
        for i, cell in enumerate(row):
            if inside:
                if not types[cell]:
                    inside = False

            else:
                if types[cell]:
                    inside = True
