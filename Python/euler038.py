print('''
Problem No. 38
Title:      Pandigital multiples

Problem:    Take the number 192 and multiply it by each of 1, 2, and 3:

                192 x 1 = 192
                192 x 2 = 384
                192 x 3 = 576

            By concatenating each product we get the 1 to 9 pandigital,
            192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

            The same can be achieved by starting with 9 and multiplying
            by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
            which is the concatenated product of 9 and (1,2,3,4,5).

            What is the largest 1 to 9 pandigital 9-digit number that can be
            formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

''')

import time

start = time.time()

# ==================================================
answer = 0


def isPandigital(y):
    if len(y) == 9:
        x = []
        for i in y:
            if i == "0":
                return False
            elif i in x:
                return False
            x.append(i)
        return True
    else:
        return False


# Upper limit is 9999 because 10000 10 digit number
for j in range(0, 9999):
    number = ""
    for n in range(1, 5):
        number += str(j * n)
        if len(number) > 9:
            break
        elif len(number) == 9:
            if not isPandigital(number):
                break
            else:
                numberint = int(number)
                if numberint > answer:
                    answer = numberint
                    break
        else:
            continue


print(answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
