import areaCalculator
from math import *

print("*******************************")
# Task 1. Calculate triangle area
print("Task 1. Calculate triangle area")
try:
    print(" Total area is: ", round(areaCalculator.calculateArea(6, 5, 3), 3))
except Exception as e:
    print(e)

print("*******************************")

# Task 2. Calculate the arithmetic expression
print("Task 2. Calculate the arithmetic expression")
x = 0.34
a = 0.5
numerator = sin(log(x + 1, 3)) + (1.5 * (x ** 3) * exp(-a * x)) + (pow((pow(x, 2) + 4.5 * pow(10, -5)), (1 / 4)))
denominator = pow(cos(x), 1 / 2) * pow(x, 5) - (6 * pow(10, 2.3)) - (pow(abs(a - x), 1 / 5))
print(" Arithmetic expression result: ", numerator / denominator)
print("*******************************")
