'''
i = 1

while(i <= 5):
    j = 1
    while(j <= i):
        print(j,end="")
        j = j+1
    print()
    i = i+1
'''
'''
1
12
123
1234
12345
'''

'''
12345
1234
123
12
1

'''
'''
i = 5

while(i >= 1):
    j = 1
    while(j <= i):
        print(j,end="")
        j = j+1
    print()
    i = i-1
'''
'''
1
2 3
4 5 6
7 8 9 10
11 12 13

'''
'''
i = 1
k = 1
while(i <= 5):
    j = 1
    while(j <= i):
        print(k,end=" ")
        j = j+1
        k= k+1
    print()
    i = i+1
'''
'''
1
3 5
7 9 11
13 15 17 19
'''
'''
i = 1
k = 2
while(i <= 5):
    j = 1
    while(j <= i):
        print(k,end=" ")
        j = j+1
        k= k+2
    print()
    i = i+1
'''


'''
    1
   12
  123
 1234
12345
'''
'''
i = 1

while(i <= 5):
    k = 5
    while(k >= i):
        print(" ",end="")
        k = k-1
    j = 1
    while(j <= i):
        print(j,end="")
        j = j+1
    print()

    i = i+1


'''
'''
10
9 10
8 9 10
7 8 9 10 
6 7 8 9 10
'''
'''
i = 10
while(i >= 6):
    j = i
    while(j <= 10):
        print(j,end=" ")
        j = j+1
    print()
    i = i-1
'''

'''
1 2 3 4 5 
6 7 8 9 
   10 11 12 
    13 14 
     15
     

12345
1234
123
12
1

i = 5
x = 1
while(i >= 1):
    k = 5
    while(k >= i):
        print(" ",end="")
        k= k+1
    j = 1
    while(j <= i):
        print(j,end=" ")
        j = j+1
        x= x+1
    print()
    i = i-1
'''

n1 =12
n2 = 64
g = 0
lcm = 0
if( n1 > n2):
    g = n1
else :
    g = n2
while(True):
    if(g % n1 == 0) and g % n2 == 0:
        lcm  = g
        break
    g = g+1
    
print(lcm)
print("hello")
    
    



