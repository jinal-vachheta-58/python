# 26) Write a python programs to create pyramid and pattern.

num = int(input("enter num"))

for i in range(0,num):
    for j in range(0,num-1-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*" ,end=" ")
    print()