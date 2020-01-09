print('''
Problem No. 41
Title:      Pandigital prime

Problem:    We shall say that an n-digit number is pandigital if it
            makes use of all the digits 1 to n exactly once. For example,
            2143 is a 4-digit pandigital and is also prime.

            What is the largest n-digit pandigital prime that exists?
''')

import time

start = time.time()

# ==================================================
from itertools import permutations
from math import sqrt


def isPandigital(y):
    if len(y) == 9:
        x = []
        for i in y:
            if i == "0":
                return False
            elif i in x:
                return False
            x.append(i)
        return True
    else:
        return False


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


answer = 0
a = '123456789'
j = 9
found = False

while not found:
    perm = permutations(a[:j])
    perm = list(perm)[::-1]
    for i in perm:
        number = int(''.join(i))
        if isPrime(number):
            answer = number
            found = True
            break
    j -= 1

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
