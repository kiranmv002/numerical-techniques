# Laplace Equcation using Liebmann Iteration
# Boundary values are given as functions
import math
# Number of interior points
n = int(input("Enter number of interior points n: "))
# Step size
h = float(input("Enter step size h: "))
# Create grid
u = [[0.0 for j in range(n + 2)] for i in range(n + 2)]
# Boundary functions
top = input("Enter top boundary function f(x): ")
bottom = input("Enter bottom boundary function f(x): ")
left = input("Enter left boundary function f(y): ")
right = input("Enter right boundary function f(y): ")
# Assign boundary values
for j in range(n + 2):
    x = j * h
    u[0][j] = eval(top)
    u[n + 1][j] = eval(bottom)
for i in range(n + 2):
    y = i * h
    u[i][0] = eval(left)
    u[i][n + 1] = eval(right)
# Intial guess
guess = float(input("Enter initial guess for interior points: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        u[i][j] = guess
# Number of iterations
itr = int(input("Enter number of iterations: "))
# Liebmann Iteration
for k in range(itr):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            u[i][j] = 0.25 * (u[i - 1][j] + u[i + 1][j] + u[i][j - 1] + u[i][j + 1]) /4
