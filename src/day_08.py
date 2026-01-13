from math import sqrt, prod
from src.day_05 import sort_by
from pprint import pprint
from copy import deepcopy


def prepare_input(input_list):
    return [[int(i) for i in row.split(",")] for row in input_list]


def straight_line_distance(a, b):
    return sqrt(sum([(ib - ia) ** 2 for ia, ib in zip(a, b)]))


def triangular_matrix(n, fill=0):
    return [[fill for _ in range(n - i)] for i in range(n)]


def get_distance_matrix(box_positions):
    no_boxes = len(box_positions)
    distance_matrix = triangular_matrix(no_boxes - 1)
    for i, box1 in enumerate(box_positions):
        for j, box2 in enumerate(box_positions[i + 1 :]):
            distance_matrix[i][j] = straight_line_distance(box1, box2)
    return distance_matrix


def get_closest_pairings(distance_matrix, n):
    distances = []
    for i, row in enumerate(distance_matrix):
        for j, distance in enumerate(row):
            distances.append({"connection": [i, i + j + 1], "distance": distance})
    return sort_by(distances, lambda x: x["distance"])[:n]


def build_circuits(box_positions, n):
    # sorting the pairings won't be sufficient to ensure minimum amount of circuits
    closest_pairings = get_closest_pairings(get_distance_matrix(box_positions), n)
    closest_pairings = sort_by(closest_pairings, lambda x: x["connection"][0])
    circuits = [closest_pairings[0]["connection"]]
    for pairing in closest_pairings[1:]:
        pairing = pairing["connection"]
        inserted = False
        for circuit in circuits:
            if pairing[0] in circuit:
                circuit.append(pairing[1])
                inserted = True
                continue
            elif pairing[1] in circuit:
                circuit.append(pairing[0])
                inserted = True
                continue

        if not inserted:
            circuits.append(pairing)
    return [list(set(circuit)) for circuit in circuits]


def get_result(box_positions, n):
    return prod([len(circuit) for circuit in build_circuits(box_positions, n)[:3]])
