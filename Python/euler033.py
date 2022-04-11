import time
from euler import print_problem

print_problem(33)
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

answer = str(answer)

print("The Answer is: %s" % answer)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
