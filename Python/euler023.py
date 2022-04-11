import time
from euler import print_problem

print_problem(23)
start = time.time()

# ==================================================
from functools import reduce
abundants = set()
answer = 0

def d(n):
    return sum(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) - n


for i in range(1, 28123):
    if d(i) > i:
        abundants.add(i)
    if not any((i - a in abundants) for a in abundants):
        answer += i

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
