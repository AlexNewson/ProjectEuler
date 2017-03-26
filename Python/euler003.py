print('''
Problem No. 3
Title:      Largest prime factor

Problem:    The prime factors of 13195 are 5, 7, 13 and 29.
            What is the largest prime factor of the number 600851475143 ?
''')

import time

start = time.time()

# ==================================================
x = 600851475143

factors = []
loop = 2

while loop <= x:
    if x % loop == 0:
        x /= loop
        factors.append(loop)
    else:
        loop += 1

print("The Answer is: %i" % max(factors))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
