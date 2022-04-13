import time
from euler import print_problem
from math import sqrt

print_problem(47)
start = time.time()

# ==================================================


def is_prime(n):
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


def prime_factor_count(x):
    i = 2
    primes = set()
    while i < x ** 0.5 or x == 1:
        if x % i == 0:
            x = x / i
            primes.add(i)
            i -= 1
        i += 1
    return len(primes) + 1


# Starting number (2 x 3 x 5 x 7)
number = 210

while True:
    number += 1

    # Check if the number, or it's next 3 neighbours are primes
    if is_prime(number):
        continue
    if is_prime(number + 1):
        continue
    if is_prime(number + 2):
        continue
    if is_prime(number + 3):
        continue

    # Check if the group of 4 have 4 exact prime factors
    if prime_factor_count(number) == 4:
        if prime_factor_count(number + 1) == 4:
            if prime_factor_count(number + 2) == 4:
                if prime_factor_count(number + 3) == 4:
                    break


print("The Answer is: %i" % number)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
