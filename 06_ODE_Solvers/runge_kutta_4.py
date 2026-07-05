# RK4 Method with User Input Function
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
    k1 = h * f(x, y)
    k2 = h * f(x + h, y + k1)
    k3 = h * f(x + h / 2, y + k1 / 2)
    k4 =h * f(x + h / 2, y + k2 / 2)
    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x = x + h
    print(f"{i}\t {x:.4f}\t {y:.4f}")
