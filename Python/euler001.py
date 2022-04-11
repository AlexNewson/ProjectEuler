import time
from euler import print_problem

print_problem(1)
start = time.time()

# ==================================================
x = 0
numbers = []

for x in range(0, 999):
    x += 1
    if x % 3 == 0 or x % 5 == 0:
        numbers.append(x)
    else:
        pass

answer = sum(numbers)
print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
