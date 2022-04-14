import time
import euler

euler.print_problem(10)

start = time.time()

# ==================================================
primeSum = 0

for n in range(2, 2000000):
    if euler.is_prime(n):
        primeSum += n

print("The Answer is: %i" % primeSum)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
