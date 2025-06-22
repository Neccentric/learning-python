# Exercise 3: User Input and Basic Calculator
# TODO: Create a simple calculator that takes two numbers from user input

# 1. Ask the user for the first number
# 2. Ask the user for the second number
# 3. Convert the inputs to appropriate data types
# 4. Perform basic operations (addition, subtraction, multiplication, division)
# 5. Display the results

# Hint: Use input() and float() or int()
# Hint: Use f-strings for formatting output

# Your code here:

first_input = float(input("Enter the first number: "))
second_input = float(input("Enter the second number: "))
addition = first_input + second_input
subtraction = first_input - second_input
multiplication = first_input * second_input
division = first_input / second_input if second_input!= 0 else "undefined (cannot divide by zero)"
Modulus = first_input % second_input if second_input != 0 else "undefined (cannot divide by zero)"
# Displaying the results
print("\nResults:")
print(f"Addition: {first_input} + {second_input} = {addition}")
print(f"Subtraction: {first_input} - {second_input} = {subtraction}")
print(f"Multiplication: {first_input} * {second_input} = {multiplication}")
print(f"Division: {first_input} / {second_input} = {division}") 
print(f"Modulus: {first_input} % {second_input} = {Modulus}")
print(f"Exponentiation: {first_input} ** {second_input} = {first_input  ** second_input}")
print(f"Floor Division: {first_input} // {second_input} = {first_input // second_input if second_input != 0 else 'undefined (cannot divide by zero)'}")
print(f"Square Root of {first_input} = {first_input ** 0.5}")