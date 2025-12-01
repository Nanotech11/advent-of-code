with open('input.txt', 'r', encoding='utf-8') as file:
# with open('test_input.txt', 'r', encoding='utf-8') as file:
    rotations = [(line[0], int(line[1:])) for line in file.readlines()]

count = 0
current_value = 50
for rot in rotations:
    if rot[0] == 'R':
        current_value = (current_value + rot[1]) % 100
    if rot[0] == 'L':
        current_value = (current_value - rot[1]) % 100
    if current_value == 0:
        count += 1

print(count)
