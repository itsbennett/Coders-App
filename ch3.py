# * EXPRESSIONS *
# 3.1 - Displaying Results
# To display results for a formula the function, also called statement or command, PRINT is needed.
# Just entering the formula alone is not enough.

# this could be entered in shell without invoking python for answer
# but cannot be used by itself in a script
5+7

# only this produces results for using Python
print( 5+7 )

print( "Hello world!" )
print( "I", "own", "two", "apples", "and", "one", "banana" )
print( "I", "own", 2, "apples", "and", 1, "banana" )

# 3.2 - Data Types
# STRINGS, INTERGERS, FLOATS

# 3.2.1 - STRINGS
# In strings " " is equal to ' ' (single or double quotes).
# Can\'t prevents the string from prematurely ending with the \
# \\\ actually prints the backslash if need be.
print( 'I can\'t stand it' )
print( 'I can\\\'t stand it' )

# 3.2.2 - INTERGERS
# Intergers by def are whole numbers. Can be positive, negative or zero.
# Number values can be written in different ways, an example being:
print( 1 )
print( +1 )

# The reason the following doesn't work is because each number ie being treated individual after the comma.
# Larger numbers must be written without commas, obviously.
print( 1, 000, 000, 000 )

# 3.2.3 - FLOATS
# Floating point numbers are numbers with decimals.
# To make an interger a floating number, add .0 to the end of it.
# Python 2 used to round formulas up, but Python 3 natively will print the exact answer
# To round you use function round()
print( 431 / 100 * 100)

# Assigning answer to x, then rounding
x = 431 / 100 * 100
print(round(x))

# 3.3 - Expressions
# Expressions are a combination of one or more values (see data types) using operators, which result in a new value.
# OPERATORS:
print( 15+4 ) # addition +
print( 15-4 ) # substraction -
print( 15*4 ) # multiplication *
print( 15/4 ) # division /
print( 15//4 ) # interger division //
print( 15**4 ) # power **
print( 15%4 ) # modulo %

# Interger division ("floor division") is a division tha rounds down to a whole number.
# If floats become involved, it will still be a float, but rounded down.
# Of course, if only intergers, it will remain an interger.

# Modulo operator (%) takes the remainder of a division. When used, it will only produce the remainder of the result.

# 3.3.2 - More Complex Calculations
# Python allows PEMDAS for doing equations.
print ( 5*2-3+4/2 )

# The end result is a float because of the division operation. This automatically turns it into a floating interger.

# This is an example of how spacing properly can drastically help readability.
print ( (5*2)-(3+4) / 2 ) # readable

#  * EXERCISE *
# Write a program that displays the number of seconds in a week on one line.
d = 7
s = 86400
print( d*s )

# 3.3.3 - Sting Expressions
# You can use the addition operator to link two strings and you can use the multiplication operator to create repetition of strings.

print( "hello" + "world")
print( 3*"Hello " )
print( "goodbye " * 3)

# 3.3.4 - Type casting
# The breakdown of a statement is function("parameters")
# print("Hello world") - print is the function, "hello world" is the parameters

# **Three main type of casting functions**
# int() - returns value as interger, rounds down if necess
# float() - return value is float
# str() - returns value as string

print( 15/4 )
print( int(15/4) ) # the int casting function rounds down

print( 15+4 )
print( float(15+4) ) # adds floating decimal

# This allows the interger to be added to the parameter because it is converted into a string.
print("I own " + str(15) + " apples.")

# 3.4 - Style
# BE CONSISTENT.
