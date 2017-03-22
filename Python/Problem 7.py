print('''
Problem No. 7
Title:      10001st prime

Problem:    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
            What is the 10 001st prime number?
''')

import time

start = time.time()

# ==================================================
def isPrime(x):
    if x % 2 == 0:
        return False

    p = 3
    while p < x**0.5+1:
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
print(answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
