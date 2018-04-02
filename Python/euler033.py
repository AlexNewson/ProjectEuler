print('''
Problem No. 33
Title:      Digit cancelling fractions

Problem:    The fraction 49/8 is a curious fraction, as an inexperienced
            mathematician in attempting to simplify it may incorrectly
            believe that 49/98 = 4/8, which is correct, is obtained by
            cancelling the 9s.

            We shall consider fractions like, 30/50 = 3/5, to be trivial
            examples.

            There are exactly four non-trivial examples of this type of
            fraction, less than one in value, and containing two digits
            in the numerator and denominator.

            If the product of these four fractions is given in its lowest
            common terms, find the value of the denominator.
''')

import time

start = time.time()

# ==================================================
from fractions import Fraction

answer = Fraction(1, 1)
answers = []

# Generate Numerators
for num in range(11, 100):
    numStr = str(num)
    # Eliminate Trivial Numerators e.g. 33/66
    if numStr[0] != numStr[1]:
        # Generate Denominators
        for den in range(num+1, 100):
            denStr = str(den)
            # Emilinate Trival Fractions e.g. 30/50
            if numStr[1] != "0" and denStr[1] != "0":
                #Eliminate Trival Fractions e.g. 32/36
                if numStr[0] != denStr[0]:
                    # Generate Fractions
                    simp = str(Fraction(num, den)).split("/")
                    # Eliminate Non-Cancelled and Trival Fractions
                    if len(simp) == 2 and (len(simp[0]) == 1 and len(simp[1]) == 1):
                        # Compare Numerator and Denominator
                        if numStr[0] == denStr[1]:
                            if int(numStr[1]) / int(denStr[0]) == num / den:
                                answers.append(simp)
                        elif numStr[1] == denStr[0]:
                            if int(numStr[0]) / int(denStr[1]) == num / den:
                                answers.append(simp)

for frac in answers:
    answer *= Fraction(int(frac[0]), int(frac[1]))

print("The Answer is: %i" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
