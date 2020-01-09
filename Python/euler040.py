print('''
Problem No. 40
Title:      Champernowne's constant

Problem:    An irrational decimal fraction is created by concatenating the positive integers:

            0.123456789101112131415161718192021...
                         ^            

            It can be seen that the 12th digit of the fractional part is 1.

            If dn represents the nth digit of the fractional part, find the value of the following expression.

            d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

''')

import time

start = time.time()

# ==================================================
s = ""

for i in range(1, 185186):
    s += str(i)

print(len(s))

answer = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
