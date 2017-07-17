# ** Chapter 3 Exercises **
# Exercise 3.1
p = 24.95
bs = .6
sh = 3
sha = .75
copies = 60

inital = (p*bs)+p+sh
total = (inital-sh+sha)*copies
print(total)

# TODO: not be stupid
# correct answer
# print (60 * (0.6 * 24.95 + 0.75) + (3 - 0.75))
