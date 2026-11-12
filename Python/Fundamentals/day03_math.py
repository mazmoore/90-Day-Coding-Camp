
# ==========================================
# DAY 03 - ARITHMETIC OPERATORS
# Topic: Mathematical Expressions in Python
# ==========================================

# LESSON NOTES
#
# Arithmetic operators allow Python to perform
# mathematical calculations.
#
# Python supports addition, subtraction,
# multiplication, division, exponentiation,
# floor division, and modulus.
#
# Arithmetic expressions can use numbers
# directly or values stored in variables.


# EXAMPLE 1: Addition (+)

number1 = 15
number2 = 10

sum_result = number1 + number2

print("Addition:", sum_result)


# EXAMPLE 2: Subtraction (-)

balance = 100
purchase = 35

remaining_balance = balance - purchase

print("Remaining balance:", remaining_balance)


# EXAMPLE 3: Multiplication (*)

price = 25
quantity = 4

total = price * quantity

print("Total cost:", total)


# EXAMPLE 4: Division (/)

total_amount = 100
people = 4

amount_per_person = total_amount / people

print("Amount per person:", amount_per_person)


# EXAMPLE 5: Floor Division (//)
#
# Floor division rounds the quotient down
# to the nearest whole number.
#
# For positive numbers, this removes
# the fractional portion.

result = 17 // 5

print("Floor division:", result)


# EXAMPLE 6: Modulus (%)
#
# The modulus operator returns the remainder
# after division.

remainder = 17 % 5

print("Remainder:", remainder)


# EXAMPLE 7: Exponentiation (**)
#
# Exponentiation raises a number to a power.

power_result = 2 ** 3

print("Exponentiation:", power_result)


# EXAMPLE 8: Order of Operations
#
# Python follows mathematical precedence.
#
# Parentheses are evaluated first.
# Multiplication and division have higher
# precedence than addition and subtraction.

calculation1 = 5 + 3 * 2
calculation2 = (5 + 3) * 2

print("Without parentheses:", calculation1)
print("With parentheses:", calculation2)


# EXAMPLE 9: Updating Variables
#
# Arithmetic can be used to change
# values stored in variables.

score = 50

score = score + 10

print("Updated score:", score)


# EXAMPLE 10: Assignment Operators
#
# += adds to the existing value.
# -= subtracts from the existing value.
# *= multiplies the existing value.
# /= divides the existing value.

points = 20

points += 5
print("After addition:", points)

points -= 3
print("After subtraction:", points)

points *= 2
print("After multiplication:", points)

points /= 2
print("After division:", points)


# EXAMPLE 11: Working with Floats

product_price = 19.99
quantity = 3

subtotal = product_price * quantity

print("Subtotal:", subtotal)


# EXAMPLE 12: Simple Business Calculation
#
# Calculate revenue from flower sales.

bouquet_price = 75
bouquets_sold = 8

revenue = bouquet_price * bouquets_sold

print("Flower sales revenue:", revenue)


# EXAMPLE 13: Calculate Profit
#
# Profit = Revenue - Expenses

revenue = 600
expenses = 275

profit = revenue - expenses

print("Business profit:", profit)


# WHAT I LEARNED
#
# 1. + performs addition.
# 2. - performs subtraction.
# 3. * performs multiplication.
# 4. / performs division and returns a float.
# 5. // performs floor division.
# 6. % returns the remainder.
# 7. ** performs exponentiation.
# 8. Parentheses control calculation order.
# 9. Assignment operators update variables.
# 10. Arithmetic is useful in real programs.
