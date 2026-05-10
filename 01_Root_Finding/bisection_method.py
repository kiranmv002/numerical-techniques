# Bisection Method 

import math

# Function defined using user input
def f(x):
    return eval(func)

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return

    print("Iter\t a\t\t b\t\t c\t\t f(c)")

    iteration = 1
    c = 0

    while (b - a) / 2 > tol:
        c = (a + b) / 2

        print(iteration, "\t", round(a,6), "\t", round(b,6), "\t", round(c,6), "\t", round(f(c),6))

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteration += 1

    print("\nApproximate root =", round(c,6))


# -------- User Input --------
func = input("Enter the function f(x): ")
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
tol = float(input("Enter tolerance: "))

bisection(a, b, tol)
