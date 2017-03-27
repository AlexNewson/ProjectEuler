print('''
Problem No. 15
Title:      Lattice paths

Problem:    Starting in the top left corner of a 2x2 grid, and only being able
            to move to the right and down, there are exactly 6 routes to the
            bottom right corner.

            How many such routes are there through a 20x20 grid?
''')

import time
from math import factorial as f

start = time.time()

# ==================================================
# Using the Combination formula of 20 Right moves and
# a total of 40 moves, we can calculate the number of
# possible paths:
m = 40
r = 20

answer = (f(m))/(f(r)*f(m-r))
print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
