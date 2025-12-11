from collections import deque

with open(('input.txt', 'test2.txt')[0], 'r', encoding='utf-8') as file:
    lines = {inp: [[o, False, False] for o in out] for inp, out in ((first, rest.strip().split()) for first, rest in (line.strip().split(':') for line in file))}

count = 0
q = deque(lines['svr'])
while q:
    device, passed_dac, passed_fft = q.pop()
    if device == 'out':
        if passed_dac and passed_fft:
            count += 1
        continue
    if device == 'fft':
        passed_fft = True
    if device == 'dac':
        passed_dac = True
    q.extend([[dev[0], passed_dac, passed_fft] for dev in lines[device]])

print(count)