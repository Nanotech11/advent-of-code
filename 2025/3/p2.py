with open('input.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]

voltages = []
for line in lines:
    str_num = ''
    remaining_chars = 12
    index = 0
    while remaining_chars > 1:
        for char in '9876543210':
            if char in line[index:-(remaining_chars - 1)]:
                index = line[index:-(remaining_chars - 1)].index(char) + 1 + index
                str_num += char
                remaining_chars -= 1
                break
    for char in '9876543210':
        if char in line[index:]:
            str_num += char
            break
    voltages.append(int(str_num))
print(sum(voltages))
