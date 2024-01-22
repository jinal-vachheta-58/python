# Maximum from three numbers in Python
a = int(input("Enter the number1 A : "))
b = int(input("Enter the number2 B : "))
c = int(input("Enter the number2 C : "))

if((a > b) and (a > c)):
    print("A is greater")
elif((b > a) and (b > c)):
    print("B is greater")
else:
    print("C is greater")


# OUTPUT:
# Enter the number1 A : 78
# Enter the number2 B : 45
# Enter the number2 C : 90
# C is greater