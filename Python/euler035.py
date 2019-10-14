print('''
Problem No. 35
Title:      Circular primes

Problem:    The number, 197, is called a circular prime because all rotations
            of the digits: 197, 971, and 719, are themselves prime.

            There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

            How many circular primes are there below one million?
''')

import time
from math import sqrt

start = time.time()

# ==================================================
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


numbers = []

for i in range(1, 1000000):
    if i not in numbers and isPrime(i):
        if len(str(i)) == 1:
            numbers.append(i)
        else:
            potential = [i]
            i1 = i
            while True:
                i1 = str(i1)[1:]+str(i1)[0]
                if i1[0] == '0':
                    break
                else:
                    i1 = int(i1)
                    if i != i1 and isPrime(i1):
                        potential.append(i1)
                        continue
                    elif i == i1:
                        numbers += potential
                        break
                    else:
                        break
    else:
        continue

answer = len(numbers)

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
