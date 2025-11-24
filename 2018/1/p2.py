found = False
count = 0
past_counts: set[int] = {0}
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
while not found:
    for line in lines:
        count += int(line)
        before_len = len(past_counts)
        past_counts.add(count)
        if before_len == len(past_counts):
            found = True
            break
print(count)
