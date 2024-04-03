# 24) Write a python program to display armstrong number between two intervals.


def armstrong(num):

    power = len(str(num))
    
    original=num
    sum=0
    while(num>0):
        digit = num%10
        sum=sum+digit**power
        num//=  10
    return sum == original


def range_A(s,e):
    armstrong_n=[]
    for num in range(s,e+1):
        if armstrong(num):
            armstrong_n.append(num)
    return armstrong_n
    
s= int (input("s"))
e= int(input("e"))

print(range_A(s, e))