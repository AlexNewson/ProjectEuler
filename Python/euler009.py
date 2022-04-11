import time
from euler import print_problem

print_problem(9)
from math import sqrt, floor

start = time.time()

# ==================================================
# Two Equations
# a2 + b2 = c2
# a + b + c = 1000

# Equations Substituted
# 0 = 1000^2 - 2000a - 2000b + 2ab

# 2000a - 2ab = 1000^2 - 2000b
# a(2000 - 2b) = 1000^2 - 2000b
# a = (1000^2 - 2000b)/(2000-2b)
# a = 1000(1000 - 2b)/(2000-2b)

# Simplified
# a = 1000 * 500-b / 1000-a

for a in range(1, 500):
    b = 1000 * (500-a) / (1000-a)
    c = sqrt(a**2 + b**2)
    if int(floor(c)) == c and 0 < a < b < c:
        answer = int(a*b*c)
        print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
