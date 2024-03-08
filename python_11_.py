#11) Write a python program to find factorial.
def find_factorial(n):
    if(n == 0):
        return 1
    else:
        return n * find_factorial(n-1) 

n = int(input("Enter number : "))

result = find_factorial(n)

print("factorial of ",n," is : ",result)

#OUTPUT:
#Enter number : 5
#factorial of  5  is :  120