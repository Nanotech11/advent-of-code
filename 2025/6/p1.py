from math import prod

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    problems = zip(*[line.rstrip().split() for line in file])

results = 0
for problem in problems:
    operator = {'+': sum, '*': prod}[problem[-1]]
    results += operator((int(val) for val in problem[:-1]))  # type: ignore

print(results)
