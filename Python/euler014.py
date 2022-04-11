import time
from euler import print_problem

print_problem(14)
start = time.time()

# ==================================================
highScore = 0
highNumber = 0

for i in range(1, 1000000):
    count = 0
    numStart = i
    while i != 1:
        count += 1
        if i % 2 == 0:
            i = i/2
        else:
            i = 3*i + 1

    if count > highScore:
        highScore = count + 1 # For the final number of '1'
        highNumber = numStart

print("The Answer is: %i at length %i" % (highNumber, highScore))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
