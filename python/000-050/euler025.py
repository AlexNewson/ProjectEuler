import time
import euler

euler.print_problem(25)
start = time.time()

# ==================================================
x1 = 0
x2 = 1
numbers = []

while len(str(x1)) != 1000:
    numbers.append(x2)
    x3 = x1 + x2
    x1 = x2
    x2 = x3

print("The Answer is: %i" % len(numbers))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
