print('''
Problem No. 16
Title:      Power digit sum

Problem:    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

            What is the sum of the digits of the number 2^1000?
''')

import time

start = time.time()

# ==================================================
number = 2**1000
n = 0

for i in str(number):
    n += int(i)

print("The Answer is: %i" % n)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
