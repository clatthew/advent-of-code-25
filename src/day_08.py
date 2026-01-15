from math import sqrt, prod
from src.day_05 import sort_by


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
    # with open(f"distance_matrix_{n}.txt", "w") as f:
    #     for row in distance_matrix:
    #         f.write(",".join([str(i) for i in row]) + "\n")
    for i, row in enumerate(distance_matrix):
        for j, distance in enumerate(row):
            if distance < 10000:
                distances.append({"connection": [i, i + j + 1], "distance": distance})
    sorted_connections = [
        connection["connection"]
        for connection in sort_by(distances, lambda x: x["distance"])
    ]
    return sorted_connections[:n]


debug_target = 593


def build_circuits(box_positions, n):
    closest_pairings = get_closest_pairings(get_distance_matrix(box_positions), n)
    connection_lookup = [-1 for _ in range(len(box_positions))]
    for pairing in closest_pairings:
        if connection_lookup[pairing[0]] < 0:
            if connection_lookup[pairing[1]] < 0:
                connection_lookup[pairing[0]] = pairing[0]
                connection_lookup[pairing[1]] = connection_lookup[pairing[0]]
            else:
                connection_lookup[pairing[0]] = connection_lookup[pairing[1]]
        elif connection_lookup[pairing[1]] < 0:
            connection_lookup[pairing[1]] = connection_lookup[pairing[0]]
        elif connection_lookup[pairing[0]] != connection_lookup[pairing[1]]:
            val_to_change = connection_lookup[pairing[1]]
            for i, _ in enumerate(connection_lookup):
                if connection_lookup[i] == val_to_change:
                    connection_lookup[i] = connection_lookup[pairing[0]]
    circuit_sizes = {}
    for circuit in connection_lookup:
        if circuit not in circuit_sizes:
            circuit_sizes[circuit] = 1
        else:
            circuit_sizes[circuit] += 1
    return prod(
        sorted(
            [value for key, value in circuit_sizes.items() if key != -1], reverse=True
        )[:3]
    )
