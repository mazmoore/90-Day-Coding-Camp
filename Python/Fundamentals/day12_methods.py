
# ==========================================
# DAY 12 - STRING METHODS
# Topic: String Methods and Text Manipulation
# ==========================================

# LESSON NOTES
#
# A string method is a built-in operation
# that performs a task on string data.
#
# String methods can:
#
# - Change letter capitalization
# - Remove unwanted whitespace
# - Search for text
# - Replace text
# - Split strings into smaller pieces
# - Combine text
# - Check string contents
#
# Most string methods use dot notation.
#
# Example:
#
# message.upper()
#
# Strings are immutable in Python.
#
# String methods do not change the
# original string directly.
#
# Instead, methods that transform text
# return a new string.
#
# The result can be stored in a variable.


# EXAMPLE 1: Converting Text to Uppercase
#
# upper() converts letters to uppercase.

message = "welcome to python"

result = message.upper()

print("Original:", message)
print("Uppercase:", result)


# EXAMPLE 2: Converting Text to Lowercase
#
# lower() converts letters to lowercase.

message = "CYBERSECURITY ANALYST"

result = message.lower()

print("Lowercase:", result)


# EXAMPLE 3: Capitalizing the First Character
#
# capitalize() capitalizes the first
# character and lowercases the rest.

message = "welcome TO PYTHON"

result = message.capitalize()

print("Capitalized:", result)


# EXAMPLE 4: Title Case
#
# title() capitalizes words according
# to Python's title-casing rules.

business = "golden aura florals"

print("Business:", business.title())


# EXAMPLE 5: Swapping Letter Case
#
# swapcase() reverses uppercase
# and lowercase letters.

message = "Python Programming"

print("Swapped:", message.swapcase())


# EXAMPLE 6: Removing Whitespace
#
# strip() removes whitespace from
# both ends of a string.
#
# It does not remove spaces
# from the middle.

username = "   cyberstudent   "

clean_username = username.strip()

print("Original:", repr(username))
print("Cleaned:", repr(clean_username))


# EXAMPLE 7: Removing Leading Whitespace
#
# lstrip() removes whitespace
# from the beginning.

message = "     Welcome!"

print("Cleaned:", repr(message.lstrip()))


# EXAMPLE 8: Removing Trailing Whitespace
#
# rstrip() removes whitespace
# from the end.

message = "Welcome!     "

print("Cleaned:", repr(message.rstrip()))


# EXAMPLE 9: Replacing Text
#
# replace(old, new) replaces matching
# text with another value.

message = "I am learning Java"

updated_message = message.replace(
    "Java", "Python"
)

print("Updated:", updated_message)


# EXAMPLE 10: Counting Occurrences
#
# count() counts non-overlapping
# occurrences of a substring.

message = "failed success failed failed"

failed_count = message.count("failed")

print("Failed occurrences:", failed_count)


# EXAMPLE 11: Finding Text
#
# find() returns the first index
# where a substring is found.
#
# If it is absent, find() returns -1.

message = "Welcome to cybersecurity"

position = message.find("cybersecurity")

print("Position:", position)


# EXAMPLE 12: Finding the Last Occurrence
#
# rfind() searches for the last
# occurrence of a substring.

filename = "backup.archive.tar.gz"

position = filename.rfind(".")

print("Last dot position:", position)


# EXAMPLE 13: Using index()
#
# index() finds a substring position.
#
# Unlike find(), it raises ValueError
# when the substring is absent.

message = "Python programming"

position = message.index("programming")

print("Index:", position)


# EXAMPLE 14: Checking String Beginnings
#
# startswith() returns True if a string
# begins with the specified text.

filename = "security_report.txt"

print(filename.startswith("security"))


# EXAMPLE 15: Checking String Endings
#
# endswith() returns True if a string
# ends with the specified text.

filename = "security_report.txt"

print(filename.endswith(".txt"))


# EXAMPLE 16: Splitting Strings
#
# split() divides a string into
# a list of smaller strings.
#
# Lists will be covered in detail
# on Day 13.

message = "Python C C++"

languages = message.split()

print("Languages:", languages)


# EXAMPLE 17: Splitting with a Delimiter
#
# A delimiter separates values.

record = "Alex,Cyber Defense,NMSU"

fields = record.split(",")

print("Name:", fields[0])
print("Major:", fields[1])
print("University:", fields[2])


# EXAMPLE 18: Joining Strings
#
# join() combines strings from
# an iterable using a separator.

words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print("Sentence:", sentence)


# EXAMPLE 19: Checking Alphabetic Characters
#
# isalpha() returns True when the
# string is nonempty and all
# characters are alphabetic.

name = "Alex"

print("Alphabetic:", name.isalpha())


# EXAMPLE 20: Checking Numeric Characters
#
# isdigit() checks whether a nonempty
# string contains only digit characters.

number = "12345"

print("Digits only:", number.isdigit())


# EXAMPLE 21: Checking Alphanumeric Text
#
# isalnum() checks whether a nonempty
# string contains only letters or numbers.

username = "CyberStudent123"

print("Alphanumeric:", username.isalnum())


# EXAMPLE 22: Checking Whitespace
#
# isspace() returns True when a string
# contains only whitespace and is nonempty.

message = "   "

print("Whitespace only:", message.isspace())


# EXAMPLE 23: Checking Uppercase and Lowercase

message1 = "PYTHON"
message2 = "python"

print(message1.isupper())
print(message2.islower())


# EXAMPLE 24: Centering Text
#
# center() places text within
# a specified width.

title = "SECURITY REPORT"

print(title.center(40, "-"))


# EXAMPLE 25: Aligning Text
#
# ljust() aligns text to the left.
# rjust() aligns text to the right.

label = "Status"

print(label.ljust(20, "."))
print(label.rjust(20, "."))


# EXAMPLE 26: Padding Numbers
#
# zfill() adds leading zeros
# to reach a specified width.

order_number = "25"

formatted_number = order_number.zfill(5)

print("Order number:", formatted_number)


# EXAMPLE 27: Cleaning User Input
#
# strip() removes surrounding whitespace.
# lower() normalizes letter case.

response = input("Type YES or NO: ")

clean_response = response.strip().lower()

if clean_response == "yes":
    print("You selected yes.")
elif clean_response == "no":
    print("You selected no.")
else:
    print("Invalid response.")


# EXAMPLE 28: Normalizing Usernames

username = "  CyberStudent  "

normalized_username = username.strip().lower()

print("Normalized username:", normalized_username)


# EXAMPLE 29: Searching Security Logs
#
# This example searches predefined
# log text without reading a real file.

log_entry = "LOGIN FAILED - USER=ADMIN"

normalized_log = log_entry.lower()

if "failed" in normalized_log:
    print("Failed login event detected.")
else:
    print("No failed login text detected.")


# EXAMPLE 30: Counting Failed Login Events

log_entries = [
    "LOGIN SUCCESS",
    "LOGIN FAILED",
    "LOGIN FAILED",
    "LOGIN SUCCESS",
    "LOGIN FAILED"
]

failed_count = 0

for entry in log_entries:
    if "failed" in entry.lower():
        failed_count += 1

print("Failed login events:", failed_count)


# EXAMPLE 31: Processing Structured Log Text
#
# split() can separate simple
# key-value information.

log_entry = "user=admin,status=failed,port=22"

fields = log_entry.split(",")

for field in fields:
    print("Field:", field)


# EXAMPLE 32: Extracting Key-Value Pairs

log_entry = "user=admin,status=failed"

fields = log_entry.split(",")

for field in fields:
    key, value = field.split("=", 1)

    print("Key:", key)
    print("Value:", value)


# EXAMPLE 33: Filename Extension Check
#
# This is a text-based extension check.
#
# File extensions alone cannot prove
# that a file is safe or identify
# its actual content.

filename = "security_report.txt"

if filename.lower().endswith(".txt"):
    print("Filename ends with .txt")
else:
    print("Different filename extension.")


# EXAMPLE 34: Cleaning Business Data

customer_name = "   alex morgan   "

clean_name = customer_name.strip().title()

print("Customer:", clean_name)


# EXAMPLE 35: Formatting Flower Orders

flower_type = "roses"
quantity = 50
customer = "alex"

print("===== FLOWER ORDER =====")
print("Customer:", customer.title())
print("Flower:", flower_type.title())
print("Quantity:", quantity)


# EXAMPLE 36: Using String Methods in Functions

def normalize_username(username):
    return username.strip().lower()


result = normalize_username("  AdminUser  ")

print("Normalized:", result)


# EXAMPLE 37: Basic Input Validation
#
# This example accepts only
# ASCII letters and digits.
#
# It is a simplified format check,
# not a complete security policy.

def valid_username(username):
    username = username.strip()

    if len(username) < 5:
        return False

    return username.isascii() and username.isalnum()


print(valid_username("Alex123"))
print(valid_username("Alex!"))


# EXAMPLE 38: String Method Chaining
#
# Multiple methods can be used
# in a single expression.

message = "   WELCOME TO PYTHON   "

clean_message = message.strip().lower().title()

print("Cleaned message:", clean_message)


# EXAMPLE 39: Understanding Immutability
#
# Methods do not change the original
# string unless their returned value
# is assigned to a variable.

message = "hello"

message.upper()

print("Original remains:", message)

message = message.upper()

print("Updated variable:", message)


# EXAMPLE 40: Basic Security Log Summary

logs = [
    "LOGIN SUCCESS - user=alex",
    "LOGIN FAILED - user=admin",
    "LOGIN FAILED - user=guest",
    "LOGIN SUCCESS - user=student",
    "LOGIN FAILED - user=admin"
]

successful_logins = 0
failed_logins = 0

for log in logs:
    normalized_log = log.strip().lower()

    if normalized_log.startswith("login success"):
        successful_logins += 1
    elif normalized_log.startswith("login failed"):
        failed_logins += 1

print("===== SECURITY LOG SUMMARY =====")
print("Successful logins:", successful_logins)
print("Failed logins:", failed_logins)
print("Total classified:", successful_logins + failed_logins)


# WHAT I LEARNED
#
# 1. String methods manipulate text.
# 2. upper() converts text to uppercase.
# 3. lower() converts text to lowercase.
# 4. capitalize() changes sentence casing.
# 5. title() applies title casing.
# 6. strip() removes surrounding whitespace.
# 7. replace() substitutes matching text.
# 8. count() counts substring occurrences.
# 9. find() searches for text positions.
# 10. startswith() checks prefixes.
# 11. endswith() checks suffixes.
# 12. split() separates text into a list.
# 13. join() combines strings.
# 14. isalpha() checks alphabetic content.
# 15. isdigit() checks digit characters.
# 16. isalnum() checks letters and digits.
# 17. Methods can be chained together.
# 18. Strings remain immutable.
# 19. Text normalization helps consistency.
# 20. String methods support log analysis.
