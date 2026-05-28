# Stirling's Interpolation with user input

# Input
n = int(input("Enter number of data points (prefer odd): "))
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

# Build forward difference table
diff = [y.copy()]

for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i-1][j+1] - diff[i-1][j])
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

# Central index
m = n // 2
u = (xp - x[m]) / h
result = y[m]

# Stirling formula terms
term1 = u * (diff[1][m-1] + diff[1][m]) / 2
result += term1

term2 = (u*u / 2) * diff[2][m-1]
result += term2

term3 = (u*(u*u - 1) / 6) * (diff[3][m-2] + diff[3][m-1]) / 2
result += term3

term4 = (u*u*(u*u - 1) / 24) * diff[4][m-2]
result += term4

print("\nInterpolated value =", result)
