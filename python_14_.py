
#14) Write a python program to find gcd.


def gcd(num1, num2):
    if(num2==0):
        return num1
    else:
        return gcd(num2 , num1%num2)
    
num1= int(input("enter num"))
num2= int(input("enter num"))

print(gcd(num1,num2))

lcm = (num1*num2) // gcd(num1, num2)
print (lcm)

#output:
#    enter num7
#    enter num13
#    1
#    91