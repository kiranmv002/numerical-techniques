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

