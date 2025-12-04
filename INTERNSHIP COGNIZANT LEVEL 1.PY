#task1: STRING REVERSAL

# Reverse a string

text = input("Enter a string: ")
reversed_text = text[::-1]

print("Reversed string:", reversed_text)



#task2: TEMPERATURE CONVERSION


# Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Convert Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius:", celsius)


#Task 3: EMAIL VALIDATOR


# Basic email validator

email = input("Enter your email address: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid email address")
else:
    print("Invalid email address")


# Task 4: Calculator Program

# Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print("Result:", result)

  
    

# Task 5: Palindrome Checker

# Palindrome checker

text = input("Enter a string: ")
reversed_text = text[::-1]

if text == reversed_text:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")






