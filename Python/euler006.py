print('''
Problem No. 6
Title:      Sum square difference

Problem:    The sum of the squares of the first ten natural numbers is,

            12 + 22 + ... + 102 = 385

            The square of the sum of the first ten natural numbers is,

            (1 + 2 + ... + 10)2 = 552 = 3025

            Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
            Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
''')

import time

start = time.time()

# ==================================================
sumOfSq = 0
sqOfSum = 0

for x in range(1, 101):
    sumOfSq += x**2
    sqOfSum += x

sumOfSq = sumOfSq
sqOfSum = sqOfSum**2

diff = sqOfSum - sumOfSq

print("The Answer is: %i" % diff)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
