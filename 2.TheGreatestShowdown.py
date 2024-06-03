# 2. The Greatest Showdown
# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The largest number is 4.".
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

numbers = [num1, num2, num3]

# Find the largest number using a loop
largest = numbers[0]
for number in numbers:
  if number > largest:
    largest = number

print("The largest number is", largest)