import time
import euler
from math import factorial as f

euler.print_problem(15)

start = time.time()

# ==================================================
# Using the Combination formula of 20 Right moves and
# a total of 40 moves, we can calculate the number of
# possible paths:
m = 40
r = 20

answer = (f(m))/(f(r)*f(m-r))
print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
