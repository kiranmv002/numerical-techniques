import math

# Central Difference - First Derivative
def central_first_derivative(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    idx = x.index(xp)
    # Formula: (y[i+1] - y[i-1]) / 2h
    dy = (y[idx + 1] - y[idx - 1]) / (2 * h)
    return dy

# Central Difference - Second Derivative
def central_second_derivative(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    idx = x.index(xp)
    # Formula: (y[i+1] - 2*y[i] + y[i-1]) / h^2
    d2y = (y[idx + 1] - 2 * y[idx] + y[idx - 1]) / (h ** 2)
    return d2y

# --------------------------------
# USER INPUT SECTION
# --------------------------------
n = int(input("Enter number of data points: "))
x = []
y = []
print("Enter x values:")
for i in range(n):
    x.append(float(input(f"x[{i}] = ")))
print("Enter y values:")
for i in range(n):
    y.append(float(input(f"y[{i}] = ")))

xp = float(input("Enter the value of x to differentiate at (must be an interior point): "))

# Validate interior point
idx = x.index(xp)
if idx == 0 or idx == n - 1:
    print("Error: Central difference requires an interior point (not first or last).")
else:
    dy  = central_first_derivative(x, y, xp)
    d2y = central_second_derivative(x, y, xp)

    print(f"\nFirst Derivative  dy/dx   at x = {xp} is: {dy}")
    print(f"Second Derivative d²y/dx² at x = {xp} is: {d2y}")
    print("\nNote: Central difference is more accurate than forward/backward.")
