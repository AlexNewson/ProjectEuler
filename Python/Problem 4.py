print('''
Problem No. 4
Title:      Largest palindrome product

Problem:    A palindromic number reads the same both ways.
            The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
            Find the largest palindrome made from the product of two 3-digit numbers.
''')

import time

start = time.time()

# ==================================================
x1 = 999
x2 = 999
found = False

while not found:
    number = x1 * x2
    if str(number) == str(number)[::-1]:
        print(str(number))
        found = True
    else:
        pass
    x1 -= 1

    number = x1 * x2
    if str(number) == str(number)[::-1]:
        print(str(number))
        found = True
    else:
        pass
    x2 -= 1
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
