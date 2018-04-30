print('''
Problem No. 34
Title:      Digit factorials

Problem:    145 is a curious number, as
            1! + 4! + 5! = 1 + 24 + 120 = 145

            Find the sum of all numbers which are equal
            to the sum of the factorial of their digits.

            Note: as 1! = 1 and 2! = 2 are not sums,
            they are not included.
''')

import time

start = time.time()

# ==================================================
from math import factorial as f

answer = 0

for x in range(3, 2540160):
    y = 0
    for d in str(x):
        y += f(int(d))
    if y == x:
        print(x)
        answer += x

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
