import re

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if any(char in line for char in ('S', '^'))]

beams = {i: 0 for i in range(len(lines[0]))}
beams[lines[0].index('S')] += 1
timelines = 1
for line in lines[1:]:
    indices = (m.start() for m in re.finditer(r'\^', line))
    for idx in indices:
        if idx in beams:
            timelines += beams[idx]
            beams[idx - 1] += beams[idx]
            beams[idx + 1] += beams[idx]
            beams[idx] = 0
print(timelines)
