# 28) Write a python program to display Simple Number Triangle Pattern


n = int(input("enter num"))
num=1;
for i in range(1, n+1):
    for j in range(1,i+1):
        print(num, end=" ")
        num =num+1
    print()
