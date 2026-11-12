
# ==========================================
# DAY 05 - CONDITIONAL STATEMENTS
# Topic: Making Decisions with if and else
# ==========================================

# LESSON NOTES
#
# Conditional statements allow programs
# to make decisions based on conditions.
#
# A condition is an expression that evaluates
# to either True or False.
#
# The if statement executes a block of code
# only when its condition is True.
#
# The else statement provides an alternative
# block of code when the if condition is False.
#
# Python uses indentation to identify which
# statements belong to a conditional block.
#
# A colon (:) marks the beginning of a block.


# EXAMPLE 1: Basic if Statement

age = 20

if age >= 18:
    print("You are an adult.")

print("Program completed.")


# EXAMPLE 2: Basic if and else

age = 16

if age >= 18:
    print("Access granted.")
else:
    print("Access denied.")


# EXAMPLE 3: Comparison Operators
#
# == means equal to
# != means not equal to
# >  means greater than
# <  means less than
# >= means greater than or equal to
# <= means less than or equal to

number = 10

print(number == 10)
print(number != 5)
print(number > 7)
print(number < 15)
print(number >= 10)
print(number <= 20)


# EXAMPLE 4: Checking a Password
#
# This is a basic learning example.
# Real systems should not store passwords
# directly in source code.

password = "python123"

if password == "python123":
    print("Login successful.")
else:
    print("Incorrect password.")


# EXAMPLE 5: Checking a Username

username = "admin"

if username == "admin":
    print("Welcome, administrator.")
else:
    print("Unknown username.")


# EXAMPLE 6: Number Comparison

number = 25

if number > 20:
    print("The number is greater than 20.")
else:
    print("The number is 20 or less.")


# EXAMPLE 7: Checking Even or Odd
#
# The modulus operator (%) returns
# the remainder after division.
#
# Even numbers have a remainder of zero
# when divided by 2.

number = 12

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# EXAMPLE 8: Flower Order Minimum
#
# A customer must order at least 25 roses.

rose_quantity = 50

if rose_quantity >= 25:
    print("Order accepted.")
else:
    print("Minimum order is 25 roses.")


# EXAMPLE 9: Checking Account Balance

balance = 200
withdrawal = 75

if withdrawal <= balance:
    print("Withdrawal approved.")
else:
    print("Insufficient funds.")


# EXAMPLE 10: Using Boolean Variables

is_student = True

if is_student:
    print("Student discount available.")
else:
    print("Regular pricing applies.")


# EXAMPLE 11: Using User Input

age = int(input("Enter your age: "))

if age >= 18:
    print("You meet the age requirement.")
else:
    print("You do not meet the age requirement.")


# EXAMPLE 12: Checking a PIN
#
# This is a basic demonstration only.
# Do not use hardcoded PINs in real systems.

pin = input("Enter your PIN: ")

if pin == "1234":
    print("PIN accepted.")
else:
    print("Incorrect PIN.")


# EXAMPLE 13: Checking a Product Price

price = 120

if price > 100:
    print("This is a premium product.")
else:
    print("This is a standard product.")


# EXAMPLE 14: Comparing Two Numbers

number1 = 15
number2 = 20

if number1 > number2:
    print("The first number is larger.")
else:
    print("The first number is not larger.")


# EXAMPLE 15: Understanding Indentation
#
# Indented statements belong to the
# conditional block.
#
# Unindented statements execute outside
# the conditional block.

temperature = 90

if temperature > 85:
    print("It is hot outside.")
    print("Remember to stay hydrated.")

print("Weather check completed.")


# EXAMPLE 16: Checking a File Extension
#
# endswith() checks whether a string
# ends with specific characters.

filename = "report.pdf"

if filename.endswith(".pdf"):
    print("PDF file detected.")
else:
    print("File is not a PDF.")


# EXAMPLE 17: Checking a Security Setting

firewall_enabled = True

if firewall_enabled:
    print("Firewall protection is enabled.")
else:
    print("Warning: Firewall is disabled.")


# EXAMPLE 18: Basic Access Control

authorized_user = False

if authorized_user:
    print("Access to the system granted.")
else:
    print("Access to the system denied.")


# WHAT I LEARNED
#
# 1. Conditions evaluate to True or False.
# 2. if executes code when a condition is True.
# 3. else executes when the condition is False.
# 4. Comparison operators compare values.
# 5. == checks equality.
# 6. = assigns a value to a variable.
# 7. Indentation defines code blocks.
# 8. Colons begin conditional blocks.
# 9. Conditions can use user input.
# 10. Conditional logic supports access checks.
