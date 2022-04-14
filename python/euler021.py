import time
import euler
from functools import reduce

euler.print_problem(21)

start = time.time()

# ==================================================
count = 0


def d(n):
    return sum(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) - n


for a in range(2, 10001):
    b = d(a)
    if a == d(b) and a != b:
        count += a + b

print("The Answer is: %s" % int((count/2)))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
