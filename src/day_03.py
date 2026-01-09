def get_joltage_of_bank(bank: str, no_batteries=2):
    bank_list = [int(i) for i in bank]
    digits = []
    positions = [-1]
    for i in range(no_batteries, 0, -1):
        candidates = bank_list[positions[-1] + 1 : (-(i - 1) or None)]
        digits.append(max(candidates))
        positions.append(bank_list.index(digits[-1], positions[-1] + 1))
    return int("".join(str(i) for i in digits))


def get_total_output(banks, no_batteries=2):
    return sum([get_joltage_of_bank(bank, no_batteries) for bank in banks])
