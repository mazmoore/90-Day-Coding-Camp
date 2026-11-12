
# ==========================================
# DAY 06 - MULTIPLE CONDITIONS
# Topic: Using if, elif, and else
# ==========================================

# LESSON NOTES
#
# The elif keyword means "else if".
#
# It allows Python to evaluate additional
# conditions when an earlier condition
# is False.
#
# A conditional chain can contain:
#
# One if statement
# Zero or more elif statements
# An optional else statement
#
# Python checks the conditions from top
# to bottom.
#
# Once a condition evaluates to True,
# Python executes that block and skips
# the remaining branches in the chain.
#
# The else block runs only when none
# of the earlier conditions are True.
#
# The order of conditions is important.


# EXAMPLE 1: Basic if, elif, and else

age = 17

if age >= 21:
    print("You are 21 or older.")
elif age >= 18:
    print("You are between 18 and 20.")
else:
    print("You are under 18.")


# EXAMPLE 2: Grading System

grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# EXAMPLE 3: Understanding Condition Order
#
# Python checks conditions in order.
#
# If a broad condition comes first,
# it may prevent more specific conditions
# from being reached.

score = 95

if score >= 90:
    print("Excellent performance.")
elif score >= 80:
    print("Good performance.")
elif score >= 70:
    print("Satisfactory performance.")
else:
    print("Needs improvement.")


# EXAMPLE 4: Temperature Categories

temperature = 78

if temperature >= 90:
    print("Very hot weather.")
elif temperature >= 75:
    print("Warm weather.")
elif temperature >= 60:
    print("Mild weather.")
else:
    print("Cool weather.")


# EXAMPLE 5: Flower Order Categories

rose_quantity = 75

if rose_quantity < 25:
    print("Order denied: Minimum is 25 roses.")
elif rose_quantity < 50:
    print("Small rose arrangement.")
elif rose_quantity < 100:
    print("Medium rose arrangement.")
else:
    print("Large rose arrangement.")


# EXAMPLE 6: User Input with elif

age = int(input("Enter your age: "))

if age < 13:
    print("Child category.")
elif age < 18:
    print("Teen category.")
elif age < 65:
    print("Adult category.")
else:
    print("Senior category.")


# EXAMPLE 7: Account Balance Categories

balance = 750

if balance >= 1000:
    print("High account balance.")
elif balance >= 500:
    print("Moderate account balance.")
elif balance > 0:
    print("Low account balance.")
else:
    print("Zero or negative balance.")


# EXAMPLE 8: Shipping Cost Categories

order_total = 125

if order_total >= 150:
    print("Free express shipping.")
elif order_total >= 100:
    print("Free standard shipping.")
elif order_total >= 50:
    print("Standard shipping: $5.")
else:
    print("Standard shipping: $10.")


# EXAMPLE 9: Login Access Levels
#
# This is a basic learning example.
# Real systems require secure authentication
# and authorization controls.

role = "admin"

if role == "admin":
    print("Administrator access.")
elif role == "manager":
    print("Manager access.")
elif role == "employee":
    print("Employee access.")
else:
    print("Unknown role.")


# EXAMPLE 10: Network Port Categories
#
# Ports are numbers used to identify
# network services.
#
# This example classifies port numbers
# by their standard numeric ranges.

port = 443

if port < 0 or port > 65535:
    print("Invalid port number.")
elif port <= 1023:
    print("Well-known port range.")
elif port <= 49151:
    print("Registered port range.")
else:
    print("Dynamic or private port range.")


# EXAMPLE 11: Password Length Categories
#
# Password length is only one factor
# in password security.

password = "ExamplePassword123!"

length = len(password)

if length < 8:
    print("Very short password.")
elif length < 12:
    print("Short password.")
elif length < 16:
    print("Longer password.")
else:
    print("Password is 16+ characters.")


# EXAMPLE 12: Comparing Three Numbers

number1 = 15
number2 = 25
number3 = 10

if number1 >= number2 and number1 >= number3:
    print("First number is one of the largest.")
elif number2 >= number1 and number2 >= number3:
    print("Second number is one of the largest.")
else:
    print("Third number is one of the largest.")


# EXAMPLE 13: Using Logical Operators
#
# and requires both conditions to be True.
# or requires at least one condition to be True.
# not reverses a Boolean value.

age = 25
has_id = True

if age >= 18 and has_id:
    print("Verification passed.")
elif age >= 18 and not has_id:
    print("Identification required.")
else:
    print("Age requirement not met.")


# EXAMPLE 14: Menu Selection

print("===== MAIN MENU =====")
print("1. View Account")
print("2. Update Profile")
print("3. Security Settings")
print("4. Exit")

choice = input("Select an option: ")

if choice == "1":
    print("Opening account information.")
elif choice == "2":
    print("Opening profile settings.")
elif choice == "3":
    print("Opening security settings.")
elif choice == "4":
    print("Exiting program.")
else:
    print("Invalid selection.")


# EXAMPLE 15: Security Alert Severity
#
# This is a simplified classification
# example, not a real detection system.

failed_logins = 12

if failed_logins >= 20:
    print("Critical alert: Many failed logins.")
elif failed_logins >= 10:
    print("High alert: Investigate activity.")
elif failed_logins >= 5:
    print("Medium alert: Monitor account.")
elif failed_logins > 0:
    print("Low alert: Failed login detected.")
else:
    print("No failed login attempts.")


# EXAMPLE 16: Multiple Conditions with Strings

status = input("Enter system status: ").strip().lower()

if status == "online":
    print("System is operational.")
elif status == "maintenance":
    print("System is under maintenance.")
elif status == "offline":
    print("System is unavailable.")
else:
    print("Unknown system status.")


# EXAMPLE 17: Understanding Boundaries
#
# Test values at the boundaries
# between categories.
#
# For example, 69, 70, 79, and 80
# can help verify grading conditions.

grade = 79

if grade >= 80:
    print("B or higher.")
elif grade >= 70:
    print("C.")
else:
    print("Below C.")


# WHAT I LEARNED
#
# 1. elif means "else if".
# 2. elif checks additional conditions.
# 3. Python evaluates branches in order.
# 4. Only the first matching branch runs.
# 5. else handles unmatched conditions.
# 6. Condition order affects results.
# 7. and combines required conditions.
# 8. or accepts either condition.
# 9. not reverses a Boolean value.
# 10. Boundary testing helps find errors.
