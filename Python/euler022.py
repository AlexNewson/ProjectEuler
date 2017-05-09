print('''
Problem No. 22
Title:      Names Scores

Problem:    Using euler022.txt, a 46K text file containing over five-thousand
            first names, begin by sorting it into alphabetical order. Then
            working out the alphabetical value for each name, multiply this
            value by its alphabetical position in the list to obtain a name
            score.

            For example, when the list is sorted into alphabetical order,
            COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name
            in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

            What is the total of all the name scores in the file?
''')

import time

start = time.time()

# ==================================================
import os
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
