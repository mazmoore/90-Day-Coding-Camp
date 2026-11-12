
# ==========================================
# DAY 04 - USER INPUT
# Topic: Interactive Python Programs
# ==========================================

# LESSON NOTES
#
# The input() function allows a Python
# program to receive information from a user.
#
# When Python encounters input(), the program
# pauses and waits for the user to type
# something into the terminal.
#
# The user presses Enter to submit a response.
#
# IMPORTANT:
# input() always returns a string (str).
#
# If a program needs to perform calculations
# with user input, the value may need to be
# converted to an integer or float.


# EXAMPLE 1: Basic User Input

name = input("What is your name? ")

print("Hello,", name)


# EXAMPLE 2: Asking Multiple Questions

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Welcome,", first_name, last_name)


# EXAMPLE 3: Storing User Input

school = input("What university do you attend? ")

print("University:", school)


# EXAMPLE 4: Understanding Input Data Types
#
# Even if the user enters a number,
# Python initially stores it as a string.

age = input("How old are you? ")

print("You entered:", age)
print("Data type:", type(age))


# EXAMPLE 5: Converting Strings to Integers
#
# int() converts a valid numeric string
# into an integer.
#
# This allows mathematical calculations.

age = int(input("Enter your age: "))

next_year_age = age + 1

print("Next year you will be:", next_year_age)


# EXAMPLE 6: Converting Strings to Floats
#
# float() converts a valid numeric string
# into a decimal number.

price = float(input("Enter the product price: "))

print("Product price:", price)


# EXAMPLE 7: Simple Addition Calculator

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

total = number1 + number2

print("The sum is:", total)


# EXAMPLE 8: Flower Shop Order
#
# Collect information about a customer order.

customer_name = input("Customer name: ")
flower_type = input("Flower type: ")
quantity = int(input("How many flowers? "))

print("Customer:", customer_name)
print("Flower:", flower_type)
print("Quantity:", quantity)


# EXAMPLE 9: Calculating an Order Total

bouquet_price = 65.00

quantity = int(input("How many bouquets? "))

total = bouquet_price * quantity

print("Your total is: $", total)


# EXAMPLE 10: Building a Student Profile

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
university = input("Enter your university: ")
major = input("Enter your major: ")
career_goal = input("Enter your career goal: ")

print()
print("===== STUDENT PROFILE =====")
print("Name:", student_name)
print("Age:", student_age)
print("University:", university)
print("Major:", major)
print("Career Goal:", career_goal)


# EXAMPLE 11: Using Input with Calculations

hours_worked = float(input("Hours worked: "))
hourly_rate = float(input("Hourly pay rate: "))

gross_pay = hours_worked * hourly_rate

print("Gross pay before deductions: $", gross_pay)


# EXAMPLE 12: String Concatenation
#
# The + operator can combine strings.
#
# This is called concatenation.

first_name = input("First name: ")
last_name = input("Last name: ")

full_name = first_name + " " + last_name

print("Full name:", full_name)


# EXAMPLE 13: Input with Whitespace
#
# strip() removes leading and trailing
# whitespace from a string.

username = input("Enter username: ").strip()

print("Username:", username)


# EXAMPLE 14: Converting Text to Lowercase
#
# lower() converts letters to lowercase.
#
# This can help standardize user responses.

answer = input("Do you like Python? ").lower()

print("Your response:", answer)


# EXAMPLE 15: Combining String Methods
#
# strip() removes surrounding whitespace.
# lower() converts letters to lowercase.

response = input("Enter yes or no: ").strip().lower()

print("Normalized response:", response)


# WHAT I LEARNED
#
# 1. input() collects information from users.
# 2. input() returns a string.
# 3. int() converts valid input to integers.
# 4. float() converts valid input to decimals.
# 5. Variables store user responses.
# 6. Input can be used in calculations.
# 7. Strings can be joined using +.
# 8. strip() removes surrounding whitespace.
# 9. lower() converts text to lowercase.
# 10. Interactive programs respond to users.
