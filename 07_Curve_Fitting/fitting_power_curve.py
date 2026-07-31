import math
# Input
n = int(input("Enter the number of data points: "))
x = []
y = [] 
for i in range(n):
    x.append(float(input(f"Enter x : ")))
    y.append(float(input(f"Enter y: ")))
# Transform values

X = [math.log(val) for val in x]
Y = [math.log(val) for val in y]    
# Calculate sums
sumX = sum(X)
sumY = sum(Y)   
sumXY = sum(X[i] * Y[i] for i in range(n))
sumX2 = sum(X[i]**2 for i in range(n))

