import math

# Function to create Divided Difference Table
def divided_difference_table(x, y, n):

    diff = [y.copy()]

    for i in range(1, n):
        temp = []

        for j in range(n - i):

            val = (diff[i - 1][j + 1] - diff[i - 1][j]) / (x[j + i] - x[j])

            temp.append(val)

        diff.append(temp)

    return diff


# Newton's Divided Difference Interpolation
def newton_divided_difference(x, y, xp):

    n = len(x)

    diff = divided_difference_table(x, y, n)

    result = y[0]
    product = 1

    for i in range(1, n):

        product *= (xp - x[i - 1])

        result += product * diff[i][0]

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

xp = float(input("Enter the value of x to interpolate: "))

# Compute interpolated value
result = newton_divided_difference(x, y, xp)

print("\nInterpolated value at x =", xp, "is:", result)
