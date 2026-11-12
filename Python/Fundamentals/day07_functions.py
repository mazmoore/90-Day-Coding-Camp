
# ==========================================
# DAY 07 - FUNCTIONS AND REUSABLE CODE
# Topic: Defining and Calling Functions
# ==========================================

# LESSON NOTES
#
# A function is a reusable block of code
# designed to perform a specific task.
#
# Functions help organize programs,
# reduce repetition, and improve readability.
#
# The def keyword defines a function.
#
# The function name identifies the function.
#
# Parentheses () hold optional parameters.
#
# A colon (:) begins the function body.
#
# Indentation determines which statements
# belong to the function.
#
# Defining a function does not execute
# the statements inside it.
#
# A function must be called to run.
#
# Functions can accept information
# through parameters and return results.


# EXAMPLE 1: Defining a Function

def welcome():
    print("Welcome to Python programming!")


# Calling the function

welcome()


# EXAMPLE 2: Calling a Function Multiple Times

def greeting():
    print("Hello!")
    print("Welcome to my coding camp.")


greeting()
greeting()
greeting()


# EXAMPLE 3: Functions with Multiple Statements

def student_profile():
    print("===== STUDENT PROFILE =====")
    print("University: New Mexico State University")
    print("Major: Information Technology")
    print("Career Goal: Cybersecurity Analyst")


student_profile()


# EXAMPLE 4: Function with a Parameter
#
# A parameter is a variable listed
# in the function definition.
#
# An argument is the value supplied
# when the function is called.

def greet_user(name):
    print("Hello,", name)


greet_user("Alex")
greet_user("Jordan")


# EXAMPLE 5: Function with Two Parameters

def display_student(name, major):
    print("Student:", name)
    print("Major:", major)


display_student("Alex", "Cyber Defense")


# EXAMPLE 6: Function with User Input

def ask_name():
    name = input("Enter your name: ")
    print("Welcome,", name)


ask_name()


# EXAMPLE 7: Function with a Calculation

def calculate_total(price, quantity):
    total = price * quantity
    print("Total cost: $", total)


calculate_total(75, 3)


# EXAMPLE 8: Function with a Return Statement
#
# return sends a result back to the
# location where the function was called.
#
# Unlike print(), return allows another
# part of the program to use the result.

def add_numbers(number1, number2):
    return number1 + number2


result = add_numbers(10, 20)

print("Sum:", result)


# EXAMPLE 9: Understanding print vs return

def show_total(price, quantity):
    print(price * quantity)


def get_total(price, quantity):
    return price * quantity


show_total(25, 4)

total = get_total(25, 4)

print("Stored total:", total)


# EXAMPLE 10: Function with if and else

def check_age(age):
    if age >= 18:
        print("Access granted.")
    else:
        print("Access denied.")


check_age(20)
check_age(15)


# EXAMPLE 11: Function with elif

def classify_grade(grade):
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


classify_grade(95)
classify_grade(82)
classify_grade(67)


# EXAMPLE 12: Flower Order Function

def check_flower_order(quantity):
    if quantity >= 25:
        print("Flower order accepted.")
    else:
        print("Minimum order is 25 roses.")


check_flower_order(50)
check_flower_order(12)


# EXAMPLE 13: Function with a Default Parameter
#
# Default parameters provide a value
# when no argument is supplied.

def welcome_customer(name="Customer"):
    print("Welcome,", name)


welcome_customer()
welcome_customer("Alex")


# EXAMPLE 14: Keyword Arguments
#
# Keyword arguments identify parameters
# by name when calling a function.

def display_order(customer, flowers, quantity):
    print("Customer:", customer)
    print("Flowers:", flowers)
    print("Quantity:", quantity)


display_order(
    customer="Alex",
    flowers="Roses",
    quantity=50
)


# EXAMPLE 15: Function Calling Another Function

def display_header():
    print("===== GOLDEN AURA FLORALS =====")


def display_message():
    display_header()
    print("Thank you for your order!")


display_message()


# EXAMPLE 16: Local Variables
#
# Variables created inside a function
# are normally local to that function.
#
# Local variables cannot usually
# be accessed outside their function.

def calculate_discount():
    discount = 10
    print("Discount:", discount)


calculate_discount()


# EXAMPLE 17: Returning Boolean Values

def is_adult(age):
    return age >= 18


result = is_adult(21)

print("Adult status:", result)


# EXAMPLE 18: Function with Multiple Returns
#
# A return statement immediately ends
# the function's execution.

def check_access(role):
    if role == "admin":
        return "Administrator access."
    elif role == "employee":
        return "Employee access."
    else:
        return "Access denied."


print(check_access("admin"))
print(check_access("guest"))


# EXAMPLE 19: Security Alert Function
#
# This is a simplified classification
# example for learning purposes.

def classify_alert(failed_attempts):
    if failed_attempts >= 20:
        return "Critical"
    elif failed_attempts >= 10:
        return "High"
    elif failed_attempts >= 5:
        return "Medium"
    elif failed_attempts > 0:
        return "Low"
    else:
        return "No Alert"


alert = classify_alert(12)

print("Security alert level:", alert)


# EXAMPLE 20: Combining Functions

def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate


def display_receipt(subtotal, tax):
    total = subtotal + tax

    print("===== RECEIPT =====")
    print("Subtotal: $", round(subtotal, 2))
    print("Tax: $", round(tax, 2))
    print("Total: $", round(total, 2))


subtotal = calculate_subtotal(65, 3)
tax = calculate_tax(subtotal, 0.08)

display_receipt(subtotal, tax)


# EXAMPLE 21: Main Function
#
# A main() function can organize the
# primary steps of a program.
#
# Python does not require main(),
# but it is a common design pattern.

def main():
    print("Starting the program.")
    print("Running application tasks.")
    print("Program completed.")


main()


# WHAT I LEARNED
#
# 1. Functions organize reusable code.
# 2. def creates a function.
# 3. Functions execute when called.
# 4. Parameters receive information.
# 5. Arguments provide actual values.
# 6. return sends a result to the caller.
# 7. print displays information.
# 8. Functions can contain conditions.
# 9. Functions can call other functions.
# 10. Local variables have limited scope.
# 11. Default parameters are optional values.
# 12. Functions improve code organization.
