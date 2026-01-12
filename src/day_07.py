def split_row(row, beams):
    candidate_output_beams = []
    splits = 0
    for beam in beams:
        if row[beam] == "^":
            candidate_output_beams += [beam - 1, beam + 1]
            splits += 1
        else:
            candidate_output_beams.append(beam)
    return [
        beam
        for beam in list(set(candidate_output_beams))
        if beam >= 0 and beam < len(row)
    ], splits


def analyse_manifold(diagram):
    beams = [diagram[0].index("S")]
    splits = 0
    for row in diagram[1:]:
        beams, new_splits = split_row(row, beams)
        splits += new_splits
    return splits
