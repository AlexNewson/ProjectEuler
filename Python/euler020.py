print('''
Problem No. 20
Title:      Factorial digit sum

Problem:    n! means n x (n - 1) x ... x 3 x 2 x 1

            For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
            and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

            Find the sum of the digits in the number 100!
''')

import time
from math import factorial as f

start = time.time()

# ==================================================
print("The Answer is: %i" % sum([int(digit) for digit in str(f(100))]))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
