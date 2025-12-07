from itertools import pairwise

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    lines = list(file)

operator_line = lines[-1]
start_indices = []
for idx, char in enumerate(operator_line):
    if char != ' ':
        start_indices.append(idx)
start_indices.append(len(operator_line) + 1)
number_lines = []
for line in lines[:-1]:
    number_lines.append([line[start : end - 1] for start, end in pairwise(start_indices)])

problems = zip(*number_lines, operator_line.split())

result = 0
for problem in problems:
    if problem[-1] == '+':
        temp_result = 0
        num_strs = zip(*problem[:-1])
        for num_str in num_strs:
            temp_result += int(''.join(num_str))
        result += temp_result
    else:
        num_strs = zip(*problem[:-1])
        temp_result = int(''.join(next(num_strs)))
        for num_str in num_strs:
            temp_result *= int(''.join(num_str))
        result += temp_result

print(result)
