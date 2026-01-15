def prepare_input(input_list):
    return [[int(i) for i in elt.split(",")] for elt in input_list]


def get_rectangle_area(corner_1, corner_2):
    return (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1)


def find_biggest_rectangle(corners):
    max_area = 0
    for i, corner_1 in enumerate(corners):
        for j, corner_2 in enumerate(corners[1:], i + 1):
            area = get_rectangle_area(corner_1, corner_2)
            if area > max_area:
                max_area = area
    return max_area
