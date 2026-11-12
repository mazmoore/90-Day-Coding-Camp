
# ==========================================
# DAY 11 - STRINGS AND TEXT PROCESSING
# Topic: Working with Text in Python
# ==========================================

# LESSON NOTES
#
# A string is a sequence of characters.
#
# Strings are used to store text such as:
#
# Names
# Usernames
# Messages
# Filenames
# Log entries
# IP addresses
#
# Strings can be created using single
# quotes or double quotes.
#
# Python uses zero-based indexing.
#
# This means the first character
# of a string has an index of 0.
#
# Strings are immutable.
#
# This means individual characters
# cannot be changed directly after
# a string has been created.


# EXAMPLE 1: Creating Strings

first_name = "Alex"
last_name = 'Morgan'

print(first_name)
print(last_name)


# EXAMPLE 2: String Data Types

language = "Python"

print("Value:", language)
print("Data type:", type(language))


# EXAMPLE 3: String Concatenation
#
# Concatenation combines strings
# using the + operator.

first_name = "Alex"
last_name = "Morgan"

full_name = first_name + " " + last_name

print("Full name:", full_name)


# EXAMPLE 4: String Repetition
#
# The * operator repeats strings.

message = "Python! "

print(message * 3)


# EXAMPLE 5: String Length
#
# len() returns the number
# of characters in a string.
#
# Spaces and punctuation count
# as characters.

message = "Hello Python"

print("Length:", len(message))


# EXAMPLE 6: String Indexing
#
# Python starts counting at index 0.
#
# P = 0
# y = 1
# t = 2
# h = 3
# o = 4
# n = 5

word = "Python"

print("First character:", word[0])
print("Second character:", word[1])
print("Third character:", word[2])


# EXAMPLE 7: Negative Indexing
#
# Negative indexes count backward
# from the end of the string.
#
# -1 refers to the last character.

word = "Cybersecurity"

print("Last character:", word[-1])
print("Second-to-last:", word[-2])


# EXAMPLE 8: String Slicing
#
# Slicing extracts a portion
# of a string.
#
# Syntax:
#
# string[start:stop]
#
# The stop index is not included.

word = "Cybersecurity"

print("First five:", word[0:5])
print("Next portion:", word[5:9])


# EXAMPLE 9: Slicing from the Beginning
#
# Leaving out the start index
# begins at index 0.

word = "Programming"

print(word[:7])


# EXAMPLE 10: Slicing to the End
#
# Leaving out the stop index
# continues to the end.

word = "Programming"

print(word[7:])


# EXAMPLE 11: Slicing with a Step
#
# Syntax:
#
# string[start:stop:step]
#
# The step controls how many
# positions are skipped.

word = "ABCDEFGHIJ"

print(word[::2])


# EXAMPLE 12: Reversing a String
#
# A step of -1 processes
# the string backward.

word = "Python"

reversed_word = word[::-1]

print("Reversed:", reversed_word)


# EXAMPLE 13: Checking String Membership
#
# The in operator checks whether
# text appears inside a string.

message = "Welcome to cybersecurity"

print("cybersecurity" in message)
print("Python" in message)


# EXAMPLE 14: Using not in

filename = "report.pdf"

if ".exe" not in filename:
    print("The text .exe was not found.")
else:
    print("The text .exe was found.")


# EXAMPLE 15: Comparing Strings
#
# String comparisons are case-sensitive.

username = "Admin"

print(username == "Admin")
print(username == "admin")


# EXAMPLE 16: String Formatting with f-Strings
#
# An f-string allows variables
# and expressions to appear
# inside a formatted string.

name = "Alex"
age = 23

print(f"My name is {name} and I am {age} years old.")


# EXAMPLE 17: Formatting Numbers

price = 75.5
quantity = 3

total = price * quantity

print(f"Total: ${total:.2f}")


# EXAMPLE 18: Escape Characters
#
# Escape characters control
# how text is displayed.
#
# \n creates a new line.
# \t creates a tab.
# \" displays a double quote.
# \\ displays a backslash.

print("Line 1\nLine 2")
print("Name:\tAlex")
print("She said, \"Hello!\"")
print("Folder: C:\\Users\\Student")


# EXAMPLE 19: Multiline Strings
#
# Triple quotes allow text
# to span multiple lines.

message = """Welcome to my coding camp.
I am learning Python.
My goal is cybersecurity."""

print(message)


# EXAMPLE 20: Strings Are Immutable
#
# You cannot directly replace
# a character using an index.
#
# The following would cause an error:
#
# word = "Python"
# word[0] = "J"
#
# Instead, create a new string.

word = "Python"

new_word = "J" + word[1:]

print("Original:", word)
print("New:", new_word)


# EXAMPLE 21: Iterating Through a String

word = "Security"

for character in word:
    print("Character:", character)


# EXAMPLE 22: Counting Characters

username = "cyberstudent"

character_count = 0

for character in username:
    character_count += 1

print("Character count:", character_count)


# EXAMPLE 23: Username Length Check
#
# This example checks only length.
# Real username validation may require
# additional rules.

username = "cyberstudent"

if len(username) >= 8:
    print("Username meets length requirement.")
else:
    print("Username is too short.")


# EXAMPLE 24: Processing a Log Entry
#
# A log entry contains text describing
# an event recorded by a system.

log_entry = "LOGIN FAILED - user=admin"

if "FAILED" in log_entry:
    print("Failed login event detected.")
else:
    print("No failed login text detected.")


# EXAMPLE 25: Extracting a Filename Extension
#
# rfind() returns the last position
# of the specified text.
#
# It returns -1 if the text is absent.

filename = "security_report.txt"

dot_position = filename.rfind(".")

extension = filename[dot_position:]

print("File extension:", extension)


# EXAMPLE 26: Basic Email Text Check
#
# This checks whether an @ symbol
# appears in the string.
#
# It does not fully validate
# an email address.

email = "student@example.com"

if "@" in email:
    print("Email contains @.")
else:
    print("Email does not contain @.")


# EXAMPLE 27: Extracting Text from an IP Address
#
# An IPv4 address is commonly written
# using four decimal components.
#
# This example demonstrates slicing.
# It does not validate the address.

ip_address = "192.168.1.10"

print("First three characters:", ip_address[:3])
print("Last two characters:", ip_address[-2:])


# EXAMPLE 28: Using Strings in Functions

def display_welcome(name):
    print(f"Welcome, {name}!")


display_welcome("Alex")


# EXAMPLE 29: Returning a Formatted String

def create_profile(name, major):
    return f"Student: {name} | Major: {major}"


profile = create_profile("Alex", "Cyber Defense")

print(profile)


# EXAMPLE 30: String Input

username = input("Enter your username: ")

print(f"Welcome, {username}!")
print("Username length:", len(username))


# WHAT I LEARNED
#
# 1. Strings store sequences of characters.
# 2. Strings can use single or double quotes.
# 3. Indexing starts at zero.
# 4. Negative indexing counts backward.
# 5. Slicing extracts portions of strings.
# 6. Step values control slicing intervals.
# 7. Strings can be reversed using [::-1].
# 8. in checks whether text is present.
# 9. Strings are case-sensitive.
# 10. f-strings format text with variables.
# 11. Escape characters control formatting.
# 12. Triple quotes support multiline text.
# 13. Strings are immutable.
# 14. Loops can process characters.
# 15. Text processing supports log analysis.
