import time
import euler
from math import sqrt

euler.print_problem(47)
start = time.time()

# ==================================================
# Starting number (2 x 3 x 5 x 7)
number = 210

while True:
    number += 1

    # Check if the number, or it's next 3 neighbours are primes
    if euler.is_prime(number):
        continue
    if euler.is_prime(number + 1):
        continue
    if euler.is_prime(number + 2):
        continue
    if euler.is_prime(number + 3):
        continue

    # Check if the group of 4 have 4 exact prime factors
    if euler.prime_factor_count(number) == 4:
        if euler.prime_factor_count(number + 1) == 4:
            if euler.prime_factor_count(number + 2) == 4:
                if euler.prime_factor_count(number + 3) == 4:
                    break


print("The Answer is: %i" % number)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
