import time
from euler import print_problem

print_problem(4)
start = time.time()

# ==================================================
x1 = 999
x2 = 999
found = False

while not found:
    number = x1 * x2
    if str(number) == str(number)[::-1]:
        print("The Answer is: %i" % number)
        found = True
    else:
        pass
    x1 -= 1

    number = x1 * x2
    if str(number) == str(number)[::-1]:
        print("The Answer is: %i" % number)
        found = True
    else:
        pass
    x2 -= 1
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
