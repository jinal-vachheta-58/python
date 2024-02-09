# Built-in Data Types

# Text Type       :	    str
# Numeric Types   :	    int, float, complex
# Sequence Types  :	    list, tuple, range
# Mapping Type    :	    dict
# Set Types       :	    set, frozenset
# Boolean Type    :	    bool
# Binary Types    :	    bytes, bytearray, memoryview
# None Type       :	    NoneType
# __________________________________

# string

x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# __________________________________

# int

x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# __________________________________

# float

x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# __________________________________

# complex

x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# __________________________________
# list

x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# __________________________________
# tuple

x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# __________________________________

# range

x = range(6)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# __________________________________

# dictionary same as object

x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# __________________________________

# set {}

x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# __________________________________

# frozenset  ({})

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 


# __________________________________
# nonetype

x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# __________________________________


# OUTPUT:
# PS C:\Users\rcc\Desktop\python assignment> python python_3_.py
# Hello World
# <class 'str'>

# 20
# <class 'int'>

# 20.5
# <class 'float'>

# 1j
# <class 'complex'>

# ['apple', 'banana', 'cherry']
# <class 'list'>

# ['apple', 'banana', 'cherry']
# <class 'list'>

# range(0, 6)
# <class 'range'>

# {'name': 'John', 'age': 36}
# <class 'dict'>

# {'banana', 'cherry', 'apple'}
# <class 'set'>

# frozenset({'banana', 'cherry', 'apple'})
# <class 'frozenset'>

# None
# <class 'NoneType'>