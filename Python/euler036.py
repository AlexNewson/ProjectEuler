print('''
Problem No. 36
Title:      Double-base palindromes

Problem:    The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

            Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
            
            (Please note that the palindromic number, in either base, may not include leading zeros.)
''')

import time

start = time.time()

# ==================================================
answer = 0

for i in range(0, 1000001):
    if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
        answer += i

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
