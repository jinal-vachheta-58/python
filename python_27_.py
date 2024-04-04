# 27) Write a python program to make a simple calculator to add, subtract, multiply or divide


def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Example usage:
num1 = 10
num2 = 5
operation = '+'
result = calculator(num1, num2, operation)
print(f"{num1} {operation} {num2} = {result}")