# Fixed Point Method (Simple Code)

import math
import sympy as sp


# Input functions
f = input("Enter f(x): ")
g = input("Enter g(x): ")

def func(x):
    return eval(f)

def gfunc(x):
    return eval(g)

# Input values
a = float(input("Enter a: "))
b = float(input("Enter b: "))
tol = float(input("Enter tolerance: "))

# Check interval
if func(a) * func(b) > 0:
    print("Root not lies in this interval")
else:
    print("Root lies between", a, "and", b)

# Initial guess
x0 = (a + b) / 2

print("\nIter\t x0\t\t x1\t\t Error")

i = 1

