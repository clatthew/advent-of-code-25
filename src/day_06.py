from math import prod


def prepare_input(input_list):
    rows = [row.split() for row in input_list]
    return [
        [int(row[j]) if i < len(rows) - 1 else row[j] for i, row in enumerate(rows)]
        for j, _ in enumerate(rows[0])
    ]


def prepare_input_2(input_list, operation_row=3):
    new_number_indices = [
        i for i, element in enumerate(input_list[operation_row]) if element != " "
    ] + [len(input_list[operation_row]) + 1]
    problems = []
    for i, start in enumerate(new_number_indices[:-1]):
        stop = new_number_indices[i + 1] - 1
        problems.append([row[start:stop] for row in input_list])
    new_problems = []
    for problem in problems:
        operation = problem[-1]
        numbers = problem[:-1]
        new_problems.append(
            [
                int("".join([number[i] for number in numbers]))
                for i, _ in enumerate(numbers[0])
            ]
            + [operation]
        )
    return new_problems


def solve_problem(operation, numbers):
    if "+" in operation:
        return sum(numbers)
    if "*" in operation:
        return prod(numbers)


def solve_worksheet(worksheet):
    return sum([solve_problem(problem[-1], problem[:-1]) for problem in worksheet])
