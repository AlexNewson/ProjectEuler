# -*- coding: utf-8 -*-
print('''
Problem No. 31
Title:      Coin sums

Problem:    In England the currency is made up of pound, £, and pence, p, and
            there are eight coins in general circulation:

                1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

            It is possible to make £2 in the following way:

                1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

            How many different ways can £2 be made using any number of coins?
''')

import time

start = time.time()

# ==================================================
solutions = [0] * 201
solutions[0] = 1
coins = [1, 2, 5, 10, 20, 50, 100, 200]

for x in coins:
    for y in range(x, 201):
        solutions[y] += solutions[y - x]

answer = solutions[200]

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
