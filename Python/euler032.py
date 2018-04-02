print('''
Problem No. 32
Title:      Pandigital Products

Problem:    We shall say that an n-digit number is pandigital if it makes use
            of all the digits 1 to n exactly once; for example, the 5-digit
            number, 15234, is 1 through 5 pandigital.

            The product 7254 is unusual, as the identity, 39 x 186 = 7254,
            containing multiplicand, multiplier, and product is 1 through 9
            pandigital.

            Find the sum of all products whose multiplicand/multiplier/product
            identity can be written as a 1 through 9 pandigital.
''')

import time

start = time.time()

# ==================================================
from itertools import permutations

answer = 0
answers = set([])

numbers = "123456789"
permList = list(permutations(numbers))
permNumbers = []

for seq in permList:
    number = ""
    for i in seq:
       number += str(i)
    permNumbers.append(number)

for number in permNumbers:
    for x in range(len(number)):
        s1 = number[:x+1]
        sN = number[x+1:]
        for y in range(len(sN)-1):
            s2 = sN[:y+1]
            s3 = sN[y+1:]
            if (int(s1)*int(s2)) == int(s3):
                answers.add(int(s3))

answer = sum(answers)

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
