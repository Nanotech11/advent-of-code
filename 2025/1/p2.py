with open('input.txt', 'r', encoding='utf-8') as file:
# with open('test_input.txt', 'r', encoding='utf-8') as file:
    rotations = [(line[0], int(line[1:])) for line in file.readlines()]

count = 0
current_value = 50
for direction, amount in rotations:
    for i in range(amount):
        if (current_value := (current_value + (1 if direction == 'R' else -1)) % 100) == 0:
            count += 1

print(count)
