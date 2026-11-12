
# ==========================================
# DAY 13 - LISTS AND DATA COLLECTIONS
# Topic: Working with Lists in Python
# ==========================================

# LESSON NOTES
#
# A list is a data structure that stores
# multiple values in a single variable.
#
# Lists are created using square brackets [].
#
# Each value in a list is called an element.
#
# Lists are:
#
# 1. Ordered
# 2. Mutable
# 3. Able to contain duplicate values
# 4. Able to store different data types
#
# Ordered means elements have positions.
#
# Mutable means elements can be changed.
#
# Python lists use zero-based indexing.
#
# The first element has index 0.
#
# Lists are useful for:
#
# Student records
# Customer orders
# Inventory tracking
# Security events
# Network port collections
# Application data


# EXAMPLE 1: Creating a List

programming_languages = [
    "Python",
    "C",
    "C++"
]

print(programming_languages)


# EXAMPLE 2: Creating a List of Numbers

grades = [85, 92, 78, 95, 88]

print("Student grades:", grades)


# EXAMPLE 3: Creating an Empty List
#
# Empty lists can be populated later.

security_events = []

print("Security events:", security_events)


# EXAMPLE 4: Lists with Different Data Types
#
# Lists can contain strings, integers,
# floating-point numbers, and Booleans.

student_information = [
    "Alex",
    23,
    3.5,
    True
]

print("Student information:", student_information)


# EXAMPLE 5: Accessing List Elements
#
# List indexing begins at zero.

languages = ["Python", "C", "C++"]

print("First language:", languages[0])
print("Second language:", languages[1])
print("Third language:", languages[2])


# EXAMPLE 6: Negative Indexing
#
# Negative indexes count backward.
#
# -1 refers to the last element.

languages = ["Python", "C", "C++"]

print("Last language:", languages[-1])
print("Second-to-last:", languages[-2])


# EXAMPLE 7: List Length
#
# len() returns the number of elements.

tools = [
    "Wireshark",
    "Nmap",
    "Python",
    "Linux"
]

print("Number of tools:", len(tools))


# EXAMPLE 8: Modifying List Elements
#
# Lists are mutable.
#
# Existing elements can be replaced.

languages = ["Python", "Java", "C++"]

languages[1] = "C"

print("Updated languages:", languages)


# EXAMPLE 9: Lists Allow Duplicates

login_events = [
    "failed",
    "success",
    "failed",
    "failed"
]

print("Login events:", login_events)


# EXAMPLE 10: List Slicing
#
# Slicing extracts a portion of a list.
#
# Syntax:
#
# list[start:stop]
#
# The stop index is excluded.

numbers = [10, 20, 30, 40, 50]

print("First three:", numbers[0:3])
print("Middle values:", numbers[1:4])


# EXAMPLE 11: Slicing from the Beginning

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])


# EXAMPLE 12: Slicing to the End

numbers = [10, 20, 30, 40, 50]

print(numbers[2:])


# EXAMPLE 13: Slicing with a Step

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("Every second element:", numbers[::2])


# EXAMPLE 14: Reversing a List with Slicing

numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]

print("Original:", numbers)
print("Reversed:", reversed_numbers)


# EXAMPLE 15: Checking List Membership
#
# in checks whether a value
# exists inside a list.

tools = ["Wireshark", "Nmap", "Python"]

print("Python" in tools)
print("Java" in tools)


# EXAMPLE 16: Using not in

authorized_roles = [
    "admin",
    "analyst",
    "employee"
]

role = "guest"

if role not in authorized_roles:
    print("Role not in authorized list.")
else:
    print("Role is listed as authorized.")


# EXAMPLE 17: Iterating Through a List
#
# A for loop processes each element.

languages = ["Python", "C", "C++"]

for language in languages:
    print("Language:", language)


# EXAMPLE 18: Iterating with Indexes
#
# range(len()) generates valid indexes.

tools = ["Wireshark", "Nmap", "Python"]

for index in range(len(tools)):
    print(index, tools[index])


# EXAMPLE 19: Using enumerate()
#
# enumerate() provides an index
# and an element during iteration.

tools = ["Wireshark", "Nmap", "Python"]

for index, tool in enumerate(tools, start=1):
    print(index, tool)


# EXAMPLE 20: Adding List Elements
#
# append() adds one element
# to the end of a list.
#
# More list methods will be
# covered on Day 14.

languages = ["Python", "C"]

languages.append("C++")

print("Updated list:", languages)


# EXAMPLE 21: Removing List Elements
#
# remove() removes the first
# matching value from a list.
#
# It raises ValueError if the
# value is not present.

languages = ["Python", "Java", "C++"]

languages.remove("Java")

print("Updated list:", languages)


# EXAMPLE 22: Combining Lists
#
# The + operator combines lists
# into a new list.

python_tools = ["Python", "Jupyter"]

security_tools = ["Wireshark", "Nmap"]

combined_tools = python_tools + security_tools

print("Combined tools:", combined_tools)


# EXAMPLE 23: Repeating Lists
#
# The * operator repeats list elements.

numbers = [1, 2]

repeated_numbers = numbers * 3

print("Repeated list:", repeated_numbers)


# EXAMPLE 24: Finding Minimum and Maximum
#
# min() returns the smallest value.
# max() returns the largest value.

grades = [85, 92, 78, 95, 88]

print("Lowest grade:", min(grades))
print("Highest grade:", max(grades))


# EXAMPLE 25: Adding Numeric List Values
#
# sum() adds numeric elements.

grades = [85, 92, 78, 95, 88]

total = sum(grades)

print("Total:", total)


# EXAMPLE 26: Calculating an Average

grades = [85, 92, 78, 95, 88]

average = sum(grades) / len(grades)

print("Average grade:", average)


# EXAMPLE 27: Sorting a List
#
# sorted() creates a new sorted list.
#
# It does not modify the original list.

numbers = [50, 10, 40, 20, 30]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)


# EXAMPLE 28: List References
#
# Assigning a list to another variable
# does not automatically create a copy.
#
# Both variables can refer to
# the same list object.

original = [10, 20, 30]

reference = original

reference[0] = 99

print("Original:", original)
print("Reference:", reference)


# EXAMPLE 29: Copying a List
#
# copy() creates a shallow copy.
#
# For a flat list of integers,
# changes to one list do not
# affect the other list.

original = [10, 20, 30]

copied = original.copy()

copied[0] = 99

print("Original:", original)
print("Copied:", copied)


# EXAMPLE 30: Flower Inventory List

flowers = [
    "Roses",
    "Tulips",
    "Lilies",
    "Orchids"
]

for flower in flowers:
    print("Available flower:", flower)


# EXAMPLE 31: Flower Sales Revenue

bouquet_prices = [65, 75, 85, 95]

total_revenue = sum(bouquet_prices)

print("Total revenue: $", total_revenue)


# EXAMPLE 32: Customer Order List

orders = [
    "Order 001",
    "Order 002",
    "Order 003"
]

for order in orders:
    print("Processing:", order)


# EXAMPLE 33: Security Event List

security_events = [
    "login_success",
    "login_failed",
    "port_scan",
    "login_failed",
    "file_access"
]

for event in security_events:
    print("Security event:", event)


# EXAMPLE 34: Counting Failed Login Events

login_events = [
    "success",
    "failed",
    "failed",
    "success",
    "failed"
]

failed_count = 0

for event in login_events:
    if event == "failed":
        failed_count += 1

print("Failed login events:", failed_count)


# EXAMPLE 35: Network Port List
#
# This example reviews stored
# port numbers.
#
# It does not scan a network.

ports = [22, 80, 443, 3389, 8080]

for port in ports:
    print("Port:", port)


# EXAMPLE 36: Filtering List Values
#
# Create a new list containing
# values that meet a condition.

numbers = [5, 10, 15, 20, 25, 30]

filtered_numbers = []

for number in numbers:
    if number >= 20:
        filtered_numbers.append(number)

print("Filtered numbers:", filtered_numbers)


# EXAMPLE 37: Lists Inside Functions

def display_tools(tools):
    for tool in tools:
        print("Tool:", tool)


security_tools = [
    "Wireshark",
    "Nmap",
    "Python"
]

display_tools(security_tools)


# EXAMPLE 38: Returning a List

def create_languages():
    languages = ["Python", "C", "C++"]

    return languages


result = create_languages()

print("Languages:", result)


# EXAMPLE 39: Basic List Input
#
# This example collects three names
# and stores them in a list.

names = []

for number in range(3):
    name = input("Enter a name: ")
    names.append(name)

print("Collected names:", names)


# EXAMPLE 40: Basic Security Event Summary

events = [
    "success",
    "failed",
    "failed",
    "success",
    "failed",
    "success"
]

successful_logins = 0
failed_logins = 0

for event in events:
    if event == "success":
        successful_logins += 1
    elif event == "failed":
        failed_logins += 1

print("===== SECURITY SUMMARY =====")
print("Successful logins:", successful_logins)
print("Failed logins:", failed_logins)
print("Total events:", len(events))


# WHAT I LEARNED
#
# 1. Lists store multiple values.
# 2. Lists are created using [].
# 3. Lists preserve element order.
# 4. Lists are mutable.
# 5. Lists allow duplicate values.
# 6. Lists support multiple data types.
# 7. Indexing starts at zero.
# 8. Negative indexing counts backward.
# 9. Slicing extracts list portions.
# 10. len() counts list elements.
# 11. in checks list membership.
# 12. for loops iterate through lists.
# 13. enumerate() provides indexes.
# 14. append() adds elements.
# 15. remove() removes matching elements.
# 16. Lists can be combined.
# 17. sum() adds numeric elements.
# 18. min() and max() find extremes.
# 19. sorted() returns a sorted list.
# 20. Lists can be passed to functions.
# 21. Lists can be returned from functions.
# 22. Lists support security event analysis.
