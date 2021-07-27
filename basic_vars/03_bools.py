# there is a type of variables in almost all programming languages called BOOLEANS (bool for short)
# this type can have two value: True or False
# the boolean variable is pretty important to understand in the coding world
# there are many important operations that can be used with bools

# example (defining two vars with the two boolean values and printing them on the same line separated by a space):
b1 = True
b2 = False
print(b1, b2)

# OPERATIONS

# not - turn a boolean into its opposite value (not True == False)
print(not True)
print(not False)

# and - returns True if both booleans are True, False otherwise
# x and y True only if x True AND y True
print(True and True)
print(False and True)
print(False and False)

# or - returns True if at least one of the two booleans are True
# x or y True if x true OR y true
print(True or True)
print(True or False)
print(False or False)

# NOTE: there are order of operations when working with boolean operations too
# first precedence to last precedence: not, and, or

# you can make some more complex expressions as well (kinda like math)
# try to predict what the result of this expression will be before looking at the printed value
print(not ((False and True) or (False and False)) and ((False and True) and not False))

# also some comparisons evaluate to True or False depending on whether they are true or not
# some of these operations are:
#  == (equal to)
#   < (less than)
#   > (greater than)
#  <= (less than or equal to)
#  >= (greater than or equal to)
# You can see that the expressions below evaluate to booleans with values based on whether they are true
print(23 > 10)
print(-3 <= 18)
print(-4 < -23)
print(23 == 23)
print(18 == 17)

# ====================
# PRACTICE STARTS HERE
# ====================

# define a variable called 'is_five_foot' with a value of True if you are over five foot tall, False otherwise

# define a variable called 'plays_ball' with a value of True if you play basketball, False otherwise

# define a variable called 'ate_meat' with a value of True if you ate meat within the last 3 days

# define a variable called 'big_meat' with the boolean value if you are over five foot and ate meat in the last 3 days using the variables defined above

# define a variable called 'meat_ball' with the boolean value if you play basketball and ate meat in the last 3 days using the variables defined above

# define a variable called 'complex1' with the boolean value if you are taller than five foot and ate meat or you did not eat meat and taller than five foot

# define a variable called 'complex2' with the boolean value if you did not eat meat and you are either a basketball player or shorter than five foot

# for all the 'define a variable' problems above, print the variables out and make sure that the values are expected

# predict the values of the variables below, print the result to validate your answer (understand how it got to that result)
# do it one at a time because some variables will refernce variables above them
a = not True and False or False
b = (True or not False and True) or False
c = not (False and True) and False or (not (True and not False) or False and True)
d = not not not not not (not (not not not True and False) and True or False)
e = (not (a and b) or not (c or d)) and (a and not (b or c))
f = ((e and not b) or (c and d)) or (not (a and (not c and (d and True))))
