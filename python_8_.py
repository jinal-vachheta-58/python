# 8) Write a python program to find all roots of a quadratic equation.

import cmath
# coefficient of quadratic equation : ax^2 + bx + c = 0
a = float(input("Enter num for a : "))
b = float(input("Enter num for b : "))
c = float(input("Enter num for c : "))

d = (b**2) - (4 * a * c)

root1 = (-b + cmath.sqrt(d) ) / (2 * a)
root2 = (-b - cmath.sqrt(d) ) / (2 * a)

print("root no. 1 : ",root1)
print("root no. 2 : ",root2)

#OUTPUT:
#Enter num for a : 4
#Enter num for b : 5
#Enter num for c : 6
#root no. 1 :  (-0.625+1.0532687216470449j)
#root no. 2 :  (-0.625-1.0532687216470449j)