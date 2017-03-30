print('''
Problem No. 17
Title:      Number letter counts

Problem:    If the numbers 1 to 5 are written out in words: one, two, three,
            four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
            total.

            If all the numbers from 1 to 1000 (one thousand) inclusive were
            written out in words, how many letters would be used?


            NOTE: Do not count spaces or hyphens. For example, 342
            (three hundred and forty-two) contains 23 letters and 115
            (one hundred and fifteen) contains 20 letters. The use of "and"
            when writing out numbers is in compliance with British usage.
''')

import time

start = time.time()

# ==================================================
un = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]  # one two three four five six seven eight nine
te = [3, 6, 6, 5, 5, 5, 7, 6, 6]  # ten twenty thirty forty fifty sixty seventy eighty ninty
an = 3  # and
hu = 7  # hundred
th = 11  # one thousand

teen = [6, 6, 8, 8, 7, 7, 9, 8, 8]  # eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen

countTotal = 0

for i in range(1, 1001):
    if len(str(i)) == 1:
        count = un[int(str(i)[0])]
    elif len(str(i)) == 2:
        if i > 10 and i < 20:
            count = teen[int(str(i)[1]) - 1]
        else:
            count = un[int(str(i)[1])]
            count += te[int(str(i)[0]) - 1]
    elif len(str(i)) == 3:
        if i % 100 > 10 and i % 100 < 20:
            count = teen[int(str(i)[2]) - 1]
            count += an
            count += hu
            count += un[int(str(i)[0])]
        else:
            count = un[int(str(i)[2])]
            if int(str(i)[1]) != 0:
                count += te[int(str(i)[1]) - 1]
            if int(str(i)[1]) == 0 and int(str(i)[2]) == 0:
                count += 0
            else:
                count += an
            count += hu
            count += un[int(str(i)[0])]
    elif len(str(i)) == 4:
        print(th)
        count = th

    countTotal += count

print("The Answer is: %i" % countTotal)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
