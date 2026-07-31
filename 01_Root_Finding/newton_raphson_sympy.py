# Newton-Raphson Method using SymPy

import sympy as sp

# Input function
f_str = input("Enter function f(x): ")
x = sp.symbols('x')
f = sp.sympify(f_str)     # convert string to SymPy expression

# Automatic derivative
df = sp.diff(f, x)

def func(val):
    return float(f.subs(x, val))

def dfunc(val):
    return float(df.subs(x, val))

# Input interval and tolerance
a = float(input("Enter interval start a: "))
b = float(input("Enter interval end b: "))
tol = float(input("Enter tolerance: "))

# Check if root exists
if func(a) * func(b) > 0:
    print("No root in this interval")
    exit()

# Initial guess (midpoint)
x0 = (a + b) / 2

print("\nInitial interval: [", a, ",", b, "]")
print("Initial guess x0 =", round(x0, 6))

print("\nIter\t x_n\t\t f(x_n)\t\t x_(n+1)")

i = 1

while True:
    fx = func(x0)
    dfx = dfunc(x0)

    x1 = x0 - fx / dfx

    print(i, "\t", round(x0,6), "\t", round(fx,6), "\t", round(x1,6))

    if abs(x1 - x0) < tol:
        break

    x0 = x1
    i += 1

print("\nApproximate Root =", round(x1,6))
