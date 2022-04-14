import time
import euler
from math import factorial

euler.print_problem(20)

start = time.time()

# ==================================================
print("The Answer is: %i" % sum([int(digit) for digit in str(factorial(100))]))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
