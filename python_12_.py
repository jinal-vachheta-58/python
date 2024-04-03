
# 12) Write a python program to generate multiplication table.

""

num = int(input("enter the number for print the table of that"))

for i in range(1,11):
    a=num*i
    print (f"{num} x {i} =",a)
    
    
    
    '''
    output:-
    
    
    enter the number for print the table of that5
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50'''
