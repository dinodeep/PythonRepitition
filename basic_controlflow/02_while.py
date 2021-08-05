# 'if statements' allow code to be skipped depending on if a boolean is True
# 'while loops' allow code to be REPEATED depending on if a boolean is True

# 'while loops' are written in a specific format that looks like this
'''
while <condition>:
    <code repeating when true>
'''
# You can read it as: "WHILE <condition> is True, then run ALL of <code repeating when true>. Once the code is done AND the condition is False, leave EXIT the loop"
# it seems pretty simple but it is very powerful

# 'while loops' allow you to repeat lines of code.

# NOTE: <condition> must always turn into a True or False boolean value
# NOTE: any code that is in the while-loop (like ifs and functions) MUST be indented evenly, otherwise you'll get a syntax error

# Example

# try to predict what this will do before running it
i = 0               # define an i = 0
while i < 10:       # keep looping when i < 10
    print(i)            # in each loop, print i
    i = i + 1           # add 1 to i

print()
even = 0
while even <= 12:
    print(even)
    even = even + 2

print()
i = 123
while i < 15:
    print(i)
    if i > 64:
        i = i / 2
    else:
        i = i - 3

# ========
# PRACTICE
# ========


'''
#1: use input(...) to take in a positive number and convert it into an int and store it in 'x'
    then use a while loop print all numbers from 0 to 'x'
'''

'''
#2: print all even numbers from 0 to 'x' using a while loop
'''

'''
#3: print all odd numbers from 0 to 'x' using a while loop
'''

'''
#4: print all multiples of 7 from 0 to 'x' using a while loop
'''

'''
#5: print all even numbers from x to 0 using a while loop (and maybe an if-statement)
'''

'''
CHALLENGE: keep calling input(...) until the input that the user provides has length 5
           and store the final input into 'x'
           NOTE: you can get the length of a string by calling the len(...) function and passing the string (example below)
'''
l = len("oh no!")
print(l)
