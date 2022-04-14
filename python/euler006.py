import time
import euler

euler.print_problem(6)
start = time.time()

# ==================================================
sumOfSq = 0
sqOfSum = 0

for x in range(1, 101):
    sumOfSq += x**2
    sqOfSum += x

sumOfSq = sumOfSq
sqOfSum = sqOfSum**2

diff = sqOfSum - sumOfSq

print("The Answer is: %i" % diff)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
