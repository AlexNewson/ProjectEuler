import time
from euler import print_problem

print_problem(16)
start = time.time()

# ==================================================
number = 2**1000
n = 0

for i in str(number):
    n += int(i)

print("The Answer is: %i" % n)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
