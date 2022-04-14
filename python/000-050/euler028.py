import time
import euler

euler.print_problem(28)
start = time.time()

# ==================================================
gridSize = 1001
totalSize = gridSize ** 2
answer = 0

gap = 1
count = 1
repeat = -1

for i in range(1, totalSize + 1):
    if count == gap:
        answer += i
        count = 0
        repeat += 1
    else:
        count += 1

    if repeat == 4:
        gap += 2
        repeat = 0


print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
