
# usually, there are three parts to a variable
# 1. name = how you reference the variable (the name is chosen by the programmer)
# 2. type = says what values the variable can have (the type is determined from the value)
# 3. value = the actual value stored in the variable (the value is chosen by the programmer)
#            a value can be provided from a different variable (y = x) or provided as a constant (y = 5)

# For example:
# x = 5
# name: x
# type: int
# value: 5

# Another example:
# s = "greetings, sire"
# name: s
# type: string
# value: "greetings, sire"

# variables with that are of INTEGER (a.k.a int) have values that are whole numbers
# because a program can not have an infinite amount of numbers, variables of type int can store -2147483648 through 2147483647

# ====================
# PRACTICE STARTS HERE
# ====================

# EXAMPLE
# 0. define a variable with name 'this_is_a_number' and value 23
# print the type of this variable and print its value
this_is_a_number = 23
print(type(this_is_a_number))   # printing type
print(this_is_a_number)         # printing value

# DEFINING

# 1. define a variable with name 'x' and value 5
# print the type of this variable by (1) calling the built-in type(<var>) function and (2) printing the value returned by calling the function

# 2. define a variable with name 'y' and value 17
# print the value of this variable by calling the built-in print(<var>)

# 3. define a variable with name 'z' and a value that is a prime number

# 4. define a variable with name 'sum' that is the sum of x, y, and z
# print the type and value of this variable

# 5. REDEFINE the variable with name 'x' and give it value 25
# print the type of this variable

# 6. REDEFINE the variable with name 'y' and give it value of it's current value plus 3
# print the type of this variable and print its value

# 7. REDEFINE the variable with name 'sum' and give it value of the sum 'x' and 'y' values
# print the type and value of this variable

# 8. CHALLENGE: swap the values in 'x' and 'y' ('x' is redefined to have 'y' value and 'y' is redefined to have 'x' value)
#               CONSTRAINT: DO NOT explicitly set the variables with constants like y = 25
#                           your code can not use any constants (any method that does not use constants is valid)


# NOTE:
# - a BUILT-IN function is automatically provided in any python program
#   (that means that you don't need to define it), you can just call it
# - REDEFINING a variable that is already defined sets the variable to a new value (won't be able to use whatever the old value was)
