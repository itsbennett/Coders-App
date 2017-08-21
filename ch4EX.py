# Exercise 4.1
var1 = 5
var2 = 10
var3 = 15
average =(var1+var2+var3 / 3)
print(average)

# Exercise 4.2
radius = 50
pi = 3.14159
formula = radius*radius*pi
print("The surface area of a circle with a radius of", radius, "is", formula)
# TODO: how to add radius and formula to this string

# Exercise 4.3
cents_dollar = 100
cents_quarter = 25
cents_dime = 10
cents_nickel = 5
# testing this out
amount = 1142 # to demonstrate at least one of each coin
cents = amount
dollars = int( cents / cents_dollar )
cents -= dollars * cents_dollar
quarters = int( cents / cents_quarter )
cents -= quarters * cents_quarter
dimes = int( cents / cents_dime )
cents -= dimes * cents_dime
nickels = int( cents / cents_nickel )
cents -= nickels * cents_nickel
cents = int( cents )

print( amount / cents_dollar, "Consists of:")
print( "Dollars:", dollars )
print( "Quarters:", quarters )
print( "Dimes:", dimes )
print( "Nickels:", nickels )
print( "Pennies:", cents)

# Exercise 4.4
a = 17
b = 23
print("a =", a, "and b =", b)
a += b
b = a - b
a -= b
print("a =", a, "and b =", b)
