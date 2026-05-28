import math

def lagrange_interpolation(x, y, xp):
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]

        for j in range(n):
            if j != i:
                term *= (xp - x[j]) / (x[i] - x[j])

        result += term

    return result


n = int(input("Enter the number of data points: "))

x = []
y = []

print("Enter x values:")
for i in range(n):
    x.append(float(input(f"x[{i}]: ")))

print("Enter y values:")
for i in range(n):
    y.append(float(input(f"y[{i}]: ")))

xp = float(input("Enter the value to interpolate: "))

result = lagrange_interpolation(x, y, xp)

print(f"\nThe interpolated value at {xp} is {result}")
