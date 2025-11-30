import math

import numpy as np
from numpy.typing import NDArray


def numpad_seq(seq: str) -> list[str]:
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """

    numpad = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [' ', '0', 'A']])
    idx_dict = {numpad[r, c]: np.array([r, c]) for r, c in np.ndindex(numpad.shape)}
    current_idx = idx_dict['A']
    sequences: list[str] = []
    moves: list[NDArray[np.int8]] = []
    for c in seq:
        moves.append(idx_dict[c] - current_idx)
        current_idx = idx_dict[c]

    print(seq)

    # This should be the maximum number of useful sequences
    # Each new key will require at most 2 directions, which could be done in either order
    for _ in range(2**len(seq)):
        sequence: str = ''
        for move in moves:
            print(move)
            if move[0] < 0:
                sequence += '^' * abs(move[0])
            if move[1] > 0:
                sequence += '>' * move[1]
            if move[0] > 0:
                sequence += 'v' * move[0]
            if move[1] < 0:
                sequence += '<' * abs(move[1])
            sequence += 'A'
        sequences.append(sequence)
    return sequences


with open('test_input.txt', 'r', encoding='utf-8') as file:
    codes = [line.strip() for line in file.readlines()]

for code in codes:
    print(numpad_seq(code))
