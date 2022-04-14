import time
import euler

euler.print_problem(38)
start = time.time()

# ==================================================
answer = 0

# Upper limit is 9999 because 10000 10 digit number
for j in range(0, 9999):
    number = ""
    for n in range(1, 5):
        number += str(j * n)
        if len(number) > 9:
            break
        elif len(number) == 9:
            if not euler.is_pandigital(number):
                break
            else:
                numberint = int(number)
                if numberint > answer:
                    answer = numberint
                    break
        else:
            continue


print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
