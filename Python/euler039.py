import time
import euler
from collections import Counter

euler.print_problem(39)
start = time.time()

# ==================================================
perimeters = []

for a in range(1, 501):
    for b in range(a, 501):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(a+b+c)

count = Counter(perimeters)

answer = count.most_common(1)[0][0]

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
