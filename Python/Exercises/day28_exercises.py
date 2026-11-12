
# ==========================================
# DAY 28 - PRACTICE EXERCISES
# Topic: Writing Files
# ==========================================

# INSTRUCTIONS:
#
# Complete each exercise using Python.
#
# Practice:
#
# File creation
# Write mode
# Append mode
# Exclusive creation
# write()
# writelines()
# Text formatting
# pathlib
# Directory creation
# File verification
# JSON output
# Error handling
# Business records
# Security event reports
#
# Leave all solutions blank
# until returning to the lessons.
#
# Use synthetic data only.
# Do not overwrite important files.


# EXERCISE 1: Create a Text File
#
# Create a new text file
# using write mode.
#
# Write "Hello, Python!".
#
# Read the file to verify it.


# EXERCISE 2: Multiple Lines
#
# Create a text file.
#
# Write at least three lines
# using separate write() calls.


# EXERCISE 3: Overwrite Contents
#
# Create a file with text.
#
# Open it again using "w".
#
# Replace the original contents.
#
# Explain what happened.


# EXERCISE 4: Append Text
#
# Create a text file.
#
# Add a second entry
# using append mode.
#
# Verify both entries remain.


# EXERCISE 5: Multiple Appends
#
# Create a file.
#
# Append three separate lines.
#
# Display the final contents.


# EXERCISE 6: Exclusive Creation
#
# Create a new file using "x".
#
# Write a short message.
#
# Confirm the file exists.


# EXERCISE 7: Existing File Error
#
# Attempt to create an existing
# file using "x".
#
# Catch FileExistsError.
#
# Display an explanation.


# EXERCISE 8: writelines()
#
# Create a list containing
# three flower products.
#
# Write the list using writelines().
#
# Include newline characters.


# EXERCISE 9: Newline Behavior
#
# Use writelines() without
# newline characters.
#
# Read the result.
#
# Explain the output.


# EXERCISE 10: Write a Variable
#
# Store a flower product
# name in a variable.
#
# Write the variable to a file.


# EXERCISE 11: Write an Integer
#
# Store an inventory quantity
# in an integer variable.
#
# Convert it to text.
#
# Save it to a file.


# EXERCISE 12: f-String Output
#
# Create a product name
# and price.
#
# Write a formatted line
# using an f-string.


# EXERCISE 13: Write List Items
#
# Create a list of flowers.
#
# Write each item
# on a separate line.


# EXERCISE 14: Write Dictionary
#
# Create a product dictionary.
#
# Write each key-value pair
# to a text file.


# EXERCISE 15: Numbered Lines
#
# Create a list of products.
#
# Use enumerate() to write
# numbered lines.


# EXERCISE 16: Report Header
#
# Create a text report.
#
# Include:
#
# Report title
# Subtitle
# Divider line


# EXERCISE 17: Timestamp
#
# Import datetime.
#
# Create a timestamp.
#
# Write it to a file
# using ISO formatting.


# EXERCISE 18: Unicode Writing
#
# Create a text file.
#
# Write accented characters
# and an emoji.
#
# Use UTF-8 encoding.


# EXERCISE 19: Empty File
#
# Create an empty file.
#
# Check its size.
#
# Explain the result.


# EXERCISE 20: Join Strings
#
# Create a list of names.
#
# Use join() to combine them
# with newline separators.
#
# Save the result.


# EXERCISE 21: Path.write_text()
#
# Import Path.
#
# Create a file using
# Path.write_text().
#
# Verify its contents.


# EXERCISE 22: Binary Writing
#
# Create a bytes object.
#
# Save it using
# Path.write_bytes().
#
# Read it back.


# EXERCISE 23: Create Directory
#
# Use pathlib to create
# a directory named reports.
#
# Use exist_ok=True.


# EXERCISE 24: Write in Subfolder
#
# Create a reports folder.
#
# Save a text report inside it.
#
# Confirm the file exists.


# EXERCISE 25: Check Before Writing
#
# Check whether a file exists.
#
# Write a new file if absent.
#
# Explain why an existence
# check alone does not guarantee
# safe exclusive creation.


# EXERCISE 26: w+ Mode
#
# Open a file using "w+".
#
# Write text.
#
# Reset the file position.
#
# Read the text back.


# EXERCISE 27: a+ Mode
#
# Create a file with text.
#
# Open it using "a+".
#
# Append another line.
#
# Reset the position.
#
# Read all contents.


# EXERCISE 28: flush()
#
# Open a file for writing.
#
# Write text.
#
# Call flush().
#
# Explain what flush() does
# and what it does not guarantee.


# EXERCISE 29: Verify Written Data
#
# Save a string to a file.
#
# Read the file back.
#
# Compare actual contents
# with expected contents.


# EXERCISE 30: Handle Write Errors
#
# Attempt to write into
# a nonexistent parent directory.
#
# Catch FileNotFoundError.
#
# Display a useful message.


# EXERCISE 31: Save JSON Dictionary
#
# Create a settings dictionary.
#
# Save it using json.dump().
#
# Use indentation.


# EXERCISE 32: Save JSON List
#
# Create a list containing
# synthetic event dictionaries.
#
# Save the list as JSON.


# EXERCISE 33: Unicode JSON
#
# Create a dictionary containing
# accented characters or emojis.
#
# Save it as JSON using
# ensure_ascii=False.


# EXERCISE 34: Key-Value Settings
#
# Create a configuration dictionary.
#
# Write settings using:
#
# key=value
#
# Place each setting
# on a separate line.


# EXERCISE 35: Summary Report
#
# Create a dictionary containing
# security event counts.
#
# Write a formatted
# summary report.


# EXERCISE 36: Flower Inventory
#
# Create a flower inventory.
#
# Include at least five products.
#
# Save each product
# and quantity to a file.


# EXERCISE 37: Inventory Activity
#
# Create an inventory activity log.
#
# Append an inventory update.
#
# Verify previous entries remain.


# EXERCISE 38: Order Summary
#
# Create a synthetic flower order.
#
# Include:
#
# Order ID
# Product
# Quantity
# Unit price
# Subtotal
#
# Save a formatted order summary.


# EXERCISE 39: Multiple Orders
#
# Create a list containing
# at least five synthetic orders.
#
# Save the list as JSON.


# EXERCISE 40: Sales Report
#
# Create a list of order totals.
#
# Calculate total sales.
#
# Write a formatted sales report.


# EXERCISE 41: Security Event Log
#
# Create a synthetic security event.
#
# Include:
#
# Timestamp
# Source IP
# Event type
# Severity
#
# Save the event to a log file.


# EXERCISE 42: Append Security Events
#
# Create multiple synthetic events.
#
# Append them to a log file.
#
# Verify all events were saved.


# EXERCISE 43: Suspicious Events
#
# Create a list of events.
#
# Filter failed login
# and port scan events.
#
# Save only matching records.


# EXERCISE 44: Event Counts
#
# Create synthetic events.
#
# Count events by type.
#
# Save counts to a text report.


# EXERCISE 45: Unique IP Addresses
#
# Create synthetic security records.
#
# Extract unique source IPs.
#
# Sort and save the addresses.


# EXERCISE 46: JSON Security Export
#
# Convert synthetic log records
# into dictionaries.
#
# Save the records as JSON.


# EXERCISE 47: Rejected Record Report
#
# Create a list of rejected records.
#
# Include line numbers
# and rejection reasons.
#
# Save a text report.


# EXERCISE 48: Security Alert File
#
# Create a failed login threshold.
#
# Compare the number of failures
# with the threshold.
#
# Save an alert message
# when the threshold is reached.


# EXERCISE 49: Atomic Replacement
#
# Create an existing report.
#
# Write a new report
# to a temporary file.
#
# Replace the original
# using os.replace().
#
# Explain limitations involving
# crashes and concurrent writers.


# EXERCISE 50: Independent Challenge
#
# Build a complete security event
# report generation system.
#
# Requirements:
#
# 1. Create at least 20 synthetic events.
# 2. Use documentation IP ranges.
# 3. Store events as dictionaries.
# 4. Include timestamps.
# 5. Include source IP addresses.
# 6. Include event types.
# 7. Include severity levels.
# 8. Include valid records.
# 9. Include invalid records.
# 10. Create at least six functions.
# 11. Validate required fields.
# 12. Validate event types.
# 13. Validate severity values.
# 14. Validate IP address syntax.
# 15. Separate accepted records.
# 16. Separate rejected records.
# 17. Count total events.
# 18. Count accepted events.
# 19. Count rejected events.
# 20. Count failed logins.
# 21. Count port scans.
# 22. Count events by severity.
# 23. Identify unique source IPs.
# 24. Identify the most frequent IP.
# 25. Generate a text report.
# 26. Generate a JSON report.
# 27. Create a reports directory.
# 28. Use pathlib for paths.
# 29. Use UTF-8 encoding.
# 30. Use context managers.
# 31. Handle expected file errors.
# 32. Avoid overwriting source logs.
# 33. Preserve original event records.
# 34. Include a report timestamp.
# 35. Save a rejected-record summary.
# 36. Verify generated files exist.
# 37. Read back at least one report.
# 38. Handle an empty event list.
# 39. Avoid storing sensitive secrets.
# 40. Document file writing decisions.
# 41. Explain the difference between
#     write and append modes.
# 42. Explain how generated reports
#     could support SOC investigations.
#
# Write the program independently.
