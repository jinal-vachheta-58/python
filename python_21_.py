
# 21) Write a python program to check whether a number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
number = 21
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
    
    
#output :
#    21 is not a prime number