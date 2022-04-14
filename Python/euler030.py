import time
import euler

euler.print_problem(30)
start = time.time()

# ==================================================
answer = 0
# Limit = (9^5) * (5-1)
L = (9**5) * (5-1)

for x in range(2, L):
    subAnswer = 0
    xStr = str(x)
    for y in range(0, len(xStr)):
        subAnswer += int(xStr[y]) ** 5

    if subAnswer == x:
        answer += subAnswer

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
