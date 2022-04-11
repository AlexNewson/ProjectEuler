import time
from euler import print_problem

print_problem(32)
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
