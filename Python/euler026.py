import time
import euler

euler.print_problem(26)
start = time.time()

# ==================================================


def cycle_length(n):
    x = 10
    i = 0
    while x != 10 or i < 1:
        x = (x % n) * 10
        i += 1
    return i


longest = 0

for i in range(2, 1000):
    if i % 2 != 0 and i % 5 != 0:
        length = cycle_length(i)
        if length > longest:
            longest = length
            answer = i

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
