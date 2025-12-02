with open('input.txt', 'r', encoding='utf-8') as file:
    rotations = [{'R': 1, 'L': -1}[line[0]] * int(line[1:]) for line in file]

count = 0
current_value = 50
for rotation in rotations:
    current_value = (current_value + rotation) % 100
    if current_value == 0:
        count += 1

print(count)
