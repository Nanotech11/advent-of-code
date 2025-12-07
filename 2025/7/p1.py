import re

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if any(char in line for char in ('S', '^'))]

beams = {lines[0].index('S')}
count = 0
for line in lines[1:]:
    indices = (m.start() for m in re.finditer(r'\^', line))
    for idx in indices:
        if idx in beams:
            count += 1
            beams.remove(idx)
            beams.update((idx - 1, idx + 1))
print(count)
