with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    ranges = sorted(((int(s), int(e)) for s, e in (line.split('-') for line in iter(file.readline, '\n'))))
    ingredients = sorted((int(line) for line in file))

n_fresh = 0
idx = 0
for ingredient in ingredients:
    for i, (start, end) in enumerate(ranges[idx:]):
        if ingredient >= start:
            idx = i
            if ingredient <= end:
                n_fresh += 1
                break
print(n_fresh)
