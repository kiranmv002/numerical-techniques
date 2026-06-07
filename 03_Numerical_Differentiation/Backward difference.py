import math

# Function to compute Backward Difference Table
def backward_difference_table(y, n):
    diff = [y.copy()]
    for i in range(1, n):
        temp = []
        for j in range(n - i):
            val = diff[i - 1][j + 1] - diff[i - 1][j]
            temp.append(val)
        diff.append(temp)
    return diff

# Backward Difference - First Derivative
def backward_first_derivative(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    diff = backward_difference_table(y, n)
    idx = x.index(xp)
    # Use last point (backward from xp)
    i = idx
    dy = (1 / h) * (diff[1][i - 1] + (1/2)*diff[2][i - 2] + (1/3)*diff[3][i - 3]) if n > 3 else (1 / h) * diff[1][i - 1]
    return dy

# Backward Difference - Second Derivative
def backward_second_derivative(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    diff = backward_difference_table(y, n)
    idx = x.index(xp)
    i = idx
    d2y = (1 / h**2) * (diff[2][i - 2] + diff[3][i - 3]) if n > 3 else (1 / h**2) * diff[2][i - 2]
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

xp = float(input("Enter the value of x to differentiate at: "))

h = x[1] - x[0]
diff = backward_difference_table(y, n)
idx = x.index(xp)
i = idx

# First Derivative
dy = (1 / h) * (diff[1][i - 1] + (1/2)*diff[2][i - 2] + (1/3)*diff[3][i - 3]) if n > 3 else (1 / h) * diff[1][i - 1]

# Second Derivative
d2y = (1 / h**2) * (diff[2][i - 2] + diff[3][i - 3]) if n > 3 else (1 / h**2) * diff[2][i - 2]

print("\nBackward Difference Table:")
for i, row in enumerate(diff):
    print(f"  Delta^{i}y: {row}")

print(f"\nFirst Derivative  dy/dx  at x = {xp} is: {dy}")
print(f"Second Derivative d²y/dx² at x = {xp} is: {d2y}")
