import time
from euler import print_problem
from math import sqrt

print_problem(45)
start = time.time()

# ==================================================


def is_pen(x):
    return ((1 + sqrt(1 + 24 * x)) / 6).is_integer()


def gen_hex(n):
    return int(n * (2 * n - 1))


i = 144

while True:
    hexagon = gen_hex(i)
    if is_pen(hexagon):
        break
    i += 1


print("The Answer is: %i" % hexagon)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
