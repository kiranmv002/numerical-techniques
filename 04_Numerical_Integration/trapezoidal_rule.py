import math

# Function to compute Trapezoidal Rule
def trapezoidal(x, y, n):
    h = x[1] - x[0]
    # Formula: h/2 * [y0 + 2(y1+y2+...+yn-1) + yn]
    middle_sum = sum(y[i] for i in range(1, n - 1))
    result = (h / 2) * (y[0] + 2 * middle_sum + y[n - 1])
    return result

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

# Compute integral
