#15) Write a python program to find lcm.


def gcd(a, b):
    while (b != 0):
        temp = a
        a = b
        b = temp % b
    return a  

def lcm(a, b):
    ans = (a * b) // gcd(a, b)
    return ans

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate GCD
result = lcm(num1, num2)

print("The LCM of", num1, "and", num2, "is", result)

#output:
#Enter first number: 13
#Enter second number: 17
#The GCD of 13 and 17 is 1

