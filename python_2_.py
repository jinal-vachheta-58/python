# write a program for find quotient and reminder

def find_quotient(x,y):
    return x//y

def find_reminder(x,y):
    return x%y


x = int(input("enter first number : "))
y = int(input("enter second number : "))

result = find_quotient(x,y)
print("quotient of x and y = ",result)

result = find_reminder(x,y)
print("reminder of x and y = ",result)

# output:
# PS C:\Users\rcc\Desktop\python assignment> python python_2_.py
# enter first number : 5
# enter second number : 5
# quotient of x and y =  1
# reminder of x and y =  0