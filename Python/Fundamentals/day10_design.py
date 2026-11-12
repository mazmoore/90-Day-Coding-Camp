
# ==========================================
# DAY 10 - PSEUDOCODE AND PROGRAM DESIGN
# Topic: Planning Programs Before Coding
# ==========================================

# LESSON NOTES
#
# Program design is the process of planning
# how a program will solve a problem.
#
# Before writing code, programmers identify:
#
# 1. The problem being solved
# 2. The information needed
# 3. The processing steps
# 4. The expected output
# 5. Possible errors or unusual situations
#
# An algorithm is a sequence of steps
# designed to solve a problem.
#
# Pseudocode describes an algorithm
# using simple, human-readable instructions.
#
# Pseudocode does not need to follow
# the exact syntax of a programming language.
#
# Python comments can be used to document
# pseudocode before writing actual code.


# EXAMPLE 1: Understanding Input, Process, Output
#
# PROBLEM:
# Calculate the total cost of a purchase.
#
# INPUT:
# Product price and quantity
#
# PROCESS:
# Multiply price by quantity
#
# OUTPUT:
# Display the total cost

price = 25
quantity = 4

total = price * quantity

print("Total cost:", total)


# EXAMPLE 2: Writing Pseudocode
#
# PSEUDOCODE:
#
# START
# SET number1 to 10
# SET number2 to 20
# ADD number1 and number2
# STORE result in total
# DISPLAY total
# END
#
# PYTHON IMPLEMENTATION:

number1 = 10
number2 = 20

total = number1 + number2

print("Sum:", total)


# EXAMPLE 3: Planning a Greeting Program
#
# PSEUDOCODE:
#
# START
# ASK user for their name
# STORE name
# DISPLAY personalized greeting
# END

name = input("Enter your name: ")

print("Welcome,", name)


# EXAMPLE 4: Planning a Conditional Program
#
# PROBLEM:
# Determine whether a user meets
# an age requirement.
#
# PSEUDOCODE:
#
# START
# SET age
# IF age is 18 or older
#     DISPLAY access granted
# OTHERWISE
#     DISPLAY access denied
# END

age = 20

if age >= 18:
    print("Access granted.")
else:
    print("Access denied.")


# EXAMPLE 5: Planning Multiple Conditions
#
# PROBLEM:
# Assign a letter grade.
#
# PSEUDOCODE:
#
# START
# SET numeric grade
# IF grade is at least 90
#     DISPLAY A
# ELSE IF grade is at least 80
#     DISPLAY B
# ELSE IF grade is at least 70
#     DISPLAY C
# OTHERWISE
#     DISPLAY Below C
# END

grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: Below C")


# EXAMPLE 6: Planning a While Loop
#
# PROBLEM:
# Count from 1 through 5.
#
# PSEUDOCODE:
#
# START
# SET counter to 1
# WHILE counter is less than or equal to 5
#     DISPLAY counter
#     INCREASE counter by 1
# END WHILE
# END

counter = 1

while counter <= 5:
    print("Counter:", counter)
    counter += 1


# EXAMPLE 7: Planning a For Loop
#
# PROBLEM:
# Display five security events.
#
# PSEUDOCODE:
#
# START
# FOR each event number from 1 through 5
#     DISPLAY event number
# END FOR
# END

for event in range(1, 6):
    print("Security event:", event)


# EXAMPLE 8: Planning a Function
#
# PROBLEM:
# Calculate the total price of an order.
#
# PSEUDOCODE:
#
# DEFINE calculate_total(price, quantity)
#     MULTIPLY price by quantity
#     RETURN result
# END FUNCTION
#
# CALL function
# DISPLAY returned result

def calculate_total(price, quantity):
    total = price * quantity
    return total


result = calculate_total(75, 3)

print("Order total:", result)


# EXAMPLE 9: Breaking a Problem into Steps
#
# PROBLEM:
# Calculate the profit from flower sales.
#
# STEP 1: Identify revenue.
# STEP 2: Identify expenses.
# STEP 3: Subtract expenses from revenue.
# STEP 4: Display the profit.

revenue = 1500
expenses = 650

profit = revenue - expenses

print("Business profit:", profit)


# EXAMPLE 10: Flower Order Algorithm
#
# PROBLEM:
# Determine whether an order meets
# the minimum rose quantity.
#
# INPUT:
# Number of roses requested
#
# PROCESS:
# Compare quantity against minimum
#
# OUTPUT:
# Accepted or denied
#
# PSEUDOCODE:
#
# START
# SET minimum order to 25
# SET requested quantity
# IF quantity is at least minimum
#     DISPLAY order accepted
# OTHERWISE
#     DISPLAY order denied
# END

minimum_order = 25
requested_quantity = 50

if requested_quantity >= minimum_order:
    print("Flower order accepted.")
else:
    print("Minimum order is 25 roses.")


# EXAMPLE 11: Planning a Menu System
#
# PSEUDOCODE:
#
# START
# DISPLAY menu choices
# ASK user to select an option
# IF option is 1
#     DISPLAY account message
# ELSE IF option is 2
#     DISPLAY settings message
# OTHERWISE
#     DISPLAY invalid selection
# END

print("===== MAIN MENU =====")
print("1. View Account")
print("2. Settings")

choice = input("Select an option: ")

if choice == "1":
    print("Opening account.")
elif choice == "2":
    print("Opening settings.")
else:
    print("Invalid selection.")


# EXAMPLE 12: Designing a Reusable Program
#
# A program can be divided into
# smaller functions.
#
# Each function should have a
# clear responsibility.

def display_header():
    print("===== ORDER SYSTEM =====")


def calculate_subtotal(price, quantity):
    return price * quantity


def display_total(total):
    print("Total: $", total)


def run_order():
    display_header()

    subtotal = calculate_subtotal(65, 3)

    display_total(subtotal)


run_order()


# EXAMPLE 13: Planning Security Event Analysis
#
# PROBLEM:
# Count failed login events.
#
# INPUT:
# A list of login events
#
# PROCESS:
# Examine each event
# Increase the counter for failed events
#
# OUTPUT:
# Total failed login attempts
#
# PSEUDOCODE:
#
# START
# CREATE list of login events
# SET failed counter to zero
# FOR each event
#     IF event is failed
#         INCREASE counter
#     END IF
# END FOR
# DISPLAY failed counter
# END

login_events = [
    "success",
    "failed",
    "failed",
    "success",
    "failed"
]

failed_count = 0

for event in login_events:
    if event == "failed":
        failed_count += 1

print("Failed login events:", failed_count)


# EXAMPLE 14: Identifying Edge Cases
#
# An edge case is an unusual or
# boundary situation that may affect
# program behavior.
#
# Examples:
#
# - Zero quantity
# - Negative quantity
# - Empty input
# - Invalid menu selection
# - Extremely large values
#
# Programs should consider these cases.

quantity = -5

if quantity < 0:
    print("Invalid quantity.")
elif quantity == 0:
    print("No items ordered.")
else:
    print("Valid quantity:", quantity)


# EXAMPLE 15: Testing Program Logic
#
# Testing verifies that a program
# behaves as expected.
#
# A useful test plan includes:
#
# 1. Normal values
# 2. Boundary values
# 3. Invalid values
#
# Example:
# Test a minimum order of 25 roses.
#
# Test cases:
#
# Quantity 24 = Denied
# Quantity 25 = Accepted
# Quantity 26 = Accepted
# Quantity -1 = Invalid

def validate_order(quantity):
    if quantity < 0:
        return "Invalid"
    elif quantity >= 25:
        return "Accepted"
    else:
        return "Denied"


print(validate_order(24))
print(validate_order(25))
print(validate_order(26))
print(validate_order(-1))


# EXAMPLE 16: Designing a Main Function
#
# A main function organizes the
# primary flow of a program.
#
# A common Python pattern is:
#
# if __name__ == "__main__":
#     main()
#
# This runs main() when the file is
# executed directly, but not when
# it is imported as a module.

def main():
    print("Starting program design example.")
    print("Processing program tasks.")
    print("Program completed.")


if __name__ == "__main__":
    main()


# EXAMPLE 17: Understanding Flowcharts
#
# A flowchart visually represents
# the steps of an algorithm.
#
# Common symbols:
#
# Oval = Start or End
# Parallelogram = Input or Output
# Rectangle = Process
# Diamond = Decision
# Arrow = Direction of flow
#
# Example:
#
# START
#   |
# INPUT age
#   |
# IS age >= 18?
#   |       |
#  YES      NO
#   |       |
# GRANT    DENY
#   |       |
#   +---+---+
#       |
#      END
#
# Flowcharts help programmers
# visualize program decisions.


# EXAMPLE 18: Planning Before Implementation
#
# A useful workflow:
#
# 1. Understand the problem.
# 2. Identify inputs and outputs.
# 3. Break the problem into steps.
# 4. Write pseudocode.
# 5. Draw a flowchart if helpful.
# 6. Implement the solution.
# 7. Test normal and unusual cases.
# 8. Debug and improve the program.
# 9. Document the final solution.


# WHAT I LEARNED
#
# 1. Program design begins before coding.
# 2. Algorithms describe solution steps.
# 3. Pseudocode explains program logic.
# 4. Input, process, and output are key.
# 5. Complex problems can be divided.
# 6. Flowcharts visualize algorithms.
# 7. Functions organize program tasks.
# 8. Edge cases require consideration.
# 9. Testing verifies expected behavior.
# 10. Planning improves maintainability.
