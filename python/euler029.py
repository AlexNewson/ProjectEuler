import time
import euler

euler.print_problem(29)
start = time.time()

# ==================================================
terms = set([])

for a in range(2, 101):
    for b in range(2, 101):
        x = a ** b
        terms.add(x)

answer = len(list(terms))

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
