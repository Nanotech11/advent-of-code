with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    lines = [line.strip().split() for line in file]

results = 0
problems = zip(*lines)

for problem in problems:
    if problem[-1] == '+':
        results += sum((int(val) for val in problem[:-1]))
    else:
        temp_result = int(problem[0])
        for val in problem[1:-1]:
            temp_result *= int(val)
        results += temp_result

print(results)
