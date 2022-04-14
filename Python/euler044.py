import sys
import time
import euler
from math import sqrt
from itertools import combinations

euler.print_problem(44)
start = time.time()

# ==================================================
pentagonal_numbers = []
lowest_d = sys.maxsize

for i in range(1, 2500):
    pentagonal_numbers.append(euler.generate_pentagonal(i))

for pair in combinations(pentagonal_numbers, 2):
    s = pair[0] + pair[1]
    if euler.is_pentagonal(s):
        d = abs(pair[0] - pair[1])
        if euler.is_pentagonal(d):
            if d < lowest_d:
                lowest_d = d

print("The Answer is: %i" % lowest_d)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
