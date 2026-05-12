# Regular Falsi Method

import math

# Function defined using user input
def f(x):
    return eval(func)

func = input("Enter the function f(x): ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
tol = float(input("Enter tol: "))

if f(a) * f(b) >= 0:
    print("Invalid interval. f(a) and f(b) must have opposite signs.")
else:
    print("\nIter\t a\t\t b\t\t c\t\t f(c)")

    i = 1
    c_old = a   # initial value

    while True:
        # Regula Falsi Formula
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(i, "\t", round(a,6), "\t", round(b,6), "\t", round(c,6), "\t", round(f(c),6))

        # Proper stopping condition
        if abs(f(c)) < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        i += 1

    print("\nRoot =", round(c,4))
