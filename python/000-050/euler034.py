import time
import euler
from math import factorial

euler.print_problem(34)
start = time.time()

# ==================================================
answer = 0

for x in range(3, 2540160):
    y = 0
    for d in str(x):
        y += factorial(int(d))
    if y == x:
        print(x)
        answer += x

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
