import time
from euler import print_problem

print_problem(36)
start = time.time()

# ==================================================
answer = 0

for i in range(0, 1000001):
    if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
        answer += i

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
