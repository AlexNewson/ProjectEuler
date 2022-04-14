import time
import euler

euler.print_problem(12)
from math import sqrt

start = time.time()

# ==================================================
found = False

n = 0
number = 0

while not found:
    n += 1
    number += n
    factors = set([])

    for i in range(1, int((sqrt(number))+1)):
        if number % i == 0:
            factors.add(i)
            factors.add(number/i)

    if len(factors) >= 500:
        found = True

print("The Answer is: %i" % number)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
