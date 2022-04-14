import time
import euler

euler.print_problem(7)

start = time.time()

# ==================================================
answer = euler.nth_prime(10001)
print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
