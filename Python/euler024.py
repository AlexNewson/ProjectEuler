import time
import euler

euler.print_problem(24)
start = time.time()

# ==================================================
from itertools import permutations

perms = [''.join(p) for p in permutations('0123456789')]
perms = sorted(perms)

print("The Answer is: %s" % perms[999999])
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
