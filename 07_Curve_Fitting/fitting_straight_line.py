import math
# Input
n = int(input("Enter the number of data points: "))
x = []
y = [] 
for i in range(n):
    x.append(float(input(f"Enter x : ")))
    y.append(float(input(f"Enter y: ")))

sumX = sum(x)
sumY = sum(y)   
sumXY = sum(x[i] * y[i] for i in range(n))
sumX2 = sum(x[i]**2 for i in range(n))

# Find b
b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)
# Find a
a = (sumY - b * sumX) / n

print("a =", a)
print("b =", b)
print("\nFitted Straight Line:")
print("y =", round(a, 4), "* x^", round(b, 4))

# Estimate y for a given x
x_val = float(input("\nEnter x value to estimate y: "))
y_est = a + b * x_val
print("Estimated y =", round(y_est, 4))
