print('''
Problem No. 42
Title:      Coded triangle numbers

Problem:    The nth term of the sequence of triangle numbers is given by,
            tn = ½n(n+1); so the first ten triangle numbers are:

            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

            By converting each letter in a word to a number corresponding to
            its alphabetical position and adding these values we form a word
            value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
            If the word value is a triangle number then we shall call the word a triangle word.
            
            Using euler042.txt, a 16K text file containing nearly two-thousand common
            English words, how many are triangle words?
''')

import time

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
