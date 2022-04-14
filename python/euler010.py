import time
import euler

euler.print_problem(10)

start = time.time()

# ==================================================
prime_sum = 0

for n in range(2, 2000000):
    if euler.is_prime(n):
        prime_sum += n

print("The Answer is: %i" % prime_sum)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
