import time
import euler

euler.print_problem(37)
start = time.time()

# ==================================================
answer = 0
i = 10
x = 0

while x != 11:
    j = i
    if euler.is_prime((int(str(i)[0]))):
        while True:
            if euler.is_prime(j):
                if len(str(j)) > 1:
                    j = int(str(j)[1:])
                else:
                    j = i
                    while True:
                        if euler.is_prime(j):
                            if len(str(j)) > 1:
                                j = int(str(j)[:-1])
                            else:
                                print("Found! %i" % i)
                                answer += i
                                x += 1
                                i += 1
                                break
                        else:
                            i += 1
                            break
                    break
            else:
                i += 1
                break
    else:
        i += 1


print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
