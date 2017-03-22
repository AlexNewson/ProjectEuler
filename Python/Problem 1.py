print('''
Problem No. 1
Title:      Multiples of 3 and 5

Problem:    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
            The sum of these multiples is 23.
            Find the sum of all the multiples of 3 or 5 below 1000.
''')
import time

start = time.time()

# ==================================================
x = 0
numbers = []

for x in range(0, 999):
    x += 1
    if x % 3 == 0 or x % 5 == 0:
        numbers.append(x)
    else:
        pass

answer = sum(numbers)
print('The Answer is: %i' % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
