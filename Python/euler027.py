import time
from euler import print_problem

print_problem(27)
start = time.time()

# ==================================================
from math import sqrt


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def primeSieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i * i//2::i] = [False] * ((n - i * i - 1)//(2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n//2) if sieve[i]]


Limit = 1000
nmax = 0
for b in primeSieve(Limit):
    for a in range(-b + 2, 0, 2):
        n = 1
        while isPrime(n*n + a*n + b):
            n += 1
        if n > nmax:
            nmax, p = n, (a, b)

x = p[0]*p[1]
print("The Answer is: %i" % x)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
