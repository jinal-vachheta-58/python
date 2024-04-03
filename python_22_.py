
# 22) Write a python program to display prime numbers between two intervals.

def prime_numbers_interval(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers

# Example usage:
start = 10
end = 50
print(f"Prime numbers between {start} and {end} are:", prime_numbers_interval(start, end))