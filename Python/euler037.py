print('''
Problem No. 37
Title:      Truncatable primes

Problem:    The number 3797 has an interesting property. Being prime itself,
            it is possible to continuously remove digits from left to right,
            and remain prime at each stage: 3797, 797, 97, and 7. Similarly
            we can work from right to left: 3797, 379, 37, and 3.

            Find the sum of the only eleven primes that are both truncatable
            from left to right and right to left.

            NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
''')

import time

start = time.time()

# ==================================================
from math import sqrt

answer = 0
i = 10
x = 0

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


while x != 11:
    j = i
    if isPrime(int(str(i)[0])):
        while True:
            if isPrime(j):
                if len(str(j)) > 1:
                    j = int(str(j)[1:])
                else:
                    j = i
                    while True:
                        if isPrime(j):
                            if len(str(j)) > 1:
                                j = int(str(j)[:-1])
                            else:
                                print("Found! %i" % i)
                                answer += i
                                x += 1
                                i += 1
                                break
                        else:
                            i += 1
                            break
                    break
            else:
                i += 1
                break
    else:
        i += 1


print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
