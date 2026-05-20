# Newton Backward Difference with user input

# Input
n = int(input("Enter number of data points: "))
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

# Build backward difference table
diff = [y.copy()]

for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i-1][j+1] - diff[i-1][j])
    diff.append(temp)

# Display table
print("\nBackward Difference Table:")
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(diff[j][i], end="\t")
    print()

# Interpolation
xp = float(input("\nEnter value to interpolate: "))
h = x[1] - x[0]
p = (xp - x[n-1]) / h   # backward u

result = y[n-1]
term = 1

for i in range(1, n):
    term = term * (p + (i - 1)) / i
    result += term * diff[i][n - i - 1]

print("\nInterpolated value =", result)
