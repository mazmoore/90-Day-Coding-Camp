
# ==========================================
# DAY 06 - PRACTICE EXERCISES
# Topic: Multiple Conditions Using elif
# ==========================================

# INSTRUCTIONS:
# Complete each exercise using if, elif,
# and else where appropriate.
#
# Use variables and user input.
# Display results using print().
#
# Leave answers blank until your review.


# EXERCISE 1: Grading System
#
# Ask the user for a numeric grade.
#
# 90-100 = A
# 80-89 = B
# 70-79 = C
# 60-69 = D
# Below 60 = F
#
# Display the letter grade.
# Reject grades outside 0-100.


# EXERCISE 2: Age Categories
#
# Ask the user for their age.
#
# Under 13 = Child
# 13-17 = Teen
# 18-64 = Adult
# 65+ = Senior
#
# Display the correct category.
# Reject negative ages.


# EXERCISE 3: Temperature Classification
#
# Ask the user for a temperature.
#
# 90 or above = Very Hot
# 75-89 = Warm
# 60-74 = Mild
# Below 60 = Cool


# EXERCISE 4: Flower Order Categories
#
# Ask how many roses the customer wants.
#
# Below 25 = Order denied
# 25-49 = Small arrangement
# 50-99 = Medium arrangement
# 100+ = Large arrangement


# EXERCISE 5: Shipping Calculator
#
# Ask for the order total.
#
# $150+ = Free express shipping
# $100-$149.99 = Free standard shipping
# $50-$99.99 = $5 shipping
# Below $50 = $10 shipping
#
# Reject negative order totals.


# EXERCISE 6: User Role System
#
# Ask for a user role.
#
# admin = Administrator access
# manager = Manager access
# employee = Employee access
# Any other role = Unknown role
#
# Ignore surrounding spaces and case.


# EXERCISE 7: Network Port Classification
#
# Ask the user for a port number.
#
# Below 0 or above 65535 = Invalid
# 0-1023 = Well-known
# 1024-49151 = Registered
# 49152-65535 = Dynamic/private


# EXERCISE 8: Password Length
#
# Ask the user to enter a test password.
#
# Under 8 characters = Very short
# 8-11 = Short
# 12-15 = Longer
# 16+ = 16 or more characters
#
# Use len() to measure the length.
# Do not use a real password.


# EXERCISE 9: Account Balance
#
# Create a variable for account balance.
#
# $1000+ = High balance
# $500-$999.99 = Moderate balance
# $0.01-$499.99 = Low balance
# $0 = Empty account
# Below $0 = Negative balance


# EXERCISE 10: Main Menu
#
# Display four menu choices:
#
# 1. View Account
# 2. Update Profile
# 3. Security Settings
# 4. Exit
#
# Ask the user to select a number.
# Display a message for each selection.
# Handle invalid selections.


# EXERCISE 11: Failed Login Alerts
#
# Ask for the number of failed logins.
#
# 20+ = Critical
# 10-19 = High
# 5-9 = Medium
# 1-4 = Low
# 0 = No alert
#
# Reject negative values.


# EXERCISE 12: System Status
#
# Ask the user for system status.
#
# online = Operational
# maintenance = Under maintenance
# offline = Unavailable
# Anything else = Unknown status


# EXERCISE 13: Logical Operators
#
# Ask for the user's age.
# Ask whether they have an ID.
#
# If age is 18+ AND they have an ID:
# Display "Verification passed."
#
# If age is 18+ but they have no ID:
# Display "Identification required."
#
# Otherwise:
# Display "Age requirement not met."


# EXERCISE 14: Debugging
#
# The following code has a logic error:
#
# grade = 95
#
# if grade >= 70:
#     print("C")
# elif grade >= 80:
#     print("B")
# elif grade >= 90:
#     print("A")
#
# Identify the problem.
# Rewrite the conditions in the
# correct order.


# EXERCISE 15: Boundary Testing
#
# Create a grading system.
#
# Test the following values:
# 59, 60, 69, 70, 79, 80, 89, 90
#
# Verify that each score receives
# the correct letter grade.


# EXERCISE 16: Independent Challenge
#
# Build a basic security alert classifier.
#
# Ask the user for:
# 1. Number of failed login attempts
# 2. Whether the account is locked
#
# Create at least four alert categories.
#
# Requirements:
# - Use if, elif, and else.
# - Use at least one logical operator.
# - Handle zero failed attempts.
# - Reject negative failed attempts.
# - Display a final alert category.
# - Add comments explaining your logic.