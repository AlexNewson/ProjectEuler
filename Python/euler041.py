import time
import euler

euler.print_problem(41)
start = time.time()

# ==================================================
from itertools import permutations

answer = 0
a = '123456789'
j = 9
found = False

while not found:
    perm = permutations(a[:j])
    perm = list(perm)[::-1]
    for i in perm:
        number = int(''.join(i))
        if euler.is_prime(number):
            answer = number
            found = True
            break
    j -= 1

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
