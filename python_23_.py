# 23) Write a python program to check armstrong number. (eg. 13 + 33 + 53 = 153)


def armstrong(num):
    power = len(str(num))
    
    original=num;
    sum=0
    while(num>0):
        digit = num%10
        sum=sum+digit**power
        num=num//10
    if sum == original:
        return ("armstong")
    else:
        return ("not")

num=int(input("number"))

print(armstrong(num))