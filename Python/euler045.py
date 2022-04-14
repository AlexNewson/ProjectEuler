import time
import euler

euler.print_problem(45)
start = time.time()

# ==================================================
i = 144

while True:
    hexagon = euler.generate_hexagonal(i)
    if euler.is_pentagonal(hexagon):
        break
    i += 1


print("The Answer is: %i" % hexagon)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
