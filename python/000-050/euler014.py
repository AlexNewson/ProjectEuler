import time
import euler

euler.print_problem(14)
start = time.time()

# ==================================================
high_score = 0
high_number = 0

for i in range(1, 1000000):
    count = 0
    num_start = i
    while i != 1:
        count += 1
        if i % 2 == 0:
            i = i/2
        else:
            i = 3*i + 1

    if count > high_score:
        high_score = count + 1  # For the final number of '1'
        high_number = num_start

print("The Answer is: %i at length %i" % (high_number, high_score))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
