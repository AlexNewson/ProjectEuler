import time
import euler

euler.print_problem(27)
start = time.time()

# ==================================================
Limit = 1000
nmax = 0

for b in euler.prime_sieve(Limit):
    for a in range(-b + 2, 0, 2):
        n = 1
        while euler.is_prime(n*n + a*n + b):
            n += 1
        if n > nmax:
            nmax, p = n, (a, b)

x = p[0]*p[1]
print("The Answer is: %i" % x)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
