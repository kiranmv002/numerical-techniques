#finding polynomial, differentiation and estimation
# for equal interval data
from sympy import symbols, diff, expand
n = int(input("Enter number of data points: "))
x = []
y = []
for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))
h = x[1] - x[0] # equal interval
#difference table
diff_table = [y.copy()]
for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff_table[i-1][j+1] - diff_table[i-1][j])
    diff_table.append(temp) # display forward difference table
print("\nForward Difference Table:")
print("-" * 60)
print("x\t y\t Δy\t Δ²y\t Δ³y \t Δ⁴y")
for i in range(n):
    print(x[i], end="")
    for j in range(n - i):
        print(round(diff_table[j][i], 4), end="\t")
    print()
X = symbols('X')
#newton forward polynomial
u = (X - x[0]) / h
poly = y[0]
term = 1
for i in range(1, n):
    term = term * (u - (i - 1)) / i
    poly += term * diff_table[i][0]
poly = expand(poly)
print("\nInterpolation Polynomial:")
print(poly)
#Differentiate polynomaial
dpoly = diff(poly, X)
print("\nDifferentiated Polynomial:")
print(dpoly)
#Estimation 
xp = float(input("\nEnter x value for derivative estimation: "))
value = dpoly.subs(X, xp)
print(f"\nf'({xp}) = {round(float(value),4)}")
