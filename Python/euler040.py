import time
from euler import print_problem

print_problem(40)
start = time.time()

# ==================================================
s = ""

for i in range(1, 185186):
    s += str(i)

print(len(s))

answer = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
