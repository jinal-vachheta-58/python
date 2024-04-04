# 29) Write a python program to display inverted pyramid of numbers

def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(" ", end="")
        for j in range(0, i):
            print("*", end=" ")
        print()


rows = 5
inverted_pyramid(rows)