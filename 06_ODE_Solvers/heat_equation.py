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
