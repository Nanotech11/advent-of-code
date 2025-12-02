with open('input.txt', 'r', encoding='utf-8') as file:
    rotations = [({'R': 1, 'L': -1}[line[0]], int(line[1:])) for line in file]

count = 0
current_value = 50
for direction, amount in rotations:
    for i in range(amount):
        if (current_value := (current_value + direction) % 100) == 0:
            count += 1

print(count)
