
# ==========================================
# DAY 29 - PRACTICE EXERCISES
# Topic: CSV Files
# ==========================================

# INSTRUCTIONS:
#
# Complete each exercise using Python.
#
# Practice:
#
# csv.reader()
# csv.writer()
# csv.DictReader()
# csv.DictWriter()
# writerow()
# writerows()
# writeheader()
# CSV validation
# CSV filtering
# CSV sorting
# CSV exporting
# Error handling
# Business data analysis
# Security event analysis
#
# Leave solutions blank
# until reviewing the lesson.
#
# Use synthetic data only.


# EXERCISE 1: Read a CSV File
#
# Create a sample CSV file.
#
# Read the file using csv.reader().
#
# Display every row.


# EXERCISE 2: Read CSV Headers
#
# Create a CSV file with headers.
#
# Use next() to retrieve
# the header row.


# EXERCISE 3: First Data Row
#
# Create a CSV file containing
# at least five records.
#
# Skip the header.
#
# Read the first data row.


# EXERCISE 4: CSV Rows as List
#
# Read a CSV file.
#
# Convert all rows into a list.
#
# Display the resulting list.


# EXERCISE 5: Count CSV Records
#
# Read a CSV file.
#
# Count data rows
# without counting the header.


# EXERCISE 6: Access Columns
#
# Create a CSV file containing:
#
# Product
# Quantity
# Price
#
# Display each field separately.


# EXERCISE 7: CSV Data Types
#
# Read a quantity from a CSV file.
#
# Display its Python data type.
#
# Explain why conversion is needed.


# EXERCISE 8: Convert Quantity
#
# Read a quantity string.
#
# Convert it to an integer.
#
# Display the result.


# EXERCISE 9: Convert Price
#
# Read a price string.
#
# Convert it using Decimal.
#
# Display the result.


# EXERCISE 10: Calculate Row Total
#
# Read a quantity and price.
#
# Convert both values.
#
# Calculate the subtotal.


# EXERCISE 11: DictReader
#
# Create a CSV file.
#
# Read its rows using
# csv.DictReader().
#
# Display each dictionary.


# EXERCISE 12: Named Fields
#
# Read a CSV file
# using DictReader.
#
# Access a field by its name.


# EXERCISE 13: Dictionary List
#
# Read all CSV records
# into a list of dictionaries.
#
# Display the list.


# EXERCISE 14: Filter Prices
#
# Create a flower inventory CSV.
#
# Find products priced
# at $90 or higher.


# EXERCISE 15: Total Quantity
#
# Read an inventory CSV.
#
# Calculate the sum
# of all quantities.


# EXERCISE 16: Inventory Value
#
# Read an inventory CSV.
#
# Multiply quantity by price.
#
# Calculate total inventory value.


# EXERCISE 17: Highest Price
#
# Read a product CSV.
#
# Identify the product
# with the highest price.


# EXERCISE 18: Sort Products
#
# Read a product CSV.
#
# Sort products alphabetically.
#
# Display the sorted results.


# EXERCISE 19: Search Product
#
# Read a product CSV.
#
# Search for "bouquet"
# without case sensitivity.


# EXERCISE 20: Extract Column
#
# Read a CSV file.
#
# Extract all product names
# into a separate list.


# EXERCISE 21: Create CSV File
#
# Create a CSV file.
#
# Write a header row
# using csv.writer().


# EXERCISE 22: Write One Row
#
# Create a CSV file.
#
# Write a header.
#
# Write one data row.


# EXERCISE 23: Write Multiple Rows
#
# Create a list of records.
#
# Save them using writerows().


# EXERCISE 24: DictWriter
#
# Create a CSV file
# using csv.DictWriter().
#
# Write headers and one record.


# EXERCISE 25: Write Dictionaries
#
# Create a list of dictionaries.
#
# Save all records
# using DictWriter.writerows().


# EXERCISE 26: Append CSV Record
#
# Create an existing CSV file.
#
# Append a new data row.
#
# Preserve existing records.


# EXERCISE 27: Custom Delimiter
#
# Create a CSV file
# using semicolons
# instead of commas.


# EXERCISE 28: Read Custom Delimiter
#
# Read a semicolon-delimited file.
#
# Specify delimiter=";".
#
# Display parsed rows.


# EXERCISE 29: Quoted Fields
#
# Write a CSV field containing
# commas inside the text.
#
# Verify the field
# is read correctly.


# EXERCISE 30: Quote All Fields
#
# Create a CSV writer
# using csv.QUOTE_ALL.
#
# Save multiple rows.
#
# Inspect the output.


# EXERCISE 31: Validate Headers
#
# Define required CSV headers.
#
# Read a file.
#
# Verify all required headers exist.


# EXERCISE 32: Missing Values
#
# Create a CSV file containing
# blank field values.
#
# Identify incomplete records.


# EXERCISE 33: Invalid Integer
#
# Create a CSV row containing
# an invalid quantity.
#
# Attempt integer conversion.
#
# Catch ValueError.


# EXERCISE 34: Invalid Price
#
# Create a CSV row containing
# an invalid price.
#
# Catch InvalidOperation
# during Decimal conversion.


# EXERCISE 35: Quantity Validation
#
# Create a function that
# validates inventory quantities.
#
# Reject negative values
# and invalid integers.


# EXERCISE 36: Price Validation
#
# Create a function that
# validates product prices.
#
# Reject negative values,
# invalid text, and nonfinite values.


# EXERCISE 37: Empty CSV
#
# Create an empty CSV file.
#
# Read the file.
#
# Handle the empty result.


# EXERCISE 38: Missing CSV File
#
# Attempt to read
# a nonexistent CSV file.
#
# Catch FileNotFoundError.


# EXERCISE 39: Extra Columns
#
# Create a CSV row containing
# more columns than the header.
#
# Detect the extra values.


# EXERCISE 40: Missing Columns
#
# Create a CSV row containing
# fewer columns than the header.
#
# Identify the missing values.


# EXERCISE 41: CSV Sniffer
#
# Create a sample CSV string
# using semicolons.
#
# Use csv.Sniffer()
# to guess the delimiter.


# EXERCISE 42: StringIO Reading
#
# Create CSV text in memory.
#
# Use io.StringIO()
# with csv.DictReader().
#
# Display the parsed records.


# EXERCISE 43: StringIO Writing
#
# Create an in-memory text buffer.
#
# Use csv.writer().
#
# Retrieve the CSV string
# using getvalue().


# EXERCISE 44: Unicode CSV
#
# Create a CSV file containing
# accented text or emojis.
#
# Save and read it using UTF-8.


# EXERCISE 45: Sort CSV by Price
#
# Read a product CSV.
#
# Convert prices to Decimal.
#
# Sort highest to lowest.


# EXERCISE 46: Security CSV Reading
#
# Create a synthetic security CSV.
#
# Include:
#
# Timestamp
# Source IP
# Event type
# Severity
#
# Read records using DictReader.


# EXERCISE 47: Event Counts
#
# Read synthetic security events.
#
# Count events by type.
#
# Store counts in a dictionary.


# EXERCISE 48: High-Severity Events
#
# Read synthetic security events.
#
# Filter records where
# severity is HIGH.


# EXERCISE 49: Export Filtered Events
#
# Filter synthetic security events.
#
# Save matching records
# to a new CSV file.
#
# Include headers.


# EXERCISE 50: Independent Challenge
#
# Build a complete CSV-based
# security event analysis system.
#
# Requirements:
#
# 1. Create at least 25 synthetic events.
# 2. Save events to a CSV file.
# 3. Use documentation IP ranges.
# 4. Include timestamps.
# 5. Include source IP addresses.
# 6. Include event types.
# 7. Include severity levels.
# 8. Include valid records.
# 9. Include malformed records.
# 10. Use at least six functions.
# 11. Use csv.DictReader().
# 12. Use csv.DictWriter().
# 13. Validate CSV headers.
# 14. Detect missing fields.
# 15. Detect extra columns.
# 16. Validate timestamp formats.
# 17. Validate IP addresses.
# 18. Validate event types.
# 19. Validate severity values.
# 20. Separate valid records.
# 21. Separate invalid records.
# 22. Count total records.
# 23. Count valid records.
# 24. Count invalid records.
# 25. Count failed logins.
# 26. Count port scans.
# 27. Count events by severity.
# 28. Identify unique source IPs.
# 29. Identify the most frequent IP.
# 30. Sort events by timestamp.
# 31. Filter high-severity events.
# 32. Export valid records to CSV.
# 33. Export rejected-record details.
# 34. Export high-severity records.
# 35. Generate a CSV summary report.
# 36. Use pathlib for file paths.
# 37. Use UTF-8 encoding.
# 38. Use newline="".
# 39. Handle missing files.
# 40. Handle malformed CSV data.
# 41. Handle an empty CSV file.
# 42. Avoid overwriting source data.
# 43. Preserve original records.
# 44. Do not store sensitive secrets.
# 45. Explain CSV formula injection risks.
# 46. Explain how the system could
#     support SOC investigations.
#
# Write the program independently.
