import time
import euler

euler.print_problem(2)
start = time.time()

# ==================================================
x1 = 0
x2 = 1
numbers = []

while x2 < 4000000:
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    if x2 % 2 == 0:
        numbers.append(x2)
    else:
        pass

print(numbers)
answer = sum(numbers)
print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
