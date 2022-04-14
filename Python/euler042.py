import time
import euler

euler.print_problem(42)
start = time.time()

# ==================================================
answer = 0
tnumbers = []

# Generate 30 triangle numbers
for n in range(1, 31):
    tnumbers.append(int(0.5*n*(n+1)))

with open('./Resources/euler042.txt', 'r') as file:
    words = file.readline().replace("\"", "").split(",")

for word in words:
    wordvalue = 0
    for char in word:
        wordvalue += ord(char) - 64
    if wordvalue in tnumbers:
        answer += 1

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
