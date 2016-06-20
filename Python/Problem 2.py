print('''
Problem No. 2
Title:      Even Fibonacci numbers

Problem:    Each new term in the Fibonacci sequence is generated by adding the previous two terms.
            By starting with 1 and 2, the first 10 terms will be:

            1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

            By considering the terms in the Fibonacci sequence whose values do not exceed four million,
            find the sum of the even-valued terms.

''')

x1 = 0
x2 = 1
numbers = []

while x2 < 4000000:
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    if x2 % 2 == 0:
        numbers.append(x2)
    else:
        pass

print(numbers)
answer = sum(numbers)
print('The Answer is: %i' % answer)