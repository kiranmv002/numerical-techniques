import math

# Function to compute Forward Difference Table
def forward_difference_table(y, n):
    diff = [y.copy()]
    for i in range(1, n):
        temp = []
        for j in range(n - i):
            val = diff[i - 1][j + 1] - diff[i - 1][j]
            temp.append(val)
        diff.append(temp)
    return diff

# Forward Difference - First Derivative
def forward_first_derivative(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    diff = forward_difference_table(y, n)
    # Find index of xp
    idx = x.index(xp)
    p = (xp - x[0]) / h
    dy = (1 / h) * (diff[1][idx] - (1/2)*diff[2][idx] + (1/3)*diff[3][idx] if len(diff) > 3 else diff[1][idx])
    return dy

# Forward Difference - Second Derivative
def forward_second_derivative(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    diff = forward_difference_table(y, n)
    idx = x.index(xp)
    d2y = (1 / h**2) * (diff[2][idx] - diff[3][idx] if len(diff) > 3 else diff[2][idx])
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
diff = forward_difference_table(y, n)
idx = x.index(xp)
