#1.DecisionsattheCrossroad

# Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.
# Buggy Code:
# <="" code="" style="margin: 0px 0px 30px; padding: 0px; box-sizing: border-box; position: relative; display: block; min-height: 40px; width: 736.679px;">
# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")
#_______________________________________

# Correct code:
number = int(input("Enter a number: ")) #Inputs is string, need to be converted to numbers 
if number > 0:
    print("The number is positive.")
elif number == 0: #need ==
    print("The number is zero.")
else: #number < 0
    print("The number is negative.")
