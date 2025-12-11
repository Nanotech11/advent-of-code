import re
from collections import deque, defaultdict
from itertools import repeat

with open(('input.txt', 'test.txt')[1], 'r', encoding='utf-8') as file:
    goal_pattern = re.compile(r'^\[([\.#]+)\]')
    button_pattern = re.compile(r'\(([\d,]+)\)')
    machines = []
    for line in file:
        goal = tuple({'.': False, '#': True}[char] for char in re.findall(goal_pattern, line)[0])
        buttons = tuple(tuple(int(button) for button in schematic.split(',')) for schematic in re.findall(button_pattern, line))
        machines.append((goal, buttons))

total = 0
visited = defaultdict()
q = deque()
for goal, buttons in machines:
    start = [repeat(False, len(goal))]
    visited.clear()
    visited[start] = 1
    q.clear()
    q.append(start)

    found = False
    while not found:
        curr = q.popleft()
        depth = visited[curr]
        for button in buttons:
            for toggle in button:
                curr[toggle] = not curr[toggle]
            if curr == goal:
                found = True
                total += depth
                break
            if not visited[curr]:
                q.append(curr)
                visited[curr] = depth + 1
    print(goal, total)