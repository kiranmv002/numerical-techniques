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

