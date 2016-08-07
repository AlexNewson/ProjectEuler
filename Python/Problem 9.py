print('''
Problem No. 9
Title:      Special Pythagorean triplet

Problem:    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

            a^2 + b^2 = c^2
            For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

            There exists exactly one Pythagorean triplet for which a + b + c = 1000.
            Find the product abc.
''')

# A = 200
# B = 375
# C = 425

a = 0
b = 0
c = 0

while a < 998:
    b = 0
    a += 1
    while b < 999:
        c = 0
        b += 1
        while c < 1000:
            c += 1

            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print a
                    print b
                    print c
                    break
