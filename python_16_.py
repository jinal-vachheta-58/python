#16) Write a python program to reverse a number.

def reverse_num(num):
    ans = 0
    while(num != 0):
        rem =  num % 10
        ans = ans * 10 + rem
        num = num // 10
    return ans        


num = int(input("Enter the number : "))

result = reverse_num(num)

print("reversed number : ",result)

#OUTPUT:
#    Enter the number : 123456
#    reversed number :  654321
