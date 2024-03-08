# 18) Write a python program to find binary value of a character.

def char_to_binary(char):
    unicode_point = ord(char) # character to ascii code
    binary_value = bin(unicode_point) # ascii code to binary code
    return binary_value

char = input("Enter a character : ")
binary_value = char_to_binary(char)
print("Binary value of", char, "is : ", binary_value)

#OUTPUT:
#    Enter a character : h
#    Binary value of h is :  0b1101000