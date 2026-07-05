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
