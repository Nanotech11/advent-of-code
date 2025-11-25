from sympy import isprime

n_primes = 0
for b in range(109317, 126300, 34):
    if isprime(b):
        n_primes += 1
        print(b)
print(f'n_primes: {n_primes}')
