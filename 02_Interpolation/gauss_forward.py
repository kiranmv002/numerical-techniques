# Gauss Forward Difference with user input

# Input
n = int(input("Enter number of data points: "))
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

# Build forward difference table
diff = [y.copy()]

for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i - 1][j + 1] - diff[i - 1][j])
    diff.append(temp)

# Display table
print("\nForward Difference Table:")
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(diff[j][i], end="\t")
    print()

# Interpolation
xp = float(input("\nEnter value to interpolate: "))
h = x[1] - x[0]

# Find central index (middle point)
m = n // 2

u = (xp - x[m]) / h

result = y[m]
term = 1

for i in range(1, n):

    if i % 2 != 0:      # odd terms
        k = (i + 1) // 2
        term = term * (u - (k - 1)) / i
        result += term * diff[i][m - (k - 1)]

    else:               # even terms
        k = i // 2
        term = term * (u + (k - 1)) / i
        result += term * diff[i][m - k]

print("\nInterpolated value =", result)
