# Farey Algorithm
from fractions import Fraction
a = 0
b = 1
c = 1
d = 1
num = float(input("Write your number(min: 0, max: 1): "))
itr_num = int(input("Write iteration number(the bigger number means more accurate value): "))

for i in range(itr_num):
    if num > (a + b) / (c + d):
        a += b
        c += d
    elif num < (a + b) / (c + d):
        b += a
        d += c
    elif num == (a + b) / (c + d):
        print("Iterations needed: ", i)
        break

print("Rational approximation", Fraction((a + b), (c + d)))
