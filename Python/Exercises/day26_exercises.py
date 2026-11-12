
# ==========================================
# DAY 26 - PRACTICE EXERCISES
# Topic: Error Handling
# ==========================================

# INSTRUCTIONS:
#
# Complete each exercise using Python.
#
# Practice:
#
# try and except
# Exception types
# Multiple except blocks
# Exception messages
# else and finally
# raise
# Custom exceptions
# Exception chaining
# Data processing
# Safe conversions
# Flower order errors
# Security event errors
#
# Leave solutions blank until review.


# EXERCISE 1: Basic try/except
#
# Attempt to convert
# "abc" into an integer.
#
# Catch ValueError.
#
# Print a useful message.


# EXERCISE 2: Successful Conversion
#
# Convert "25" into an integer
# inside a try block.
#
# Print the converted value.


# EXERCISE 3: Division by Zero
#
# Attempt to divide 10 by zero.
#
# Catch ZeroDivisionError.
#
# Display an explanation.


# EXERCISE 4: TypeError
#
# Attempt to add
# a string and an integer.
#
# Catch TypeError.


# EXERCISE 5: IndexError
#
# Create a list containing
# three numbers.
#
# Attempt to access
# an invalid index.
#
# Catch IndexError.


# EXERCISE 6: KeyError
#
# Create a user dictionary.
#
# Attempt to access
# a missing key.
#
# Catch KeyError.


# EXERCISE 7: AttributeError
#
# Attempt to call a list method
# on an integer.
#
# Catch AttributeError.


# EXERCISE 8: Missing File
#
# Attempt to read
# a nonexistent text file.
#
# Catch FileNotFoundError.
#
# Do not create the file.


# EXERCISE 9: Multiple except Blocks
#
# Write code that may raise:
#
# ValueError
# ZeroDivisionError
#
# Handle each separately.


# EXERCISE 10: Grouped Exceptions
#
# Catch ValueError and TypeError
# using one except statement.


# EXERCISE 11: Exception Object
#
# Catch a ValueError
# using "as error".
#
# Display the error message.


# EXERCISE 12: Exception Type
#
# Catch an exception.
#
# Display the name
# of its exception class.


# EXERCISE 13: Conversion Messages
#
# Create a function that
# converts an age to an integer.
#
# Return None when conversion fails.
#
# Print a useful error message.


# EXERCISE 14: Safe Division
#
# Create a function that accepts
# two numbers.
#
# Return the division result.
#
# Return None when
# division by zero occurs.


# EXERCISE 15: Error Result Tuple
#
# Create a division function
# that returns:
#
# Success Boolean
# Result
# Error message


# EXERCISE 16: else Block
#
# Use try/except/else
# to convert a valid number.
#
# Print a success message
# inside else.


# EXERCISE 17: else After Failure
#
# Attempt an invalid conversion.
#
# Handle the exception.
#
# Verify that else
# does not execute.


# EXERCISE 18: finally Block
#
# Create a try/except/finally
# example using division.
#
# Display a cleanup message
# in finally.


# EXERCISE 19: finally with Failure
#
# Trigger a handled exception.
#
# Verify that finally
# still executes.


# EXERCISE 20: All Four Blocks
#
# Create a program using:
#
# try
# except
# else
# finally
#
# Explain when each block runs.


# EXERCISE 21: raise ValueError
#
# Create a function that
# requires a positive number.
#
# Raise ValueError
# when the number is invalid.


# EXERCISE 22: raise TypeError
#
# Create a function that
# requires string input.
#
# Raise TypeError
# for other types.


# EXERCISE 23: Quantity Exceptions
#
# Create a function that validates
# an order quantity.
#
# Raise TypeError
# for invalid types.
#
# Raise ValueError
# for invalid numeric values.


# EXERCISE 24: Missing Product
#
# Create a product catalog.
#
# Create a function that raises
# KeyError when a product ID
# does not exist.


# EXERCISE 25: Re-Raising Exceptions
#
# Create a function that
# catches ValueError.
#
# Print a message.
#
# Re-raise the exception.
#
# Handle it in the caller.


# EXERCISE 26: Custom Exception
#
# Create a custom exception
# named InvalidOrderError.
#
# Raise and catch it.


# EXERCISE 27: Inventory Exception
#
# Create a custom exception
# named InsufficientStockError.
#
# Raise it when requested
# inventory exceeds stock.


# EXERCISE 28: Exception Hierarchy
#
# Create a base exception:
#
# FlowerOrderError
#
# Create a child exception:
#
# InvalidProductError
#
# Catch the child using
# the base exception class.


# EXERCISE 29: Exception Chaining
#
# Create a function that
# converts a quantity.
#
# When conversion fails,
# raise a custom exception
# using "raise ... from ...".
#
# Inspect the original cause.


# EXERCISE 30: Custom Error Details
#
# Create a ValidationError
# exception class.
#
# Store:
#
# Field name
# Error message
#
# Display both values.


# EXERCISE 31: Invalid List Values
#
# Create a list containing
# numeric and invalid strings.
#
# Convert valid values.
#
# Skip invalid values
# using exception handling.


# EXERCISE 32: Count Errors
#
# Create a list of values.
#
# Attempt integer conversions.
#
# Count conversion failures.


# EXERCISE 33: Separate Valid and Invalid
#
# Create a function that accepts
# a list of values.
#
# Return:
#
# Valid converted integers
# Rejected original values


# EXERCISE 34: Safe Dictionary Access
#
# Create a dictionary
# missing an optional key.
#
# Use get() to provide
# a default value.


# EXERCISE 35: Safe List Access
#
# Create a function that accepts
# a list and an index.
#
# Return the matching element.
#
# Return None for invalid indices.


# EXERCISE 36: Nested Dictionary Errors
#
# Create a nested dictionary.
#
# Attempt to access
# a missing nested key.
#
# Handle the error safely.


# EXERCISE 37: Safe Float Conversion
#
# Create a function that
# converts a value to float.
#
# Catch expected conversion errors.
#
# Return None when invalid.


# EXERCISE 38: Nonfinite Values
#
# Create a function that
# converts numeric input.
#
# Reject:
#
# NaN
# Positive infinity
# Negative infinity
#
# Use math.isfinite().


# EXERCISE 39: Decimal Conversion
#
# Import Decimal.
#
# Create a function that
# safely converts a price.
#
# Reject invalid, negative,
# or nonfinite values.


# EXERCISE 40: Safe File Reading
#
# Create a function that
# attempts to read a text file.
#
# Catch:
#
# FileNotFoundError
# PermissionError
#
# Return None on failure.


# EXERCISE 41: Flower Price Error
#
# Create a function that
# validates flower prices.
#
# Raise ValueError
# for invalid prices.


# EXERCISE 42: Flower Inventory Error
#
# Create a function that
# reserves flower inventory.
#
# Raise a custom exception
# when stock is insufficient.


# EXERCISE 43: Safe Order Subtotal
#
# Create a function that accepts:
#
# Price
# Quantity
#
# Validate both.
#
# Calculate a subtotal.
#
# Handle invalid inputs.


# EXERCISE 44: Multiple Flower Orders
#
# Create a list of sample orders.
#
# Include valid and invalid orders.
#
# Process them using a loop.
#
# Continue after invalid orders.


# EXERCISE 45: Order Result Dictionary
#
# Create a function that
# processes a flower order.
#
# Return a dictionary containing:
#
# Accepted status
# Subtotal when valid
# Error message when invalid


# EXERCISE 46: Network Port Exceptions
#
# Create a function that accepts
# a network port.
#
# Allow integers or digit strings.
#
# Reject Booleans.
#
# Reject values outside 1-65535.
#
# Raise meaningful exceptions.


# EXERCISE 47: IP Address Exceptions
#
# Use ipaddress.
#
# Create a function that
# validates IP address syntax.
#
# Raise ValueError
# for invalid addresses.
#
# Use synthetic IP addresses.


# EXERCISE 48: Security Event Validation
#
# Create a function that validates
# a security event dictionary.
#
# Require:
#
# Event type
# Source IP
# Severity
#
# Raise exceptions for
# missing or invalid fields.


# EXERCISE 49: Security Record Processing
#
# Create a list of synthetic
# security event records.
#
# Include valid and invalid data.
#
# Separate accepted and rejected
# records using exception handling.
#
# Return a summary dictionary.


# EXERCISE 50: Independent Challenge
#
# Build a reliable security event
# validation and reporting system.
#
# Requirements:
#
# 1. Create at least 15 synthetic events.
# 2. Use documentation IP ranges.
# 3. Store events as dictionaries.
# 4. Include event types.
# 5. Include source IP addresses.
# 6. Include severity levels.
# 7. Include timestamps.
# 8. Create at least six functions.
# 9. Validate required fields.
# 10. Validate event types.
# 11. Validate severity values.
# 12. Validate IP address syntax.
# 13. Validate timestamp formats.
# 14. Use try and except.
# 15. Catch specific exceptions.
# 16. Use else for successful records.
# 17. Use finally for a cleanup
#     or completion message.
# 18. Create a custom exception.
# 19. Raise custom exceptions
#     for invalid records.
# 20. Use exception chaining.
# 21. Preserve original records.
# 22. Separate accepted records.
# 23. Separate rejected records.
# 24. Count failed login events.
# 25. Count rejected events.
# 26. Identify unique source IPs.
# 27. Count events by severity.
# 28. Return a structured report.
# 29. Display a formatted report.
# 30. Handle an empty event list.
# 31. Continue after invalid records.
# 32. Avoid exposing sensitive details.
# 33. Document error-handling decisions.
# 34. Explain why catching
#     Exception broadly may hide bugs.
# 35. Keep all records synthetic.
#
# Write the program independently.
