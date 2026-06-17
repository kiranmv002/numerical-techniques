import math

# Function to compute Simpson's 1/3 Rule
def simpsons_one_third(x, y, n):
    h = x[1] - x[0]
    if (n - 1) % 2 != 0:
        print("Error: Number of intervals must be even for Simpson's 1/3 Rule!")
        return None
    # Formula: h/3 * [y0 + 4(y1+y3+...) + 2(y2+y4+...) + yn]
    odd_sum  = sum(y[i] for i in range(1, n - 1, 2))
    even_sum = sum(y[i] for i in range(2, n - 1, 2))
    result = (h / 3) * (y[0] + 4 * odd_sum + 2 * even_sum + y[n - 1])
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
result = simpsons_one_third(x, y, n)

print("\nSimpson's 1/3 Rule Table:")
print(f"  {'x':>8}  {'y':>10}  {'Coefficient':>12}")
print("  " + "-" * 35)
for i in range(n):
    if i == 0 or i == n - 1:
        coeff = 1
    elif i % 2 != 0:
        coeff = 4
    else:
        coeff = 2
    print(f"  {x[i]:>8.4f}  {y[i]:>10.4f}  {coeff:>12}")

if result is not None:
    print(f"\nApproximate value of integral = {result}")
    print("Note: Number of intervals must be EVEN.")
