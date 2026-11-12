
# ==========================================
# DAY 27 - PRACTICE EXERCISES
# Topic: Reading Files
# ==========================================

# INSTRUCTIONS:
#
# Complete each exercise using Python.
#
# Practice:
#
# open()
# read()
# readline()
# readlines()
# with
# File iteration
# String processing
# pathlib
# File positions
# UTF-8
# Exception handling
# Configuration parsing
# Security log analysis
#
# Leave solutions blank until review.
#
# You may create temporary sample
# files when completing exercises.
#
# Do not use real customer information
# or sensitive security logs.


# EXERCISE 1: Open a File
#
# Create a sample text file.
#
# Open it in read mode
# using open().
#
# Read and display its contents.


# EXERCISE 2: Read Entire File
#
# Create a text file containing
# three sentences.
#
# Read the entire file
# using read().


# EXERCISE 3: Read One Line
#
# Create a file containing
# multiple lines.
#
# Read only the first line
# using readline().


# EXERCISE 4: Read Two Lines
#
# Create a file containing
# at least four lines.
#
# Use readline() twice.
#
# Display both lines.


# EXERCISE 5: readlines()
#
# Read a text file
# using readlines().
#
# Store the result in a list.
#
# Display the list.


# EXERCISE 6: Loop Through a File
#
# Create a file containing
# five flower names.
#
# Print each line
# using a for loop.


# EXERCISE 7: Partial File Reading
#
# Create a text file.
#
# Read only the first
# 10 characters.


# EXERCISE 8: Multiple Reads
#
# Open a file.
#
# Read the first five characters.
#
# Read the next five characters.
#
# Display both portions.


# EXERCISE 9: Automatic File Closing
#
# Open a file using with.
#
# Read its contents.
#
# After the with block,
# check whether the file is closed.


# EXERCISE 10: Empty File
#
# Create an empty text file.
#
# Read its contents.
#
# Explain the returned value.


# EXERCISE 11: Remove Newlines
#
# Read a file containing
# several lines.
#
# Use strip() to remove
# surrounding whitespace.


# EXERCISE 12: Preserve Other Whitespace
#
# Read lines from a file.
#
# Remove only newline characters
# using rstrip("\r\n").
#
# Preserve leading spaces.


# EXERCISE 13: Count File Lines
#
# Create a text file.
#
# Count the total number
# of lines in the file.


# EXERCISE 14: Count Nonempty Lines
#
# Create a file containing
# text and blank lines.
#
# Count only nonempty lines.


# EXERCISE 15: Search for Text
#
# Create a file containing
# several flower products.
#
# Search for the word "Tulip".
#
# Return whether it was found.


# EXERCISE 16: Case-Insensitive Search
#
# Create a text file containing
# flower names in mixed case.
#
# Search for "rose"
# without case sensitivity.


# EXERCISE 17: Split File Contents
#
# Read a sentence from a file.
#
# Split the sentence into words.
#
# Display the resulting list.


# EXERCISE 18: Count Words
#
# Read a text file.
#
# Count the total number
# of whitespace-separated words.


# EXERCISE 19: Longest Line
#
# Create a file containing
# lines of different lengths.
#
# Find and display
# the longest line.


# EXERCISE 20: Number File Lines
#
# Read a text file.
#
# Use enumerate() to display
# line numbers starting at 1.


# EXERCISE 21: File Position
#
# Open a file.
#
# Use tell() to display
# the initial file position.


# EXERCISE 22: Position After Reading
#
# Read five characters.
#
# Use tell() to display
# the current file position.


# EXERCISE 23: Reset File Position
#
# Read part of a file.
#
# Use seek(0).
#
# Read the same portion again.


# EXERCISE 24: Read File Twice
#
# Read an entire text file.
#
# Reset the position to zero.
#
# Read the file again.
#
# Compare both results.


# EXERCISE 25: Binary Reading
#
# Open a sample file using "rb".
#
# Read the first 12 bytes.
#
# Display the bytes object.


# EXERCISE 26: pathlib Path
#
# Import Path from pathlib.
#
# Create a Path object.
#
# Display the filename.


# EXERCISE 27: File Existence
#
# Create a sample file.
#
# Use is_file() to confirm
# that it exists as a regular file.


# EXERCISE 28: Missing Path
#
# Create a Path object
# for a nonexistent file.
#
# Use exists().
#
# Display the result.


# EXERCISE 29: File Extension
#
# Create a Path object
# representing a .log file.
#
# Display its suffix.


# EXERCISE 30: File Stem
#
# Create a Path object.
#
# Display the filename
# without its extension.


# EXERCISE 31: Parent Directory
#
# Create a nested file path.
#
# Display the parent directory.


# EXERCISE 32: UTF-8 Reading
#
# Create a text file containing
# accented characters or emojis.
#
# Read the file using UTF-8.


# EXERCISE 33: Missing File Error
#
# Attempt to read
# a nonexistent file.
#
# Catch FileNotFoundError.
#
# Display a useful message.


# EXERCISE 34: Safe Reading Function
#
# Create a function that accepts
# a file path.
#
# Return file contents when valid.
#
# Return None for missing files
# or permission errors.


# EXERCISE 35: Limited Reading
#
# Create a text file.
#
# Read only the first
# 20 characters.
#
# Explain why limited reading
# can be useful for large files.


# EXERCISE 36: Skip Configuration Comments
#
# Create a configuration file.
#
# Include comments beginning with #.
#
# Read only nonempty,
# noncomment lines.


# EXERCISE 37: Parse Configuration
#
# Create a file containing:
#
# application=monitor
# environment=lab
# logging=enabled
#
# Parse the file into a dictionary.


# EXERCISE 38: Read Configuration Setting
#
# Using the parsed configuration,
# retrieve the environment setting.
#
# Provide a default value
# when the key is missing.


# EXERCISE 39: Read JSON File
#
# Create a JSON file containing
# a list of synthetic events.
#
# Read it using json.load().
#
# Display the resulting objects.


# EXERCISE 40: Invalid JSON
#
# Create malformed JSON text.
#
# Attempt to parse it.
#
# Catch json.JSONDecodeError.


# EXERCISE 41: Read Security Log
#
# Create a synthetic security log.
#
# Include at least five records.
#
# Read and display the log.


# EXERCISE 42: Count Security Records
#
# Read a synthetic security log.
#
# Count all nonempty lines.


# EXERCISE 43: Find Failed Logins
#
# Create a log containing:
#
# LOGIN_SUCCESS
# LOGIN_FAILED
# PORT_SCAN
#
# Extract only failed login lines.


# EXERCISE 44: Count Failed Logins
#
# Read a synthetic log.
#
# Count records representing
# failed login attempts.


# EXERCISE 45: Split Log Fields
#
# Use a log format containing:
#
# Date
# Source IP
# Event type
# Severity
#
# Separate fields using "|".


# EXERCISE 46: Parse Log Records
#
# Create a function that accepts
# one log line.
#
# Check that four fields exist.
#
# Return a dictionary
# or None when malformed.


# EXERCISE 47: Malformed Log Lines
#
# Create a log containing
# valid and malformed lines.
#
# Separate valid records.
#
# Record invalid line numbers.


# EXERCISE 48: Count Event Types
#
# Read a synthetic log.
#
# Count events by type.
#
# Store counts in a dictionary.


# EXERCISE 49: Unique Source IPs
#
# Read a synthetic security log.
#
# Extract source IP addresses.
#
# Store unique addresses in a set.
#
# Display the sorted results.


# EXERCISE 50: Independent Challenge
#
# Build a complete security
# log reading and reporting system.
#
# Requirements:
#
# 1. Create a synthetic log file.
# 2. Include at least 20 records.
# 3. Use documentation IP ranges.
# 4. Include timestamps.
# 5. Include source IP addresses.
# 6. Include event types.
# 7. Include severity levels.
# 8. Include valid records.
# 9. Include malformed records.
# 10. Use pathlib for file paths.
# 11. Open files using with.
# 12. Specify UTF-8 encoding.
# 13. Read records line by line.
# 14. Track line numbers.
# 15. Ignore empty lines.
# 16. Split delimited fields.
# 17. Validate field counts.
# 18. Validate event types.
# 19. Validate severity values.
# 20. Validate IP addresses.
# 21. Validate timestamp formats.
# 22. Handle missing files.
# 23. Handle permission errors.
# 24. Separate valid records.
# 25. Separate invalid records.
# 26. Count total lines.
# 27. Count valid records.
# 28. Count invalid records.
# 29. Count failed login events.
# 30. Count port scan events.
# 31. Count events by severity.
# 32. Identify unique source IPs.
# 33. Identify the most frequent IP.
# 34. Return a structured report.
# 35. Display a formatted report.
# 36. Handle an empty log file.
# 37. Avoid loading large files
#     entirely into memory.
# 38. Keep all data synthetic.
# 39. Do not execute file contents.
# 40. Document parsing decisions.
# 41. Explain how this could support
#     cybersecurity investigations.
#
# Write the program independently.
