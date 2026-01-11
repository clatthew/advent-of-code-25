from copy import deepcopy


def prepare_input(input_list):
    sep = input_list.index("")
    fresh_id_range_strings = input_list[:sep]
    fresh_id_ranges = [
        [int(i) for i in id_range.split("-")] for id_range in fresh_id_range_strings
    ]
    ingredient_ids = [int(i) for i in input_list[sep + 1 :]]
    fresh_id_ranges = sort_by(fresh_id_ranges, lambda x: x[0])
    return fresh_id_ranges, ingredient_ids


def is_fresh(ingredient_id, fresh_id_ranges, return_id=False):
    for i, id_range in enumerate(fresh_id_ranges):
        if ingredient_id >= id_range[0] and ingredient_id <= id_range[1]:
            return [True, i][return_id]
    return False


def get_no_fresh_ingredients(ingredient_ids, fresh_id_ranges):
    no_fresh_ingredients = 0
    for ingredient_id in ingredient_ids:
        no_fresh_ingredients += is_fresh(ingredient_id, fresh_id_ranges)
    return no_fresh_ingredients


def range_to_no_ids(fresh_id_ranges):
    return sum([id_range[1] - id_range[0] + 1 for id_range in fresh_id_ranges])


def sort_by(sort_list, sort_fn):
    sort_list = deepcopy(sort_list)
    for i, _ in enumerate(sort_list):
        for j, __ in enumerate(sort_list):
            if sort_fn(sort_list[i]) < sort_fn(sort_list[j]):
                placeholder = sort_list[i].copy()
                sort_list[i] = sort_list[j].copy()
                sort_list[j] = placeholder

    return sort_list


def get_final_ranges(sorted_id_ranges):
    final_ranges = [sorted_id_ranges[0]]
    for id_range in sorted_id_ranges[1:]:
        last_range = final_ranges[-1]
        if id_range[0] <= last_range[1]:
            if id_range[1] > last_range[1]:
                last_range[1] = id_range[1]
        else:
            final_ranges.append(id_range)
    return final_ranges
