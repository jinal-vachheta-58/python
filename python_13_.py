#13) Write a python program to display fibonacci series. (eg. 0, 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci(n):
    if(n <= 0):
        return []
    elif(n == 1):
        return [0]
    elif(n == 2):
        return [0,1]
    else:
       arr = [0,1]
       a = 0
       b = 1
       for x in range(2,n):
           temp = a
           a=b
           b = temp+b
           arr.append(b)
       return arr
       


n = int(input("Enter the number of terms in fibonacci : "))

f_arr = fibonacci(n);
print(f_arr)

#OUTPUT:
#    Enter the number of terms in fibonacci : 8
#    [0, 1, 1, 2, 3, 5, 8, 13]
