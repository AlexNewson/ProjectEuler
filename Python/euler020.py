import time
from euler import print_problem

print_problem(20)
from math import factorial as f

start = time.time()

# ==================================================
print("The Answer is: %i" % sum([int(digit) for digit in str(f(100))]))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
