from collections import deque

with open(('input.txt', 'test1.txt')[0], 'r', encoding='utf-8') as file:
    lines = {inp: out for inp, out in ((first, rest.strip().split()) for first, rest in (line.strip().split(':') for line in file))}

count = 0
q = deque(lines['you'])
while q:
    device = q.pop()
    if device == 'out':
        count += 1
        continue
    q.extend(lines[device])

print(count)