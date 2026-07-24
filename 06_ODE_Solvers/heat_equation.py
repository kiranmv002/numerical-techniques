# One-Dimensional Heat Equation
# Bender-Schmidt Method
# Boundary and Initial Conditions as Functions
import math
# Input
L = float(input("Enter length of rod: "))
h = float(input("Enter space step (h): "))
m = int(input("Enter number of time steps: "))
# Number of intervals
n = int(L / h)
# User-defined functions
f = input("Enter initial condition f(x): ")
left = input("Enter left boundary function L(t): ")
right = input("Enter right boundary function R(t): ")
# Initial values
u = []
for i in range(n + 1):
    x = i * h
    u.append(eval(f))
print("\nInitial Values")
print(u)
# Time iterations
for j in range(1, m + 1):
    new = u.copy()
    t = j      # or t = j*k if k is specified
    # Boundary values
    new[0] = eval(left)
    new[n] = eval(right)
    # Interior points
    for i in range(1, n):
        new[i] = (u[i - 1] + u[i + 1]) / 2
    u = new
    print("\nTime Step", j)
    print([round(value, 4) for value in u])
