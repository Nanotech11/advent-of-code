with open('input.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]

voltages = []
for line in lines:
    str_num = ''
    for char in '987654321':
        if char in line[:-1]:
            str_num += char
            index = line.index(char)
            for char in '987654321':
                if char in line[index + 1:]:
                    str_num += char
                    break
            break
    voltages.append(int(str_num))

print(sum(voltages))
