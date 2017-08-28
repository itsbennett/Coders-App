# * VARIABLES *
# 4.1 - Variables and Values

# A variable lets you store a value, whether a string or interger, to a label.
x = 5
print(x)
# Giving x the value of 5 is called an assignment.

# Exercise: Assign how many seconds in a week to a variable and call it.
# Wow, almost like I did this already... 🤔
d = 7
s = 86400
print( d*s )

# When assigning a variable it is possible to overwrite it in the future with another function. When a variable is overwritten it will hold the last known value that it was given.

x = 5
print(x)
x = 7*9*13 # overwrite previous value of X
print(x)
x = "A nod\'s as good as a wink to a blind bat."
print(x)

# Once a variable has a value it can be used where you'd otherwise use values.
x = 2
y = 3
print("x =", x)
print("y =", y)
print("x*y =", x*y)
print("x+y =", x+y)

# You can copy the contents of one var to another using assignment operator.
x = 2
y = 3
print("x =", x, "and y =", y)

z = x
print(x)
x = x+3
print(x)

# A variable MUST be created before used. Running this will result in an error:
# print(days_in_a_year)
days_in_a_year=365
# NameError: name 'days_in_a_year' is not defined

# 4.2 - Variable Names
# !! A variable name must consist of only:
# - Letters (Upper or lower, IS CASE SENSITIVE)
# - Digits
# - _ (Underscores)
# !! A variable name should not be a reserved word (keywords), which are:
# - False, None, True, and, as, assert, break
# - class, continuem, def, del, elif, else, except
# - finally, for, from, global, if, import, in
# - is, lambda, nonlocal, not, or, pass, raise
# - return, try, while, with, yield

a = 3.14159265
b = 7.5
c = 8.25
d = a*b*c / 3
print(d)

# This code calculates the volume of the cone and exhibits the importance of naming variables.
# If you were asked to change a portion of the volume of the cone, which one would you know to change?

pi = 3.14159265
radius = 7.5
height = 8.25
volume = pi*radius*height / 3
print(volume)

# This is much easier to interpret and explicitately states which variable is which. This is helpful to the programmer as well as others who would be reading the code.

# 4.2.2 - Practicing with variable names
# Exercise: Determine which of these variable names are legal or illegal.
classification = 1 # legal
Classification = 1 # legal
# cl@ssification = 1 # illegal, contains a symbol
classif1cat10n = 1 # legal
# 1classification = 1 # illegal, starts with a digit
_classification = 1 # legal
# class = 1 # illegal, reserved keyword
Class = 1 # legal, but not good as it uses a keyword as a name

# 4.2.3 - Constants
# Constants are values that are assigned to a variable that cannot be changed.
# A constant is typically written in ALL CAPS.

# Without constants
total = 24.95
final_total = int(100*total*1.15 / 100)
print(final_total)

# With Constants
SERVICE_CHARGE = 1.15
CENTS = 100
total = 24.95
final_total = int(CENTS*total*SERVICE_CHARGE) / CENTS
print(final_total)

# 4.3 - Debugging Variables

nr1 = 5
nr2 = 4
nr3 = 5
print(nr3 / (nr1 % nr2) )
nr1 = nr1+1
print(nr3 / (nr1 % nr2) )
nr1 = nr1+1
print(nr3 / (nr1 % nr2) )

# 4.4 - Soft typing
# When assigning a variable from the start it is referred to as "hard typing".
# If a variable is able to be changed after it is assigned, this is called "soft typing". For instance, a variable 'x' may start as = 1 but later in the code could be changed to another interger like 3, which would overwrite it's original variable value.

# Checking value type:
a = 3 # Interger
print( type(a) )
a = 3.0 # Float
print( type(a) )
a = "3.0" # String
print( type(a) )

# When types are added together they retain their value type.
a = 1
b = 4
c = "1"
d = "4"
print(a+b)
print(c+d)

# Different value types are unable to be added together, they MUST be the same type.

# test