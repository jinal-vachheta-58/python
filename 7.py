# Python Variables - Assign Multiple Values

x,y,z = "jinal","aasima","priyanka"
print(x)
print(y)
print(z)

# output:
# jinal
# aasima
# priyanka

# ________________________________________________
# One Value to Multiple Variables
x = y = z = "jinal"
print(x)
print(y)
print(z)

# output:
# jinal
# jinal
# jinal

# ________________________________________________
# join output using comma in print() function
x = "jinal"
y = "vachheta"
z = "p."
print(x,y,z) # (,)comma operator provides automatic space
print(x+y+z) # (+)plus operator don't provide automatic space

# output:
# jinal vachheta p.
# jinalvachhetap.

# ________________________________________________
# block scope in python

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) # inside function

myfunc()

print("Python is " + x) # outside function

# output:
# Python is fantastic
# Python is awesome

# ________________________________________________
# use of global keyword to make variables global
def myfunc():
  global x
  x = "lovely"

myfunc()

print("Python is " + x)

# output:
# Python is lovely

# ________________________________________________