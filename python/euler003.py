import time
import euler

euler.print_problem(3)
start = time.time()

# ==================================================
x = 600851475143

factors = []
loop = 2

while loop <= x:
    if x % loop == 0:
        x /= loop
        factors.append(loop)
    else:
        loop += 1

print("The Answer is: %i" % max(factors))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
