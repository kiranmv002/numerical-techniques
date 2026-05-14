import math

f = input("Enter the function f(x): ")

def func(x):
    return eval(f)

x0 = float(input("Enter x0: "))
x1 = float(input("Enter x1: "))
tol = float(input("Enter tolerance: "))

print("\nIter\t x0\t\t x1\t\t x2\t\t f(x2)")

i = 1

while True:
    x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))

    print(i, "\t", round(x0,6), "\t", round(x1,6), "\t", round(x2,6), "\t", round(func(x2),6))

    if abs(func(x2)) < tol:
        break

    x0 = x1
    x1 = x2
    i += 1

print("\nApproximate root =", round(x2,6))
