count = 0
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        count += int(line)

print(count)
