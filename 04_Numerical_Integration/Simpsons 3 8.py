import math

# Function to compute Simpson's 3/8 Rule
def simpsons_three_eighth(x, y, n):
    h = x[1] - x[0]
    if (n - 1) % 3 != 0:
        print("Error: Number of intervals must be multiple of 3 for Simpson's 3/8 Rule!")
        return None
    # Formula: 3h/8 * [y0 + 3(y1+y2+y4+y5+...) + 2(y3+y6+...) + yn]
    total = y[0] + y[n - 1]
    for i in range(1, n - 1):
        if i % 3 == 0:
            total += 2 * y[i]
        else:
            total += 3 * y[i]
    result = (3 * h / 8) * total
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
result = simpsons_three_eighth(x, y, n)

print("\nSimpson's 3/8 Rule Table:")
print(f"  {'x':>8}  {'y':>10}  {'Coefficient':>12}")
print("  " + "-" * 35)
for i in range(n):
    if i == 0 or i == n - 1:
        coeff = 1
    elif i % 3 == 0:
        coeff = 2
    else:
        coeff = 3
    print(f"  {x[i]:>8.4f}  {y[i]:>10.4f}  {coeff:>12}")

if result is not None:
    print(f"\nApproximate value of integral = {result}")
    print("Note: Number of intervals must be a MULTIPLE OF 3.")
