# Modified Euler's Method with User Input Function
# Input the differential equation
func = input("enter dy/dx=")
def f(x,y): 
    return eval(func) 
#input initial values 
x = float(input("Enter initial value of x0: "))
y = float(input("Enter initial value of y0: ")) 
n = int(input("Enter number of steps: "))
h = float(input("Enter step size h: "))
print("\nStep\t x\t\t y")
print(f"0\t {x:.4f}\t {y:.4f}")
for i in range(1, n + 1):
    # Predictor step
    y_predict = y + h * f(x, y)
    # Corrector step
    y = y + (h / 2) * (f(x, y) + f(x + h, y_predict))
    x = x + h
    print(f"{i}\t {x:.4f}\t {y:.4f}")
