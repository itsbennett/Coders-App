# * SIMPLE FUNCTIONS *

# 5.1 - Elements of a function
# A function is a block of reusable code that performs some action.
# You need to know three things about a function:
# - The name of the function
# - The parameters it needs
# - The return value of the function

# 5.1.1 - Function name
# Function names have the same rules as variables.
# Almost all standard functions consists of lowercase letters.
# Usually a function name expresses concisely what the function does.
# When referring to a function, it is convention to use the name() < like so.

# 5.1.2 - Parameters
# Some functions are called with parameters (aka arguments), which may be mandatory.
# You can seperate multiple parameters with commas between them.
# Parameters are teh values that the user assigns to them.

# This must be called with one parameter to work.
int(1)

# The print() function may be called with any number of parameters, which it will display, then go to new line.

# In general, a function cannot change parameters.
x = 1.56
print( int(x) )
print(x)

# When running this code, x is not changed because it was only told to print, not reassign.
# In general, parameters are "passed by value". This means the function does not get access to the actual parameter, but a copy of it.
# Not all data types are "passed by value", but that will be addressed later.

# If a function gets multiple parameters, their order matters.

base = 2
exponent = 3
print( pow( base, exponent) )

# The function pow() gets two parameters, and raises the first to the power of the second.
# If these parameters are mixed you will get a different outcome.

# So what happens when calling a function with parameters that it can't work with?
#   x = pow(3, "2")
#   y = int("two-and-a-half")
# You get a runtime error.

# 5.1.3 - Return value
# If a function retruns a value, that value can be used in your code.
# The function int() returns an interger representation of the parameter it gets.
x = 2.1
y = '3'
z = int(x)
print(z) # since it isn't an int() it prints 2, nonfloating
print( int(y) ) # since it was assigned in a string of '3' it is reverted to floating

# Print is a function that DOES NOT return a value.
print( print("Hello, world!") )
# When running this code, you recieve, literally, 'none', as a response to the value in the function.

# When Python encounters this statement, it must evaluate print(<something>).
# Since <something> is an argument, it starts by evaluating that.
# <something> is actually print(<something_else>).
# <something_else> is the string "Hello, world!", which is not something that needs to be evaluated.
# print() has no return value, so there is nothing Python can use.
# For this Python has a special value called None.

# None is a special value that indicates "no value at all."
# This only indicates that there was nothing to print.
# None is totally different from an empty string ("").
# An empty string still has value, namely a string length of zero.
# None is no string at all, no interger, no float, nothing.


# 5.1.4 - A function is a black box
# The name, parameters and return value are all you need to know when it comes to functions.
# The function might, internally, create variables and do calculations, but they do not have an effect on the rest of your code.

# 5.2 Some basic functions

# 5.2.1 - Type Casting
# - float() has one parameter and returns a floating-point representation of the value of that parameter. i.e. 1 is returned as 1.0.
# - int() has one parameter and returns interger representation of the value of that parameter. i.e. '1.4' is returned as '1'.
