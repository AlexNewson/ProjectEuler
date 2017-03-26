print('''
Problem No. 10
Title:      Summation of primes

Problem:    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
            Find the sum of all the primes below two million.
''')

import time
from math import sqrt

start = time.time()

# ==================================================
primeSum = 0


def isPrime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False

    p = 3
    while p < sqrt(x)+1:
        if x % p == 0:
            return False
        p += 2
    return True


for n in range(2, 2000000):
    if isPrime(n):
        primeSum += n

print("The Answer is: %i" % primeSum)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
