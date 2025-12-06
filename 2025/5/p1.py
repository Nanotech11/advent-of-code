with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    ranges: list[tuple[int, int]] = []
    while (line := file.readline().strip()) != '':
        s, e = line.split('-')
        ranges.append((int(s), int(e)))
    ingredients = [int(line) for line in file.readlines()]
ranges.sort()
ingredients.sort()

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
