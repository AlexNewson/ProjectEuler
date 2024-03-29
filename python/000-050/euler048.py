import time
import euler

euler.print_problem(48)
start = time.time()

# ==================================================
answer = 0

for i in range(1, 1001):
    answer += i**i

print(str(answer)[-10:])
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
