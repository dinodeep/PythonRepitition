# before we talk about strings variables, we must know what a STRING LITERAL is
# a string literal is simply any text in your code that is surrounded by (single or double) quotes
# for example: "here's johnny!" is a string literal

# string variables are variables that are give values of type string (either from other string variables or string literals)
# example:
string_var = "greetings"
# like any variable, this variable we defined above has a name, a type, and a value

# there are also a lot of cool uses and built-in functions that come with strings which will take some practice and reptition getting used to
# one such operation is the '+' function which concatenates two strings and places them end-to-end
# NOTE: you now see the '+' function has different uses depending on whether you are adding two integers or two strings
combined_str = string_var + ", fellow human!"
print(combined_str)


# ====================
# PRACTICE STARTS HERE
# ====================

# 0. define a variable named 'first' with your first name as the string value

# 1. define a variable named 'last' with you last name as the string value

# 2. concatenate (a.k.a putting two things end-to-end) your first and last name using the + operator with strings
#    and store the result in the variable 'full'

# 3. now with three separate calls to the print(...) function (this means you call the print function three times )
#    print the first, last, and full variables you created in steps 0, 1, and 2

# 4. notice how there is no space between the first and last name in 'full'
#    define a new variable 'fixed_full' which uses the first and last variables and concatenates them with a space in between
#    you'll have more than one + sign, and you'll want to use the a " " string literal

# 5. there are some special functions where you can convert between types
#    create a string variable called 'x' that stores "5" as a string
#    in two calls to print(...), print its type and its value
#    NOTE: printing a variables type and value helps you understand what is being stored and what type the variable is
#          so if you are ever unsure about what a variable does or what value it holds, it helps to print the type and value

# 6. create a string variable called 'y' that stored "6" as a string
#   in two calls to print(...), print its type and its value

# 7. now, redefine x to store its value as an integer by calling int(x)
#    int(x) converts any string-typed value to its int-typed value and returns it
#    in two calls to print(...), print its type and its value

# 8. now, redefine y to store its values as an integer by calling int(x)
#    in two calls to print(...), print its type and its value

# 9. define a variable 'z' stored with the sum of x and y
#    print the type and its value

# 10. redefine the variable 'z' by converting it to a string using str(...)
#     str(...) takes in 1 input and converts it to its string respresentation
#    print the type and value of the redefined z
