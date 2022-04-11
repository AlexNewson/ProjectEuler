import sys
import time
from euler import print_problem
from math import sqrt
from itertools import combinations

print_problem(44)
start = time.time()

# ==================================================


def gen_pen(n):
    return int((n * (3 * n - 1)) / 2)


def is_pen(x):
    return ((1+sqrt(1+24*x))/6).is_integer()


pentagonal_numbers = []
lowest_d = sys.maxsize

for i in range(1, 2500):
    pentagonal_numbers.append(gen_pen(i))

for pair in combinations(pentagonal_numbers, 2):
    s = pair[0] + pair[1]
    if is_pen(s):
        d = abs(pair[0] - pair[1])
        if is_pen(d):
            if d < lowest_d:
                lowest_d = d

print("The Answer is: %i" % lowest_d)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
