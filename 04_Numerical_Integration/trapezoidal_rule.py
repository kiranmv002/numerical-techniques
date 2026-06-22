# Trapezoidal Rule with User Input Function and Table Display
import math
# Input function
expr = input("Enter function f(x): ")
# Input limits and number of subintervals
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals n: "))
# Function evaluator
def f(x):
    return eval(expr, {"x": x, "math": math})
# Calculate step size
h = (b - a) / n
# Generate x values and corresponding f(x) values
x = []
fx = []
for i in range(n + 1):
    xi = a + i * h
    x.append(xi)
    fx.append(f(xi))
# Display table
print("\nTRAPEZOIDAL RULE TABLE")
print("-" * 40)
print(f"{'i':<5}{'x':<15}{'f(x)':<15}")
print("-" * 40)
for i in range(n + 1):
    print(f"{i:<5}{x[i]:<15.4f}{fx[i]:<15.4f}")
# Compute integral
s = fx[0] + fx[n]
for i in range(1, n):
    s += 2 * fx[i]
I = (h / 2) * s
# Display result
print("\nFormula:")
print("I = (h/2) * [f(x0) + 2*f(x1) + 2*f(x2) + ... + 2*f(x(n-1)) + f(xn)]")
print("\nStep size h =", round(h, 4))
print("Approximate integral =", round(I, 6))
