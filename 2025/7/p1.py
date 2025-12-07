from itertools import chain

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    splits = chain.from_iterable(
        (idx for idx, char in enumerate(line.rstrip()) if char != '.')
        for line in file
        if any(char != '.' for char in line.rstrip())
    )

    beams = {next(splits)}
    count = 0
    for idx in splits:
        if idx in beams:
            count += 1
            beams.remove(idx)
            beams.update((idx - 1, idx + 1))
print(count)
