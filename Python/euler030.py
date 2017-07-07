print('''
Problem No. 30
Title:      Digit fifth powers

Problem:    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

                1634 = 14 + 64 + 34 + 44
                8208 = 84 + 24 + 04 + 84
                9474 = 94 + 44 + 74 + 44
                As 1 = 14 is not a sum it is not included.

            The sum of these numbers is 1634 + 8208 + 9474 = 19316.

            Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
''')

import time

start = time.time()

# ==================================================
answer = 0
# Limit = (9^5) * (5-1)
L = (9**5) * (5-1)

for x in range(2, L):
    subAnswer = 0
    xStr = str(x)
    for y in range(0, len(xStr)):
        subAnswer += int(xStr[y]) ** 5

    if subAnswer == x:
        answer += subAnswer

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
