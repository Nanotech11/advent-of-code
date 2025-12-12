import re
from collections import deque

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    light_pattern = re.compile(r'^\[([\.#]+)\]')
    button_pattern = re.compile(r'\(([\d,]+)\)')
    machines = []
    for line in file:
        lights = int(re.findall(light_pattern, line)[0][::-1].replace('.', '0').replace('#', '1'), base=2)
        buttons = tuple(
            sum((2 ** int(wire) for wire in schematic.split(','))) for schematic in re.findall(button_pattern, line)
        )
        machines.append((lights, buttons))

total = 0
visited: dict[int, int] = {}
q: deque[int] = deque()
for lights, buttons in machines:
    start = 0
    visited.clear()
    visited[start] = 1
    q.clear()
    q.append(start)

    found = False
    while not found:
        curr = q.popleft()
        depth = visited[curr]
        for button in buttons:
            after_button = curr ^ button
            if after_button == lights:
                found = True
                total += depth
                break
            if after_button not in visited:
                q.append(after_button)
                visited[after_button] = depth + 1
print(total)
