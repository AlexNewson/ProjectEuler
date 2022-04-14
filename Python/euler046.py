import time
import euler
from math import sqrt

euler.print_problem(46)
start = time.time()

# ==================================================
number = 9
answer = 0

while answer == 0:
    # Increment number by one
    number += 1

    # Check if number is odd
    if number % 2 == 1:
        # Check if it's a composite odd, (i.e. not a prime)
        if not euler.is_prime(number):
            x = 0
            while True:
                # Increment the "twice a square number"
                x += 1
                # Calculate the potential prime number needed to make the formula work
                prime = number - (2 * (x ** 2))
                # If it's a prime, we've found a number that fits the conjecture
                if euler.is_prime(prime):
                    break
                # If we reach 0 and still haven't found a prime, the number breaks the conjecture
                if prime < 0:
                    answer = number
                    break

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
