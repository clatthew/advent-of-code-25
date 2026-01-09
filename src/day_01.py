def get_input(filepath):
    with open(filepath, "r") as f:
        return [line.strip("\n") for line in f]


directions = {"L": -1, "R": 1}


def get_number_of_zeroes(dial_pos, instructions, every_zero=False):
    number_of_zeroes = int(dial_pos == 0)
    print("___", dial_pos, number_of_zeroes)
    for instruction in instructions:
        direction = directions[instruction[0]]
        distance = int(instruction[1:])
        for _ in range(distance):
            dial_pos = (dial_pos + direction) % 100
            number_of_zeroes += every_zero * (dial_pos == 0)
        number_of_zeroes += (1 - every_zero) * (dial_pos == 0)
        print(instruction, dial_pos, number_of_zeroes)
    return number_of_zeroes
