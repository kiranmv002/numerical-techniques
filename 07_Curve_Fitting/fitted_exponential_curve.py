# a.bpowerx
import math


# Input
n = int(input("Enter the number of data points: "))

x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x{i+1}: ")))
    y.append(float(input(f"Enter y{i+1}: ")))

# Transform y -> ln(y)
Y = [math.log(val) for val in y]

sumX = sum(x)
sumY = sum(Y)
sumXY = sum(x[i] * Y[i] for i in range(n))
sumX2 = sum(x[i] ** 2 for i in range(n))

# Find B = ln(b)
B = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)

# Find A = ln(a)
A = (sumY - B * sumX) / n

# Convert 
a = math.exp(A)
b = math.exp(B)

print("\na =", round(a, 4))
print("b =", round(b, 4))

print("\nFitted Exponential Curve:")
print("y =", round(a, 4), "* x^", round(b, 4))

# Estimate y
xp = float(input("\nEnter x value to estimate y: "))
y_est = a * (b ** xp)

print("Estimated y =", round(y_est, 4))
