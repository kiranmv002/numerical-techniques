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

