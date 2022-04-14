import time
import euler

euler.print_problem(31)
start = time.time()

# ==================================================
solutions = [0] * 201
solutions[0] = 1
coins = [1, 2, 5, 10, 20, 50, 100, 200]

for x in coins:
    for y in range(x, 201):
        solutions[y] += solutions[y - x]

answer = solutions[200]

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
