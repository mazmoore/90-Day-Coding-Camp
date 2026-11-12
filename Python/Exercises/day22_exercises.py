
# ==========================================
# DAY 22 - PRACTICE EXERCISES
# Topic: Variable Scope
# ==========================================

# INSTRUCTIONS:
#
# Complete each exercise using Python.
#
# Practice:
# Local variables
# Global variables
# Enclosing scope
# Built-in scope
# Variable shadowing
# global
# nonlocal
# Nested functions
# Closures
# Mutable arguments
# Avoiding shared state
# Cybersecurity applications
#
# Leave solutions blank until your review.


# EXERCISE 1: Local Variable
#
# Create a function containing
# a local message variable.
#
# Print the message
# inside the function.


# EXERCISE 2: Separate Local Variables
#
# Create two functions.
#
# Give each function a local
# variable named message.
#
# Print both values.


# EXERCISE 3: Local Variable Lifetime
#
# Create a function containing
# a local variable.
#
# Call the function.
#
# Explain why accessing the
# variable outside the function
# would raise NameError.
#
# Keep error-producing code
# commented out.


# EXERCISE 4: Global Variable
#
# Create a module-level variable
# containing a programming language.
#
# Read it inside a function.


# EXERCISE 5: Read a Global
#
# Create a global application name.
#
# Display it from a function
# without using global.


# EXERCISE 6: Local and Global Names
#
# Create a global status variable.
#
# Create a function containing
# a local variable with
# the same name.
#
# Print both values.


# EXERCISE 7: Variable Shadowing
#
# Create a global username.
#
# Create a function containing
# a different local username.
#
# Demonstrate which value
# is used inside the function.


# EXERCISE 8: Local Parameters
#
# Create a function accepting
# a student's name.
#
# Explain why the parameter
# is a local name.


# EXERCISE 9: Reusing Parameter Names
#
# Create two functions.
#
# Both should use a parameter
# named name.
#
# Call both functions
# with different values.


# EXERCISE 10: Return a Local Value
#
# Create a function that
# calculates a total.
#
# Store the result in
# a local variable.
#
# Return the value.


# EXERCISE 11: Avoid a Global
#
# Create a function that
# accepts a course name.
#
# Pass the course name
# as an argument instead
# of reading a global variable.


# EXERCISE 12: Update with return
#
# Create a function that accepts
# a counter value.
#
# Increase the counter by one.
#
# Return the updated value.
#
# Assign the result
# to the caller's variable.


# EXERCISE 13: Using global
#
# Create a global counter.
#
# Create a function that
# increases the counter.
#
# Use the global statement.
#
# Call the function twice.


# EXERCISE 14: Read Without global
#
# Create a global variable
# containing a maximum
# attempt count.
#
# Read the value inside
# a function without global.


# EXERCISE 15: Avoid Global State
#
# Rewrite a global counter
# example using parameters
# and return values instead.


# EXERCISE 16: Enclosing Scope
#
# Create an outer function
# containing a message variable.
#
# Create an inner function
# that reads the message.
#
# Call the inner function.


# EXERCISE 17: Shadow Enclosing Variable
#
# Create nested functions.
#
# Use the same variable name
# in the outer and inner functions.
#
# Display both values.


# EXERCISE 18: Using nonlocal
#
# Create an outer function
# containing a counter.
#
# Create an inner function
# that increases the counter.
#
# Use nonlocal.


# EXERCISE 19: Nested Function
#
# Create a function that
# defines another function.
#
# Use the inner function
# to display a report title.


# EXERCISE 20: Return a Function
#
# Create an outer function
# containing a greeting.
#
# Return an inner function
# that returns the greeting.
#
# Call the returned function.


# EXERCISE 21: Closure
#
# Create a function that accepts
# a multiplication factor.
#
# Return an inner function
# that multiplies by that factor.
#
# Create separate double
# and triple functions.


# EXERCISE 22: Closure with nonlocal
#
# Create a counter factory.
#
# Use nonlocal inside
# the returned function.
#
# Call the counter three times.


# EXERCISE 23: Independent Closures
#
# Create two independent
# counters using a factory.
#
# Demonstrate that each
# counter maintains
# separate state.


# EXERCISE 24: Built-in Scope
#
# Create a list containing
# five cybersecurity tools.
#
# Use len() to display
# the number of tools.
#
# Explain why len()
# is available.


# EXERCISE 25: Avoid Built-in Shadowing
#
# Create a list of numbers.
#
# Calculate the sum.
#
# Do not use sum, list,
# or dict as variable names.


# EXERCISE 26: LEGB Resolution
#
# Create nested functions.
#
# Use the same variable name
# in multiple scopes.
#
# Demonstrate which value
# Python resolves first.


# EXERCISE 27: Global Fallback
#
# Create a global report title.
#
# Create a function that
# reads the title without
# defining a local version.


# EXERCISE 28: UnboundLocalError
#
# Write a commented example
# that would cause
# UnboundLocalError.
#
# Explain why Python treats
# the variable as local.
#
# Do not run the broken code.


# EXERCISE 29: Correct a Scope Problem
#
# Create a function that accepts
# a numeric score.
#
# Return the score increased by 10.
#
# Update the caller's variable.


# EXERCISE 30: Mutable List Argument
#
# Create a function that accepts
# a list of cybersecurity tools.
#
# Append a new tool.
#
# Display the original list
# after the function call.


# EXERCISE 31: Avoid List Mutation
#
# Create a function that accepts
# a list of tools.
#
# Copy the list.
#
# Add a new tool to the copy.
#
# Return the updated list.
#
# Preserve the original.


# EXERCISE 32: Dictionary Mutation
#
# Create a function that accepts
# a user dictionary.
#
# Change the active status.
#
# Observe the caller's dictionary.


# EXERCISE 33: Copy a Dictionary
#
# Create a function that accepts
# a user dictionary.
#
# Copy the dictionary.
#
# Update the role or status.
#
# Return the new dictionary.
#
# Preserve the original.


# EXERCISE 34: Loop Scope
#
# Create a for loop at module level.
#
# Print the loop variable
# after the loop finishes.
#
# Explain the result.


# EXERCISE 35: if Statement Scope
#
# Create an if statement
# containing a variable assignment.
#
# Print the variable afterward.
#
# Explain why the variable
# remains accessible.


# EXERCISE 36: Comprehension Scope
#
# Create a list comprehension
# that calculates squares.
#
# Explain how its iteration
# variable is scoped in Python 3.


# EXERCISE 37: Separate Function Calls
#
# Create a function that
# calculates the square
# of a number.
#
# Call it three times
# with different arguments.


# EXERCISE 38: Recursion and Scope
#
# Create a recursive countdown
# function with a base case.
#
# Explain how each call
# has its own local parameter.
#
# Keep the countdown small.


# EXERCISE 39: Constant Convention
#
# Create an uppercase variable
# for maximum login attempts.
#
# Read the value inside a function.
#
# Explain why uppercase names
# are a convention rather than
# enforced immutability.


# EXERCISE 40: Configuration Parameters
#
# Create a function that accepts
# a server name and port.
#
# Pass configuration values
# as arguments.
#
# Avoid reading global settings.


# EXERCISE 41: Flower Inventory
#
# Create a function that accepts:
#
# Current flower quantity
# Quantity sold
#
# Return the remaining quantity.
#
# Update the caller's variable.


# EXERCISE 42: Bouquet Pricing
#
# Create a function that accepts:
#
# Bouquet price
# Quantity
#
# Calculate a local subtotal.
#
# Return the subtotal.


# EXERCISE 43: Customer Order Total
#
# Create a function that accepts
# a list of order item dictionaries.
#
# Calculate the total
# using local variables.
#
# Return the result.


# EXERCISE 44: Failed Login Counter
#
# Create a function that accepts
# a list of security event types.
#
# Use a local counter.
#
# Return the number
# of failed logins.


# EXERCISE 45: Security Configuration
#
# Create a function that accepts:
#
# List of events
# Configuration dictionary
#
# Return a summary dictionary.
#
# Do not depend on
# global configuration values.


# EXERCISE 46: Independent Event Counters
#
# Create a function that returns
# an event counter closure.
#
# Use nonlocal to track
# the event count.
#
# Create separate counters
# for two training servers.


# EXERCISE 47: Independent Reports
#
# Create a function that accepts
# a list of event types.
#
# Return a frequency dictionary.
#
# Call it with two different lists.
#
# Verify the reports are independent.


# EXERCISE 48: Test Separate Calls
#
# Create a function that accepts
# a list of numbers.
#
# Return the sum.
#
# Call the function with
# two different lists.
#
# Verify the results.


# EXERCISE 49: Nested Security Function
#
# Create an outer function
# that accepts security events.
#
# Define two inner functions:
#
# One counts total events.
# One counts unique source IPs.
#
# Return a summary dictionary.


# EXERCISE 50: Independent Challenge
#
# Build a security event
# analyzer demonstrating scope.
#
# Requirements:
#
# 1. Create at least 12 event records.
# 2. Store events in a list.
# 3. Represent each event
#    using a dictionary.
# 4. Include event type.
# 5. Include username.
# 6. Include source IP.
# 7. Include sample timestamps.
# 8. Use documentation IP ranges.
# 9. Create at least five functions.
# 10. Use local variables.
# 11. Pass data through parameters.
# 12. Return calculated results.
# 13. Demonstrate a nested function.
# 14. Demonstrate enclosing scope.
# 15. Create an independent counter
#     using nonlocal.
# 16. Count events by category.
# 17. Count failed login events.
# 18. Identify unique source IPs.
# 19. Return a nested report dictionary.
# 20. Display a formatted report.
# 21. Preserve original event records.
# 22. Avoid mutable global report state.
# 23. Add comments explaining scope.
#
# Write the program independently.
