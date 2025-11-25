register: dict[str, int] = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
pointer = 0
mul_counter = 0
with open('input.txt', 'r', encoding='utf-8') as file:
    prog: list[str] = file.readlines()

while pointer < len(prog):
    ins = prog[pointer].split()
    if ins[0] == 'set':
        register[ins[1]] = register[ins[2]] if ins[2].isalpha() else int(ins[2])
    elif ins[0] == 'sub':
        register[ins[1]] -= register[ins[2]] if ins[2].isalpha() else int(ins[2])
    elif ins[0] == 'mul':
        register[ins[1]] *= register[ins[2]] if ins[2].isalpha() else int(ins[2])
        mul_counter += 1
    elif ins[0] == 'jnz':
        if (register[ins[1]] if ins[1].isalpha() else int(ins[1])) != 0:
            pointer += register[ins[2]] if ins[2].isalpha() else int(ins[2])
            continue
    pointer += 1
print(mul_counter)
