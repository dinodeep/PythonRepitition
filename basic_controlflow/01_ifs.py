
# Code does not always read every line top-to-bottom. Some lines of code are
#     - skipped
#     - repeated
# because of CONTROL-FLOW (controls the flow of the execution of the code)

# There are two fundamental things that affect control-flow
#     - if-statements (for skipping certain lines)
#     - while-loops   (for repeating certain lines)

# First, we start with if-statements (a.k.a ifs)

# 'ifs' are written in a specific format that look like this
'''
if <condition>:
    <code when true>
else:
    <code when false>
'''
# You can read it as: "IF <condition> is True, then run the <code when true>, ELSE run the <code when false>"
# "ifs" allow you to skip certain lines of code or choose which lines of code you want to run based on some condition

# NOTE: <condition> must always turn into a True or False boolean value
# NOTE: any code that is in a if-statement MUST be indented evenly, otherwise python will get an error when you try to run the code

# Example: change condition to different booleans to see what happens
condition = True
if condition:
    print("The condition is true")
    print("I'm running the true part")
else:
    print("The condition is false")

# more examples:
playsPiano = True
playsTrumpet = False
if playsTrumpet and playsPiano:
    print("I play multiple instruments")
else:
    print("I play one or less instruments")

isPresident = True
numTerms = 1
if isPresident and numTerms < 2:
    print("I, the POTUS, will run for re-election next year.")
else:
    print("I, the POTUS, will be done his two terms soon.")

# ========
# PRACTICE
# ========

# 1. of voting age - create a variable with your age, if you are older than 17, print "I can vote", otherwise, print "I can't vote. :("
#                    then, in another if statement, if you are older than 13, print "I can vote next election", otherwise "I still won't be able to vote next election"

# 2. what gen? - create a variable with your age, print "You are a ____" and replace ____ with the correct generation based on the age
#                Boomer (56-74), Gen X (40-55), Millenial (25-39), Gen Z (0-24)

# 3. weather -  using the variables below, create two new variables: isCold and isFreezing
#               set isCold to True if the temperature is less than 45 or if it is snowing, False otherwise
#               set isFreezing to True if the temperature is less than 35 and if it is windy
#               do not explicitly type "True" or "False", use the variable 'temperature' to set isCold and isFreezing
#               that way you code can be more flexible and is dependent on temperature
temperature = 35
isRaining = False
isSnowing = True
isWindy = False

# 3. weather (continued) - now you plan on going outside in these weather conditions, print the correct statement if the expression is true (you may have to print multiple)
#                        - NOTE: change the variables above however you like and see the different responses
#                        - if it is raining and snowing, then print "I'm going to wear some snowboots.". Otherwise, print "Normal sneakers will do."
#                        - if the temperature is above 75 and it is not raining, then print "I'll wear flip-flops".
#                                      Otherwise, if it is raining, print "I need rainboots", else print "I can just wear sneakers"
#                        - if it is not cold and it is snowing, print "this should not be happening",
#                                      Otherwise, if it is freezing, then print "there might be ice forming on the groud", otherwise print "the snow will melt quickly"
#                        - if it is windy and it is freezing, then print "I should wear a scarf and hat",
#                                      Otherwise if it is not freezing then print "I don't really need a scarf", else, print "It's pretty windy outside"
