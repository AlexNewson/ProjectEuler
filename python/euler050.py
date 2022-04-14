import time
import euler

euler.print_problem(50)
start = time.time()

# ==================================================
primes = []
answer = 0
length = 0

for prime in euler.prime_sieve(1000000):
    primes.append(prime)

size = len(primes)
previous_j = size

for i in range(size):
    for j in range(length+i, previous_j):
        add = sum(primes[i:j])
        if add < 1000000:
            if add in primes:
                length = j - i
                answer = add
        else:
            previous_j = j+1
            break
            
print(answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
