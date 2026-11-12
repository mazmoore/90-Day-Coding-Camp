
# ==========================================
# DAY 24 - PRACTICE EXERCISES
# Topic: Input Validation
# ==========================================

# INSTRUCTIONS:
#
# Complete each exercise using Python.
#
# Practice:
# Type validation
# String validation
# Numeric validation
# Range validation
# Allowed selections
# Safe conversions
# Validation functions
# Error messages
# Dictionary validation
# Repeated input
# Business order validation
# Cybersecurity record validation
#
# Leave solutions blank until your review.


# EXERCISE 1: Basic Validation
#
# Create an age variable.
#
# Check whether the value
# is at least 18.
#
# Print the result.


# EXERCISE 2: Type Checking
#
# Create a numeric variable.
#
# Use isinstance() to check
# whether it is an integer.


# EXERCISE 3: Reject Boolean Integers
#
# Create a function that accepts
# a value.
#
# Return True only when
# the value is an integer
# and is not a Boolean.


# EXERCISE 4: String Validation
#
# Create a username variable.
#
# Check whether the value
# is a string.


# EXERCISE 5: Empty Strings
#
# Create an empty string.
#
# Check whether it contains
# any characters.
#
# Print the result.


# EXERCISE 6: Whitespace Removal
#
# Create a username with
# spaces before and after it.
#
# Use strip() to clean it.


# EXERCISE 7: Whitespace-Only Input
#
# Create a string containing
# only spaces.
#
# Reject the value when
# it becomes empty
# after stripping whitespace.


# EXERCISE 8: Minimum Length
#
# Create a sample password.
#
# Check whether its length
# is at least 12 characters.
#
# Do not use a real password.


# EXERCISE 9: Maximum Length
#
# Create a username.
#
# Check whether it contains
# no more than 20 characters.


# EXERCISE 10: Combined Length Rules
#
# Create a function that
# accepts a username.
#
# Return True only when
# its length is between
# 3 and 20 characters.
#
# Reject non-string values.


# EXERCISE 11: Alphabetic Input
#
# Create a name variable.
#
# Use isalpha() to check
# whether all characters
# are letters.


# EXERCISE 12: Numeric Strings
#
# Create a quantity string.
#
# Use isdigit() to check
# whether it contains digits.


# EXERCISE 13: Alphanumeric Input
#
# Create a username containing
# letters and numbers.
#
# Use isalnum() to check it.


# EXERCISE 14: Normalize Input
#
# Create a response containing
# uppercase letters and spaces.
#
# Normalize the response
# using strip() and casefold().


# EXERCISE 15: Allowed Responses
#
# Create a set containing
# "yes" and "no".
#
# Check whether a response
# is one of the allowed values.


# EXERCISE 16: Menu Selection
#
# Create menu options:
#
# 1
# 2
# 3
#
# Validate a user's
# selection against the options.


# EXERCISE 17: Numeric Range
#
# Create a quantity variable.
#
# Check whether it is
# between 1 and 100.


# EXERCISE 18: Negative Quantity
#
# Create an inventory quantity.
#
# Reject the value
# when it is negative.


# EXERCISE 19: Price Validation
#
# Create a function that accepts
# a product price.
#
# Return True only when
# the price is numeric,
# is not a Boolean,
# and is not negative.
#
# Consider how special float
# values might affect validation.


# EXERCISE 20: Float Conversion
#
# Create a numeric price string.
#
# Convert it to a float.
#
# Print the converted value.


# EXERCISE 21: Safe Integer Conversion
#
# Create a function that
# converts a value to int.
#
# Catch expected conversion errors.
#
# Return None when conversion fails.


# EXERCISE 22: Safe Float Conversion
#
# Create a function that
# converts a value to float.
#
# Catch expected conversion errors.
#
# Return None when conversion fails.


# EXERCISE 23: Validate After Conversion
#
# Create a function that accepts
# a quantity string.
#
# Convert it safely.
#
# Return True only when
# the resulting quantity
# is between 1 and 100.


# EXERCISE 24: Strict Quantity Parsing
#
# Create a function that accepts
# a quantity string.
#
# Reject:
#
# Decimal values
# Negative values
# Letters
# Empty strings
#
# Accept nonnegative
# whole-number strings.


# EXERCISE 25: Optional Notes
#
# Create a function that accepts
# an optional customer note.
#
# Accept None.
#
# Accept strings no longer
# than 200 characters.
#
# Reject other values.


# EXERCISE 26: Validation Messages
#
# Create a function that
# validates an age.
#
# Return:
#
# Boolean result
# Explanation message
#
# Reject non-integer ages
# and ages below 18.


# EXERCISE 27: Early Return
#
# Create a product name
# validation function.
#
# Reject non-string input.
# Reject empty input.
# Reject names over 50 characters.
#
# Use early returns.


# EXERCISE 28: Username Rules
#
# Create a function that accepts
# a username.
#
# Require:
#
# String input
# Length from 3 to 20
# ASCII letters, digits,
# or underscores only
#
# Return a Boolean result.


# EXERCISE 29: Required Dictionary Keys
#
# Create a function that checks
# whether a dictionary contains:
#
# username
# role
# active
#
# Return True only when
# all keys are present.


# EXERCISE 30: Dictionary Value Validation
#
# Create a function that validates
# a user dictionary.
#
# Check:
#
# Username format
# Allowed role
# Boolean active status
#
# Reject invalid records.


# EXERCISE 31: List Validation
#
# Create a function that accepts
# a list of cybersecurity tools.
#
# Require a nonempty list.
#
# Require every element
# to be a nonempty string.


# EXERCISE 32: Filter Valid Records
#
# Create a list of user dictionaries.
#
# Include valid and invalid records.
#
# Use a validation function
# to return only valid users.


# EXERCISE 33: Repeated Input
#
# Create a list of simulated
# user responses.
#
# Some responses should be invalid.
#
# Use a loop to find
# the first valid quantity.
#
# Avoid an infinite loop.


# EXERCISE 34: Limited Attempts
#
# Create a list of simulated
# yes/no responses.
#
# Allow a maximum of
# three validation attempts.
#
# Stop when a valid
# response is found.


# EXERCISE 35: Menu Validator
#
# Create a reusable function
# that accepts:
#
# Selection
# Set of allowed options
#
# Return True only when
# the selection is allowed.


# EXERCISE 36: Email Format
#
# Create a function that performs
# a basic email format check.
#
# Check:
#
# Exactly one @ symbol
# Nonempty local part
# Domain containing a dot
#
# Explain why this does not
# verify email ownership.


# EXERCISE 37: Date Validation
#
# Create a function that accepts
# a date string.
#
# Use datetime.strptime()
# to check the format
# YYYY-MM-DD.
#
# Reject impossible dates.


# EXERCISE 38: Network Port Validation
#
# Create a function that accepts
# a network port value.
#
# Require an integer
# between 1 and 65535.
#
# Reject Boolean values.


# EXERCISE 39: IP Address Validation
#
# Import ipaddress.
#
# Create a function that
# validates IP address syntax.
#
# Test valid and invalid
# synthetic IP addresses.


# EXERCISE 40: Security Event Types
#
# Create a set containing:
#
# login_success
# login_failed
# port_scan
# file_access
#
# Create a function that
# accepts only these values.


# EXERCISE 41: Flower Quantity
#
# Create a function that
# validates flower quantities.
#
# Accept integers from 1 to 100.
#
# Reject negative quantities,
# zero, decimals, and Booleans.


# EXERCISE 42: Flower Product Selection
#
# Create a function that
# validates bouquet selections.
#
# Allowed products:
#
# Rose Bouquet
# Tulip Bouquet
# Mixed Bouquet
#
# Normalize case and whitespace.


# EXERCISE 43: Delivery Area
#
# Create a function that
# validates delivery cities.
#
# Allowed training cities:
#
# Las Cruces
# El Paso
#
# Reject unsupported cities.


# EXERCISE 44: Customer Name
#
# Create a function that
# validates a customer name.
#
# Require:
#
# String input
# Nonempty after strip()
# Length between 2 and 60


# EXERCISE 45: Flower Order Record
#
# Create a function that
# validates an order dictionary.
#
# Required fields:
#
# customer
# product
# quantity
# delivery_city
#
# Use your earlier
# validation functions.


# EXERCISE 46: Security Event Record
#
# Create a function that
# validates a security event.
#
# Required fields:
#
# event_type
# source_ip
# severity
#
# Validate each field.
#
# Use documentation IP ranges.


# EXERCISE 47: Separate Records
#
# Create a list containing
# valid and invalid security events.
#
# Return two lists:
#
# Valid records
# Invalid records
#
# Do not silently discard
# invalid records.


# EXERCISE 48: Fail-Closed Decision
#
# Create a simulated
# access request validator.
#
# Require:
#
# Active Boolean status
# Locked Boolean status
# Allowed role
#
# Reject missing or invalid data.
#
# Never grant access by default.


# EXERCISE 49: Validation Errors
#
# Create a function that
# validates a flower order.
#
# Return:
#
# Boolean result
# List of error messages
#
# Report every invalid field
# instead of stopping
# after the first error.


# EXERCISE 50: Independent Challenge
#
# Build a reusable flower
# ordering validation system.
#
# Requirements:
#
# 1. Create a product catalog.
# 2. Store product names and prices.
# 3. Create at least five sample orders.
# 4. Include valid and invalid orders.
# 5. Represent orders as dictionaries.
# 6. Require customer names.
# 7. Validate product selections.
# 8. Validate order quantities.
# 9. Validate delivery cities.
# 10. Reject unsupported products.
# 11. Reject negative quantities.
# 12. Reject zero quantities.
# 13. Reject non-integer quantities.
# 14. Reject missing required fields.
# 15. Normalize product selections.
# 16. Normalize delivery city names.
# 17. Return useful error messages.
# 18. Separate valid and invalid orders.
# 19. Calculate subtotals only
#     for valid orders.
# 20. Return structured order summaries.
# 21. Display accepted orders.
# 22. Display rejected orders
#     with explanations.
# 23. Use at least six functions.
# 24. Use Boolean return values.
# 25. Use early returns.
# 26. Use loops and conditionals.
# 27. Avoid unnecessary global state.
# 28. Preserve original order records.
# 29. Add comments explaining validation.
# 30. Do not use real payment information.
#
# Write the program independently.
