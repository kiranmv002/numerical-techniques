import math

# Input
n = int(input("Enter the number of data points: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x: ")))
    y.append(float(input(f"Enter y: ")))

# Transform y to ln(y)
X = x
Y = [math.log(val) for val in y]

# Calculate sums
sumX = sum(X)
sumY = sum(Y)
sumXY = sum(X[i] * Y[i] for i in range(n))
sumX2 = sum(X[i]**2 for i in range(n))

# Find b
b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)

# Find a
A = (sumY - b * sumX) / n
a = math.exp(A)

print("a =", a)
print("b =", b)

print("Fitted exponential curve:")
print("y =", round(a, 4), "* e^(", round(b, 4), "x)")

# Estimate y for user input x value
xp = float(input("Enter a value of x to estimate y: "))
y_est = a * math.exp(b * xp)
print("Estimated y =", round(y_est, 4))
