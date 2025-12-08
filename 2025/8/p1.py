from itertools import combinations
from math import prod, sqrt
from operator import itemgetter

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    boxes = [(int(x), int(y), int(z)) for x, y, z in (line.split(',') for line in file)]

dist_dict = {}
for box1, box2 in combinations(boxes, 2):
    dist_dict[(box1, box2)] = sqrt((box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2)
close_boxes = (key for key, _val in sorted(dist_dict.items(), key=itemgetter(1)))

circuits: list[set[tuple]] = [{box} for box in boxes]
count = 0
while count < 1000:
    box1, box2 = next(close_boxes)
    containing_circuits = [circuit for circuit in circuits if box1 in circuit or box2 in circuit]
    if len(containing_circuits) == 1:
        count += 1
        continue
    containing_circuits[0].update(containing_circuits[1])
    circuits.remove(containing_circuits[1])
    count += 1
large_circuits = [len(circuit) for circuit in sorted(circuits, key=len, reverse=True)]
print(len(circuits))
print(large_circuits)
print(prod(large_circuits[:3]))
