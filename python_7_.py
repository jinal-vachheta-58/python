#7) Write a python program to find largest number among three numbers

a = int(input("Enter num for a : "))
b = int(input("Enter num for b : "))
c = int(input("Enter num for c : "))

if(a > b and a > c):
    print(a," : a is greater")
elif(b > a and b > c):
    print(b," : b is greater")
else:
    print(c," : c is greater")

#OUTPUT:
#Enter num for a : 8
#Enter num for b : 6
#Enter num for c : 45
#45  : c is greater