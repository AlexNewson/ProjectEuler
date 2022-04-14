import time
from euler import print_problem
from itertools import permutations

print_problem(49)
start = time.time()

# ==================================================


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i * i//2::i] = [False] * ((n - i * i - 1)//(2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n//2) if sieve[i]]


answer = 0
primes = []

for prime in prime_sieve(10000):
    primes.append(prime)

primes = [x for x in primes if x > 1487]

for prime in primes:
    # Generate a list of the primes digits
    digits = [int(x) for x in str(prime)]
    potential_primes = permutations(str(prime))

    prime_series = [int(''.join(x)) for x in potential_primes]
    prime_series = list(set([x for x in prime_series if x in primes]))
    prime_series.sort()

    if len(prime_series) >= 3:
        for i in range(len(prime_series)):
            for j in range(i + 1, len(prime_series)):
                difference = prime_series[j] - prime_series[i]
                if prime_series[j] + difference in prime_series:
                    answer = str(prime_series[i]) + str(prime_series[j]) + str(prime_series[j] + difference)

print(answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
