
# ==========================================
# DAY 15 - TUPLES AND IMMUTABLE DATA
# Topic: Working with Tuples in Python
# ==========================================

# LESSON NOTES
#
# A tuple is an ordered collection
# of values.
#
# Tuples are commonly created using
# parentheses ().
#
# Tuples are:
#
# 1. Ordered
# 2. Immutable
# 3. Able to contain duplicate values
# 4. Able to contain different data types
#
# Immutable means tuple elements
# cannot be directly reassigned.
#
# Tuples support:
#
# Indexing
# Negative indexing
# Slicing
# Iteration
# Membership checks
# Unpacking
#
# Tuples have fewer methods than lists.
#
# The two main tuple methods are:
#
# count()
# index()
#
# Tuples are useful for fixed records,
# coordinates, configuration information,
# and collections that should not change.


# EXAMPLE 1: Creating a Tuple

languages = ("Python", "C", "C++")

print("Languages:", languages)


# EXAMPLE 2: Checking the Data Type

tools = ("Wireshark", "Nmap", "Python")

print("Data type:", type(tools))


# EXAMPLE 3: Creating an Empty Tuple

empty_tuple = ()

print("Empty tuple:", empty_tuple)
print("Length:", len(empty_tuple))


# EXAMPLE 4: Single-Element Tuple
#
# A comma is required when creating
# a tuple with one element.

single_item = ("Python",)

not_a_tuple = ("Python")

print(type(single_item))
print(type(not_a_tuple))


# EXAMPLE 5: Tuple Packing
#
# Python can create tuples
# without parentheses.

student = "Alex", 23, "Cyber Defense"

print("Student:", student)
print("Type:", type(student))


# EXAMPLE 6: Mixed Data Types

student_record = (
    "Alex",
    23,
    3.5,
    True
)

print("Student record:", student_record)


# EXAMPLE 7: Accessing Tuple Elements
#
# Indexing starts at zero.

languages = ("Python", "C", "C++")

print("First:", languages[0])
print("Second:", languages[1])
print("Third:", languages[2])


# EXAMPLE 8: Negative Indexing
#
# Negative indexes count backward.

tools = ("Wireshark", "Nmap", "Python")

print("Last tool:", tools[-1])
print("Second-to-last:", tools[-2])


# EXAMPLE 9: Tuple Length
#
# len() counts tuple elements.

ports = (22, 80, 443, 3389)

print("Number of ports:", len(ports))


# EXAMPLE 10: Tuple Slicing
#
# Slicing creates a new tuple
# containing selected elements.
#
# The stop index is excluded.

numbers = (10, 20, 30, 40, 50)

print("First three:", numbers[:3])
print("From index 2:", numbers[2:])


# EXAMPLE 11: Slicing with a Step

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

print("Every second value:", numbers[::2])


# EXAMPLE 12: Reversing a Tuple

numbers = (1, 2, 3, 4, 5)

reversed_numbers = numbers[::-1]

print("Original:", numbers)
print("Reversed:", reversed_numbers)


# EXAMPLE 13: Tuple Membership

tools = ("Wireshark", "Nmap", "Python")

print("Python" in tools)
print("Java" in tools)


# EXAMPLE 14: Using not in

authorized_roles = (
    "admin",
    "analyst",
    "employee"
)

role = "guest"

if role not in authorized_roles:
    print("Role not listed.")
else:
    print("Role is listed.")


# EXAMPLE 15: Iterating Through a Tuple

languages = ("Python", "C", "C++")

for language in languages:
    print("Language:", language)


# EXAMPLE 16: Using enumerate()

tools = ("Wireshark", "Nmap", "Python")

for index, tool in enumerate(tools, start=1):
    print(index, tool)


# EXAMPLE 17: Tuple Immutability
#
# Tuple elements cannot be reassigned.
#
# This code would raise TypeError:
#
# languages = ("Python", "C", "C++")
# languages[0] = "Java"
#
# The incorrect assignment remains
# commented out so the lesson runs.

languages = ("Python", "C", "C++")

print("Original tuple:", languages)


# EXAMPLE 18: Creating a New Tuple
#
# To change tuple contents,
# create a new tuple.

languages = ("Python", "C", "C++")

updated_languages = ("Java",) + languages[1:]

print("Original:", languages)
print("Updated:", updated_languages)


# EXAMPLE 19: Concatenating Tuples
#
# The + operator creates a new tuple.

python_tools = ("Python", "Jupyter")

security_tools = ("Wireshark", "Nmap")

combined = python_tools + security_tools

print("Combined:", combined)


# EXAMPLE 20: Repeating Tuples
#
# The * operator creates a
# repeated tuple.

numbers = (1, 2)

repeated = numbers * 3

print("Repeated:", repeated)


# EXAMPLE 21: Using count()
#
# count() returns the number
# of matching elements.

events = (
    "failed",
    "success",
    "failed",
    "failed"
)

failed_count = events.count("failed")

print("Failed events:", failed_count)


# EXAMPLE 22: Using index()
#
# index() returns the position
# of the first matching value.
#
# It raises ValueError if absent.

tools = ("Wireshark", "Nmap", "Python")

position = tools.index("Nmap")

print("Nmap index:", position)


# EXAMPLE 23: Safe Tuple Search

tools = ("Wireshark", "Nmap", "Python")

search_tool = "Linux"

if search_tool in tools:
    print("Index:", tools.index(search_tool))
else:
    print("Tool not found.")


# EXAMPLE 24: Tuple Unpacking
#
# Unpacking assigns tuple elements
# to separate variables.

student = ("Alex", 23, "Cyber Defense")

name, age, major = student

print("Name:", name)
print("Age:", age)
print("Major:", major)


# EXAMPLE 25: Extended Unpacking
#
# The * operator can collect
# remaining elements into a list.

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# EXAMPLE 26: Swapping Variables
#
# Tuple packing and unpacking
# can exchange values.

first = 10
second = 20

first, second = second, first

print("First:", first)
print("Second:", second)


# EXAMPLE 27: Converting a List to a Tuple
#
# tuple() creates a tuple
# from an iterable.

languages_list = ["Python", "C", "C++"]

languages_tuple = tuple(languages_list)

print("Tuple:", languages_tuple)


# EXAMPLE 28: Converting a Tuple to a List
#
# list() creates a list
# from an iterable.

languages_tuple = ("Python", "C", "C++")

languages_list = list(languages_tuple)

print("List:", languages_list)


# EXAMPLE 29: Changing Data Through Conversion
#
# A tuple can be converted to a list,
# modified, then converted back.
#
# This creates a new tuple.

original = ("Python", "Java", "C++")

temporary_list = list(original)

temporary_list[1] = "C"

updated = tuple(temporary_list)

print("Original:", original)
print("Updated:", updated)


# EXAMPLE 30: Nested Tuples
#
# A tuple can contain other tuples.

students = (
    ("Alex", 90),
    ("Morgan", 85),
    ("Chris", 95)
)

for student in students:
    print("Student:", student)


# EXAMPLE 31: Unpacking Nested Records

students = (
    ("Alex", 90),
    ("Morgan", 85),
    ("Chris", 95)
)

for name, grade in students:
    print(name, "earned", grade)


# EXAMPLE 32: Tuples Containing Lists
#
# A tuple cannot replace an element,
# but mutable objects stored inside
# the tuple may still be changed.

record = ("Alex", ["Python", "C"])

record[1].append("C++")

print("Updated nested list:", record)


# EXAMPLE 33: Minimum and Maximum

numbers = (12, 5, 25, 8, 17)

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))


# EXAMPLE 34: Sum and Average

grades = (85, 92, 78, 95, 88)

total = sum(grades)
average = total / len(grades)

print("Total:", total)
print("Average:", average)


# EXAMPLE 35: Sorting a Tuple
#
# sorted() returns a list.
#
# The original tuple remains unchanged.

numbers = (50, 10, 40, 20, 30)

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted list:", sorted_numbers)


# EXAMPLE 36: Returning a Sorted Tuple

numbers = (50, 10, 40, 20, 30)

sorted_tuple = tuple(sorted(numbers))

print("Sorted tuple:", sorted_tuple)


# EXAMPLE 37: Tuples Inside Functions

def display_ports(ports):
    for port in ports:
        print("Port:", port)


network_ports = (22, 80, 443, 3389)

display_ports(network_ports)


# EXAMPLE 38: Returning a Tuple

def create_student_record():
    return ("Alex", 23, "Cyber Defense")


student = create_student_record()

print("Student:", student)


# EXAMPLE 39: Returning Multiple Values
#
# A function can return multiple values
# using tuple packing.

def calculate_results(a, b):
    total = a + b
    difference = a - b

    return total, difference


addition, subtraction = calculate_results(20, 5)

print("Addition:", addition)
print("Subtraction:", subtraction)


# EXAMPLE 40: Flower Product Record
#
# A tuple can represent a product
# with a name and fixed sample price.

flower_product = ("Rose Bouquet", 75.00)

name, price = flower_product

print("Product:", name)
print(f"Price: ${price:.2f}")


# EXAMPLE 41: Flower Product Collection

products = (
    ("Rose Bouquet", 75.00),
    ("Tulip Bouquet", 65.00),
    ("Lily Bouquet", 85.00)
)

for name, price in products:
    print(f"{name}: ${price:.2f}")


# EXAMPLE 42: Network Port Definitions
#
# This example stores common
# service-port associations.
#
# It does not scan a network.
#
# Services may use nonstandard ports.

services = (
    ("SSH", 22),
    ("HTTP", 80),
    ("HTTPS", 443),
    ("RDP", 3389)
)

for service, port in services:
    print(f"{service}: {port}")


# EXAMPLE 43: Security Event Records

security_events = (
    ("login_success", "alex"),
    ("login_failed", "admin"),
    ("port_scan", "unknown"),
    ("login_failed", "guest")
)

for event_type, username in security_events:
    print("Event:", event_type)
    print("User:", username)


# EXAMPLE 44: Counting Failed Logins

events = (
    "success",
    "failed",
    "failed",
    "success",
    "failed"
)

failed_count = events.count("failed")

print("Failed login events:", failed_count)


# EXAMPLE 45: Comparing Lists and Tuples
#
# Lists use [] and are mutable.
#
# Tuples commonly use () and
# cannot have elements reassigned.

languages_list = ["Python", "C", "C++"]

languages_tuple = ("Python", "C", "C++")

languages_list[0] = "Java"

print("Modified list:", languages_list)
print("Unchanged tuple:", languages_tuple)


# EXAMPLE 46: Basic Security Configuration
#
# A tuple can represent a collection
# of configuration values.
#
# Immutability helps prevent accidental
# element reassignment.
#
# It is not a security boundary.

security_configuration = (
    "SSH",
    22,
    True
)

service, port, enabled = security_configuration

print("===== SECURITY CONFIGURATION =====")
print("Service:", service)
print("Port:", port)
print("Enabled:", enabled)


# WHAT I LEARNED
#
# 1. Tuples are ordered collections.
# 2. Tuples are immutable.
# 3. Tuples allow duplicate values.
# 4. Tuples can contain mixed data types.
# 5. Single-element tuples need a comma.
# 6. Tuples support indexing.
# 7. Tuples support slicing.
# 8. Tuples support iteration.
# 9. count() counts matching values.
# 10. index() finds an element position.
# 11. Tuples support unpacking.
# 12. Extended unpacking uses *.
# 13. Tuples can be concatenated.
# 14. Tuples can be repeated.
# 15. Lists can be converted to tuples.
# 16. Tuples can be converted to lists.
# 17. Nested tuples organize records.
# 18. Mutable objects inside tuples
#     can still change.
# 19. Functions can return tuples.
# 20. Tuples can store fixed records.
# 21. Tuples can organize network data.
# 22. Tuples support security event analysis.
