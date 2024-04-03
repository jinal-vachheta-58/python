#20) Write a python program to check whether a number is palindrome or not.



def palindrom(num,revnum):
    if(num == revnum):
        print("palindrom")
    else:
        print("not")
       
        
num = int(input("enter number"))
realnum = num
ans=0
while (num !=0):
    rem =num%10;
    ans = ans *10 +rem
    num=num//10

revnum =ans
       
print(revnum)
#print(realnum,revnum)
palindrom(realnum,revnum)

# output :
#    enter number12321
#    12321
#    palindrom
