# 30) Write a python program to display inverted pyramid of descending numbers
def inverted_descending_pyramid(rows):
    num = 1
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(" ", end="")
        for j in range(0, i):
            print(num, end=" ")
            num += 1
        print()


rows = 5
inverted_descending_pyramid(rows)