import time
import euler
import os

euler.print_problem(22)

start = time.time()

# ==================================================
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
txt_path = os.path.dirname(os.path.realpath(__file__)) + "/Resources/euler022.txt"

file = open(txt_path, "r")
file = file.read().split(',')
names = []
for item in file:
    names.append(item[1:-1])

names = sorted(names)

total_score = 0
for name in names:
    score = 0
    for letter in name:
        score += alphabet.index(letter) + 1

    score *= names.index(name) + 1

    total_score += score


print("The Answer is: %i" % total_score)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
