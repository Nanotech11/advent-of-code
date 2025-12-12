import re
from collections import defaultdict, deque

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    button_pattern = re.compile(r'\(([\d,]+)\)')
    jolt_pattern = re.compile(r'\{([\d,]+)\}$')
    machines = []
    for line in file:
        joltages = tuple((int(joltage) for joltage in re.findall(jolt_pattern, line)[0].split(',')))
        buttons = tuple(
            tuple((int(wire) for wire in schematic.split(','))) for schematic in re.findall(button_pattern, line)
        )
        machines.append((joltages, buttons))

total = 0
visited: dict[tuple, int] = {}
q: deque[dict] = deque()
for joltages, buttons in machines[1:]:
    start: dict[int, int] = defaultdict(lambda: 0)
    visited.clear()
    visited[tuple(start.items())] = 1
    q.clear()
    q.append(start)

    found = False
    local_total = 0
    while not found:
        curr = q.popleft()
        depth = visited[tuple(curr.items())]
        for button in buttons:
            after_button = curr.copy()
            for wire in button:
                after_button[wire] += 1
            print(curr, '\t', after_button)
            if any((curr_jolt > goal_jolt for curr_jolt, goal_jolt in zip(after_button.values(), joltages))):
                continue
            if tuple(after_button.values()) == joltages:
                found = True
                # total += depth
                local_total += depth
                break
            if tuple(after_button.items()) not in visited:
                q.append(after_button)
                visited[tuple(after_button.items())] = depth + 1
    print(local_total)
    total += local_total
print(total)
