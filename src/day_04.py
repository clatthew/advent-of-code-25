from copy import deepcopy


def prepare_input(input_list):
    return [list(row) for row in input_list]


def adjacent_rolls(roll_grid, row, col):
    last_row = len(roll_grid) - 1
    last_col = len(roll_grid[0]) - 1
    assert row <= last_row
    assert col <= last_col
    directions = {
        "top_left": {"use?": (row > 0 and col > 0), "vector": [-1, -1]},
        "top": {"use?": (row > 0), "vector": [-1, 0]},
        "top_right": {"use?": (row > 0 and col < last_col), "vector": [-1, 1]},
        "left": {"use?": (col != 0), "vector": [0, -1]},
        "right": {"use?": (col < last_col), "vector": [0, 1]},
        "bottom_left": {"use?": (row < last_row and col > 0), "vector": [1, -1]},
        "bottom": {"use?": (row < last_row), "vector": [1, 0]},
        "bottom_right": {"use?": (row < last_row and col < last_col), "vector": [1, 1]},
    }
    no_adjecent_rolls = 0
    for _, details in directions.items():
        if not details["use?"]:
            continue
        if roll_grid[row + details["vector"][0]][col + details["vector"][1]] == "@":
            no_adjecent_rolls += 1
    return no_adjecent_rolls


def accessible_roll_locations(roll_grid, max_adjacent=3):
    accessible_locations = []
    for i, row in enumerate(roll_grid):
        for j, cell in enumerate(row):
            if cell == "@" and adjacent_rolls(roll_grid, i, j) <= max_adjacent:
                accessible_locations.append([i, j])
    return accessible_locations


def count_accessible_rolls(roll_grid, max_adjacent=3):
    return len(accessible_roll_locations(roll_grid, max_adjacent))


def repeated_removals(roll_grid, max_adjacent=3, iteration=1):
    rolls_to_remove = accessible_roll_locations(roll_grid, max_adjacent)
    for location in rolls_to_remove:
        roll_grid[location[0]][location[1]] = iteration
    if count_accessible_rolls(roll_grid, max_adjacent):
        return repeated_removals(roll_grid, max_adjacent, iteration + 1)
    return roll_grid


def count_possible_removals(roll_grid, max_adjacent=3):
    removed_grid = repeated_removals(deepcopy(roll_grid), max_adjacent)
    rolls_in_original = 0
    rolls_in_removed = 0
    for i, row in enumerate(removed_grid):
        for j, _ in enumerate(row):
            if roll_grid[i][j] == "@":
                rolls_in_original += 1
            if removed_grid[i][j] == "@":
                rolls_in_removed += 1
    return rolls_in_original - rolls_in_removed
