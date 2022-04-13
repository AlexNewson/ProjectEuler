import time
from euler import print_problem
from math import sqrt

print_problem(46)
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


number = 9
answer = 0

while answer == 0:
    # Incriment
    number += 1

    if number % 2 == 1:
        if not is_prime(number):
            x = 0
            while True:
                x += 1
                prime = number - (2 * (x ** 2))
                if prime < 0:
                    answer = number
                    break
                if is_prime(prime):
                    break

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
