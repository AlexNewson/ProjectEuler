print('''
Problem No. 5
Title:      Smallest multiple

Problem:    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
            What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
''')

import time

start = time.time()

# ==================================================
notFound = True
number = 0
numberList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
score = 0

while notFound:
    score = 0
    number += 2520

    for x in numberList:
        if number % x == 0:
            score += 1

    if score == 10:
        break

print("The Answer is: %i" % number)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
