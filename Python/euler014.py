print('''
Problem No. 14
Title:      Longest Collatz sequence

Problem:    The following iterative sequence is defined for the set of positive integers:

                n > n/2 (n is even)
                n > 3n + 1 (n is odd)

            Using the rule above and starting with 13, we generate the following sequence:

                    13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

            It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
            Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

            Which starting number, under one million, produces the longest chain?

            NOTE: Once the chain starts the terms are allowed to go above one million.
''')

import time

start = time.time()

# ==================================================
highScore = 0
highNumber = 0

for i in range(1, 1000000):
    count = 0
    numStart = i
    while i != 1:
        count += 1
        if i % 2 == 0:
            i = i/2
        else:
            i = 3*i + 1

    if count > highScore:
        highScore = count + 1 # For the final number of '1'
        highNumber = numStart

print("The Answer is: %i at length %i" % (highNumber, highScore))
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
