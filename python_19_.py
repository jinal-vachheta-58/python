#import time

def display_strings_continuously(string1, string2):
    while True:
        print(string1, end=" ")
        print(string2, end="\r")  # "\r" moves the cursor to the beginning of the line
       # time.sleep(1)  # Wait for 1 second before printing the strings again

# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Display the strings continuously
display_strings_continuously(string1, string2)
