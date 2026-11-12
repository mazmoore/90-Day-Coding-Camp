
# ==========================================
# DAY 30 - PRACTICE EXERCISES
# Topic: Python Modules
# ==========================================

# INSTRUCTIONS:
#
# Complete each exercise using Python.
#
# Practice:
#
# import
# from ... import
# as
# Module namespaces
# Standard library modules
# Custom modules
# Import error handling
# __name__
# __main__
# Packages
# __init__.py
# Reusable functions
# Modular cybersecurity tools
#
# Leave solutions blank
# until returning to the lessons.
#
# Use synthetic data only.


# EXERCISE 1: Import math
#
# Import the math module.
#
# Calculate the square root of 64.


# EXERCISE 2: Module Constants
#
# Import math.
#
# Display the value of math.pi.


# EXERCISE 3: Factorial
#
# Use the math module
# to calculate 5 factorial.


# EXERCISE 4: Specific Import
#
# Import ceil from math.
#
# Round 4.2 upward.


# EXERCISE 5: Multiple Imports
#
# Import floor and trunc.
#
# Demonstrate both functions.


# EXERCISE 6: Module Alias
#
# Import math using an alias.
#
# Calculate the square root of 81.


# EXERCISE 7: Function Alias
#
# Import sqrt using
# a custom alias.
#
# Calculate the square root of 49.


# EXERCISE 8: Module Namespace
#
# Use math.pow()
# to calculate 2 raised to 3.


# EXERCISE 9: Module Name
#
# Import math.
#
# Display math.__name__.


# EXERCISE 10: dir()
#
# Use dir() on math.
#
# Check whether sqrt
# appears in the result.


# EXERCISE 11: Random Module
#
# Import random.
#
# Generate a random integer.
#
# Explain why random is not
# appropriate for passwords.


# EXERCISE 12: Statistics Mean
#
# Import statistics.
#
# Calculate the mean
# of five numbers.


# EXERCISE 13: Median
#
# Use statistics.median()
# on a list of numbers.


# EXERCISE 14: JSON Serialization
#
# Import json.
#
# Convert a dictionary
# into a JSON string.


# EXERCISE 15: JSON Parsing
#
# Create a JSON string.
#
# Convert it into
# a Python dictionary.


# EXERCISE 16: Counter
#
# Import Counter.
#
# Count repeated event types.


# EXERCISE 17: Decimal
#
# Import Decimal.
#
# Calculate the subtotal
# of a fictional flower order.


# EXERCISE 18: Datetime
#
# Import datetime.
#
# Create a timestamp.
#
# Display it in ISO format.


# EXERCISE 19: pathlib
#
# Import Path.
#
# Create a temporary
# training text file.
#
# Confirm the file exists.


# EXERCISE 20: CSV Module
#
# Import csv.
#
# Write a CSV header
# and one data row.


# EXERCISE 21: Module Documentation
#
# Import math.
#
# Inspect math.__doc__.
#
# Explain what it contains.


# EXERCISE 22: Module File
#
# Import json.
#
# Use getattr() to retrieve
# its __file__ attribute.
#
# Explain why some modules
# do not have __file__.


# EXERCISE 23: Module Dictionary
#
# Inspect math.__dict__.
#
# Check whether sqrt
# is available.


# EXERCISE 24: hasattr()
#
# Use hasattr()
# to check whether math
# contains factorial.


# EXERCISE 25: getattr()
#
# Use getattr()
# to retrieve math.sqrt.
#
# Call the function.


# EXERCISE 26: sys.modules
#
# Import sys and math.
#
# Check whether math
# appears in sys.modules.


# EXERCISE 27: Python Version
#
# Import sys.
#
# Display the major
# and minor Python version.


# EXERCISE 28: Import Paths
#
# Inspect sys.path.
#
# Explain what the paths
# are used for.


# EXERCISE 29: Module Availability
#
# Use importlib.util.find_spec()
# to check whether
# the json module exists.


# EXERCISE 30: Import Errors
#
# Attempt to import
# a nonexistent module.
#
# Catch ModuleNotFoundError.


# EXERCISE 31: Custom Module
#
# Create a separate Python file.
#
# Define a constant inside it.
#
# Import the module
# into another Python file.


# EXERCISE 32: Custom Function
#
# Create a helper module.
#
# Add a function that
# calculates order subtotals.
#
# Import and call it.


# EXERCISE 33: Text Formatter
#
# Create a helper module
# containing a function
# that formats product names.
#
# Import and use it.


# EXERCISE 34: Inventory Validator
#
# Create a custom module.
#
# Add a function that
# checks inventory availability.
#
# Import the function.


# EXERCISE 35: Specific Custom Import
#
# Create a helper module.
#
# Import one function
# using from ... import.


# EXERCISE 36: Alias Custom Function
#
# Create a custom function
# in another Python file.
#
# Import it using an alias.


# EXERCISE 37: Custom Namespace
#
# Create a custom module.
#
# Use dir() to inspect
# its available names.


# EXERCISE 38: Module Cache
#
# Import a custom module.
#
# Import it again
# using importlib.import_module().
#
# Compare the module objects.


# EXERCISE 39: Main Guard
#
# Create a custom Python module.
#
# Define a function.
#
# Add a main guard.
#
# Compare direct execution
# with importing the module.


# EXERCISE 40: Reload Module
#
# Create a simple custom module.
#
# Import it.
#
# Use importlib.reload().
#
# Explain what reload does.


# EXERCISE 41: Create Package
#
# Create a Python package folder.
#
# Add __init__.py.
#
# Define a package constant.
#
# Import the package.


# EXERCISE 42: Package Validator
#
# Create a validators.py module
# inside a package.
#
# Add an IP validation function.
#
# Import and use it.


# EXERCISE 43: Severity Validator
#
# Add a function that checks
# allowed severity values.
#
# Import it from a package.


# EXERCISE 44: Analyzer Module
#
# Create an analyzers.py module.
#
# Add a function that counts
# security event types.
#
# Import and call it.


# EXERCISE 45: Failed Login Counter
#
# Add a reusable function
# that counts failed logins.
#
# Import it from
# an analyzer module.


# EXERCISE 46: Nested Import
#
# Import a function using
# a package.module path.
#
# Demonstrate the result.


# EXERCISE 47: Package Namespace
#
# Import a package submodule.
#
# Display its __name__ value.


# EXERCISE 48: Package Path
#
# Import a package.
#
# Inspect its __path__.
#
# Explain what the path represents.


# EXERCISE 49: Combine Modules
#
# Create two custom modules:
#
# validators.py
# analyzers.py
#
# Validate synthetic events.
#
# Count accepted event types.
#
# Display the results.


# EXERCISE 50: Independent Challenge
#
# Build a modular security
# event analysis application.
#
# Requirements:
#
# 1. Create a main.py file.
# 2. Create a security_tools package.
# 3. Include __init__.py.
# 4. Create validators.py.
# 5. Create analyzers.py.
# 6. Create reports.py.
# 7. Create at least 20 synthetic events.
# 8. Use documentation IP ranges.
# 9. Include event timestamps.
# 10. Include source IP addresses.
# 11. Include event types.
# 12. Include severity levels.
# 13. Include valid records.
# 14. Include invalid records.
# 15. Create at least eight functions.
# 16. Validate required fields.
# 17. Validate IP addresses.
# 18. Validate event types.
# 19. Validate severity levels.
# 20. Validate timestamp formats.
# 21. Separate accepted records.
# 22. Separate rejected records.
# 23. Count total records.
# 24. Count accepted records.
# 25. Count rejected records.
# 26. Count failed logins.
# 27. Count port scans.
# 28. Count events by severity.
# 29. Identify unique source IPs.
# 30. Identify the most frequent IP.
# 31. Filter high-severity events.
# 32. Create a report dictionary.
# 33. Save a JSON report.
# 34. Save a text report.
# 35. Use pathlib for file paths.
# 36. Use UTF-8 encoding.
# 37. Use context managers.
# 38. Handle missing files.
# 39. Handle an empty event list.
# 40. Preserve original records.
# 41. Use explicit module imports.
# 42. Avoid wildcard imports.
# 43. Use a main guard.
# 44. Keep validation functions
#     inside validators.py.
# 45. Keep analysis functions
#     inside analyzers.py.
# 46. Keep reporting functions
#     inside reports.py.
# 47. Avoid circular imports.
# 48. Document module responsibilities.
# 49. Explain how modular design
#     supports code maintenance.
# 50. Explain how the application
#     could support SOC investigations.
#
# Write the program independently.
