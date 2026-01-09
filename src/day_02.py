from math import ceil


def get_invalid_total_1(id_ranges):
    total_invalids = 0
    for id_range in id_ranges:
        id_range_list = id_range.split("-")
        lower_end = id_range_list[0]
        upper_end = id_range_list[1]
        lower_end_length = len(lower_end)
        segment_length = ceil(lower_end_length / 2)
        for number in range(int(lower_end), int(upper_end) + 1, 1):
            number_string = str(number)
            if number_string[:segment_length] == number_string[segment_length:]:
                total_invalids += number
    return total_invalids


def is_invalid_2(number):
    number_string = str(number)
    number_length = len(number_string)
    max_segment_length = number_length // 2
    for segment_length in range(max_segment_length, 0, -1):
        if number_length % segment_length == 0:
            segment_string = number_string[:segment_length]
            if segment_string * (number_length // segment_length) == number_string:
                # print(number, segment_string)
                return True
    return False


def get_invalid_total_2(id_ranges):
    invalids = []
    for id_range in id_ranges:
        id_range_list = id_range.split("-")
        lower_end = int(id_range_list[0])
        upper_end = int(id_range_list[1])
        invalids += [
            number for number in range(lower_end, upper_end + 1) if is_invalid_2(number)
        ]
    # print(invalids)
    return sum(invalids)
