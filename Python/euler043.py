import time
import euler
from itertools import permutations

euler.print_problem(43)
start = time.time()

# ==================================================
answer = 0
a = '0123456789'
mod = [2, 3, 5, 7, 11, 13, 17]

perm = permutations(a)
for i in perm:
    if (int(''.join(i[7:10])) % 17 == 0 and
            int(''.join(i[6:9])) % 13 == 0 and
            int(''.join(i[5:8])) % 11 == 0 and
            int(''.join(i[4:7])) % 7 == 0 and
            int(''.join(i[3:6])) % 5 == 0 and
            int(''.join(i[2:5])) % 3 == 0 and
            int(''.join(i[1:4])) % 2 == 0):
        answer += int("".join(i))


print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
