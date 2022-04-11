import time
from euler import print_problem

print_problem(7)
from math import sqrt

start = time.time()

# ==================================================
def isPrime(x):
    if x % 2 == 0:
        return False

    p = 3
    while p < sqrt(x)+1:
        if x % p == 0: return False
        p += 2
    return True

def nthPrime(n):
    prime = 2
    primes = 1
    number = 3
    while primes < n:
        if isPrime(number):
            prime = number
            primes += 1
        number += 1
    return prime

answer = nthPrime(10001)
print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
