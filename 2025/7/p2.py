from collections import defaultdict
from itertools import chain

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    splits = chain.from_iterable(
        (idx for idx, char in enumerate(line.rstrip()) if char != '.')
        for line in file
        if any(char != '.' for char in line.rstrip())
    )

    beams: dict[int, int] = defaultdict(lambda: 0)
    beams[next(splits)] += 1
    timelines = 1
    for idx in splits:
        timelines += beams[idx]
        beams[idx - 1] += beams[idx]
        beams[idx + 1] += beams[idx]
        beams[idx] = 0
print(timelines)
