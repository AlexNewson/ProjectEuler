import time
import euler

euler.print_problem(35)

start = time.time()

# ==================================================
numbers = []

for i in range(1, 1000000):
    if i not in numbers and euler.is_prime(i):
        if len(str(i)) == 1:
            numbers.append(i)
        else:
            potential = [i]
            i1 = i
            while True:
                i1 = str(i1)[1:]+str(i1)[0]
                if i1[0] == '0':
                    break
                else:
                    i1 = int(i1)
                    if i != i1 and euler.is_prime(i1):
                        potential.append(i1)
                        continue
                    elif i == i1:
                        numbers += potential
                        break
                    else:
                        break
    else:
        continue

answer = len(numbers)

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
