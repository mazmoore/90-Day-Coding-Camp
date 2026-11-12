
# ==========================================
# DAY 14 - LIST METHODS
# Topic: List Methods and Manipulation
# ==========================================

# LESSON NOTES
#
# Python lists store multiple values.
#
# Lists are mutable, which means their
# contents can be changed.
#
# List methods are built-in operations
# that help modify or inspect lists.
#
# Common list methods include:
#
# append()
# extend()
# insert()
# remove()
# pop()
# clear()
# index()
# count()
# sort()
# reverse()
# copy()
#
# Many list methods modify the
# original list directly.
#
# Methods such as append(), sort(),
# and reverse() return None.
#
# Do not assign their return values
# when you want the updated list.


# EXAMPLE 1: Using append()
#
# append() adds one element
# to the end of a list.

languages = ["Python", "C"]

languages.append("C++")

print("Updated languages:", languages)


# EXAMPLE 2: Appending Multiple Values
#
# append() adds one object at a time.
#
# A loop can append several values.

numbers = []

for number in range(1, 6):
    numbers.append(number)

print("Numbers:", numbers)


# EXAMPLE 3: Using extend()
#
# extend() adds elements from
# another iterable to the list.

languages = ["Python", "C"]

languages.extend(["C++", "Java"])

print("Extended list:", languages)


# EXAMPLE 4: append() Versus extend()
#
# append() adds the supplied object
# as one element.
#
# extend() adds each element from
# the supplied iterable.

list_one = [1, 2]
list_two = [1, 2]

list_one.append([3, 4])
list_two.extend([3, 4])

print("Using append:", list_one)
print("Using extend:", list_two)


# EXAMPLE 5: Using insert()
#
# insert(index, value) adds an element
# at a specified position.

languages = ["Python", "C++"]

languages.insert(1, "C")

print("Updated list:", languages)


# EXAMPLE 6: Inserting at the Beginning

tools = ["Nmap", "Python"]

tools.insert(0, "Wireshark")

print("Tools:", tools)


# EXAMPLE 7: Using remove()
#
# remove() deletes the first
# matching element.
#
# It raises ValueError if the
# element is not present.

languages = ["Python", "Java", "C++"]

languages.remove("Java")

print("Updated list:", languages)


# EXAMPLE 8: Removing Duplicate Values
#
# remove() deletes only the first
# matching occurrence.

events = ["failed", "success", "failed"]

events.remove("failed")

print("Remaining events:", events)


# EXAMPLE 9: Safe Removal
#
# Check membership before removing
# an element that may not exist.

tools = ["Wireshark", "Nmap", "Python"]

tool_to_remove = "Java"

if tool_to_remove in tools:
    tools.remove(tool_to_remove)
else:
    print("Tool not found.")

print("Tools:", tools)


# EXAMPLE 10: Using pop()
#
# pop() removes and returns
# the last element by default.

numbers = [10, 20, 30]

removed_number = numbers.pop()

print("Removed:", removed_number)
print("Remaining:", numbers)


# EXAMPLE 11: pop() with an Index
#
# pop(index) removes and returns
# the element at that position.

numbers = [10, 20, 30, 40]

removed_number = numbers.pop(1)

print("Removed:", removed_number)
print("Remaining:", numbers)


# EXAMPLE 12: Safe pop()
#
# Calling pop() on an empty list
# raises IndexError.

tasks = []

if tasks:
    completed_task = tasks.pop()
    print("Completed:", completed_task)
else:
    print("No tasks available.")


# EXAMPLE 13: Using clear()
#
# clear() removes all elements
# from a list.

numbers = [10, 20, 30]

numbers.clear()

print("Cleared list:", numbers)


# EXAMPLE 14: Using index()
#
# index() returns the position
# of the first matching element.
#
# It raises ValueError if the
# value is not present.

tools = ["Wireshark", "Nmap", "Python"]

position = tools.index("Nmap")

print("Nmap position:", position)


# EXAMPLE 15: Safe index()
#
# Check whether an element exists
# before using index().

tools = ["Wireshark", "Nmap", "Python"]

search_tool = "Linux"

if search_tool in tools:
    print("Position:", tools.index(search_tool))
else:
    print("Tool not found.")


# EXAMPLE 16: Using count()
#
# count() returns the number
# of matching elements.

events = [
    "failed",
    "success",
    "failed",
    "failed"
]

failed_count = events.count("failed")

print("Failed events:", failed_count)


# EXAMPLE 17: Using sort()
#
# sort() sorts the original list
# in ascending order.

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Sorted numbers:", numbers)


# EXAMPLE 18: Descending Sort
#
# reverse=True sorts in
# descending order.

numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print("Descending:", numbers)


# EXAMPLE 19: Sorting Strings
#
# Strings are sorted according
# to their comparison rules.

tools = ["Python", "Nmap", "Wireshark"]

tools.sort()

print("Sorted tools:", tools)


# EXAMPLE 20: Case-Insensitive Sorting
#
# key=str.lower sorts strings
# using lowercase comparison values.

names = ["alex", "Morgan", "chris"]

names.sort(key=str.lower)

print("Sorted names:", names)


# EXAMPLE 21: sort() Versus sorted()
#
# sort() changes the original list.
#
# sorted() returns a new list.

numbers = [30, 10, 20]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted copy:", sorted_numbers)


# EXAMPLE 22: Using reverse()
#
# reverse() reverses the current
# order of list elements.
#
# It does not sort the list.

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print("Reversed:", numbers)


# EXAMPLE 23: reverse() Versus Slicing
#
# reverse() modifies the original.
#
# [::-1] creates a reversed copy.

numbers = [1, 2, 3, 4, 5]

reversed_copy = numbers[::-1]

print("Original:", numbers)
print("Reversed copy:", reversed_copy)


# EXAMPLE 24: Using copy()
#
# copy() creates a shallow copy.
#
# Changes to top-level elements
# are independent.
#
# Nested mutable objects can still
# be shared between the lists.

original = ["Python", "C", "C++"]

copied = original.copy()

copied.append("Java")

print("Original:", original)
print("Copied:", copied)


# EXAMPLE 25: List Assignment Versus Copy
#
# Assignment creates another reference
# to the same list object.

original = [10, 20, 30]

reference = original

reference.append(40)

print("Original:", original)
print("Reference:", reference)


# EXAMPLE 26: Using del
#
# del is a Python statement,
# not a list method.
#
# It can remove elements by index.

numbers = [10, 20, 30, 40]

del numbers[1]

print("After deletion:", numbers)


# EXAMPLE 27: Removing a Slice
#
# del can remove several elements.

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print("Remaining:", numbers)


# EXAMPLE 28: Updating Multiple Elements
#
# Slice assignment can replace
# several list elements.

numbers = [10, 20, 30, 40]

numbers[1:3] = [25, 35]

print("Updated:", numbers)


# EXAMPLE 29: Building a List with a Loop

even_numbers = []

for number in range(1, 11):
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)


# EXAMPLE 30: List Comprehension
#
# A list comprehension provides
# a concise way to create a list.
#
# This is an introduction only.

even_numbers = [
    number for number in range(1, 11)
    if number % 2 == 0
]

print("Even numbers:", even_numbers)


# EXAMPLE 31: Flower Inventory Management

flowers = ["Roses", "Tulips", "Lilies"]

flowers.append("Orchids")
flowers.insert(1, "Sunflowers")

print("Available flowers:", flowers)


# EXAMPLE 32: Removing Flower Inventory

flowers = [
    "Roses",
    "Tulips",
    "Lilies",
    "Orchids"
]

flowers.remove("Tulips")

print("Updated inventory:", flowers)


# EXAMPLE 33: Sorting Bouquet Prices

bouquet_prices = [95, 65, 85, 75]

bouquet_prices.sort()

print("Prices low to high:", bouquet_prices)

bouquet_prices.sort(reverse=True)

print("Prices high to low:", bouquet_prices)


# EXAMPLE 34: Customer Order Queue
#
# This example processes orders
# from the beginning of a list.
#
# For large queues, other data
# structures may be more efficient.

orders = [
    "Order 001",
    "Order 002",
    "Order 003"
]

while orders:
    current_order = orders.pop(0)

    print("Processing:", current_order)

print("All orders processed.")


# EXAMPLE 35: Security Event Collection

security_events = []

security_events.append("login_success")
security_events.append("login_failed")
security_events.append("port_scan")

print("Collected events:", security_events)


# EXAMPLE 36: Counting Security Events

events = [
    "login_success",
    "login_failed",
    "login_failed",
    "port_scan",
    "login_failed"
]

failed_count = events.count("login_failed")

print("Failed logins:", failed_count)


# EXAMPLE 37: Filtering Security Events

events = [
    "login_success",
    "login_failed",
    "port_scan",
    "login_failed",
    "file_access"
]

failed_events = []

for event in events:
    if event == "login_failed":
        failed_events.append(event)

print("Failed events:", failed_events)


# EXAMPLE 38: Combining Security Event Lists

server_one = [
    "login_success",
    "login_failed"
]

server_two = [
    "port_scan",
    "login_failed"
]

server_one.extend(server_two)

print("Combined events:", server_one)


# EXAMPLE 39: Sorting Security Alert Counts

failed_login_counts = [12, 3, 25, 7, 18]

failed_login_counts.sort(reverse=True)

print("Highest counts first:", failed_login_counts)


# EXAMPLE 40: Using List Methods in Functions

def add_security_event(events, event):
    events.append(event)


security_events = []

add_security_event(
    security_events,
    "login_failed"
)

add_security_event(
    security_events,
    "port_scan"
)

print("Events:", security_events)


# EXAMPLE 41: Returning a Modified Copy
#
# This function creates a copy
# before adding a new element.
#
# The original list stays unchanged.

def create_updated_list(items, new_item):
    updated = items.copy()

    updated.append(new_item)

    return updated


original_tools = ["Wireshark", "Nmap"]

updated_tools = create_updated_list(
    original_tools,
    "Python"
)

print("Original:", original_tools)
print("Updated:", updated_tools)


# EXAMPLE 42: List Method Return Values
#
# append(), sort(), and reverse()
# modify the list and return None.

numbers = [3, 1, 2]

result = numbers.sort()

print("Sort return value:", result)
print("Updated numbers:", numbers)


# EXAMPLE 43: Basic Security Event Manager

events = [
    "login_success",
    "login_failed",
    "port_scan",
    "login_failed"
]

events.append("file_access")

failed_count = events.count("login_failed")

sorted_events = sorted(events)

print("===== SECURITY EVENT MANAGER =====")
print("Total events:", len(events))
print("Failed logins:", failed_count)
print("Sorted events:", sorted_events)


# WHAT I LEARNED
#
# 1. append() adds one element.
# 2. extend() adds multiple elements.
# 3. insert() adds at a position.
# 4. remove() deletes a matching value.
# 5. pop() removes and returns an element.
# 6. clear() empties a list.
# 7. index() finds an element position.
# 8. count() counts matching values.
# 9. sort() modifies list order.
# 10. sorted() returns a sorted list.
# 11. reverse() reverses element order.
# 12. copy() creates a shallow copy.
# 13. del removes elements by position.
# 14. Slice assignment replaces elements.
# 15. Loops can build new lists.
# 16. List comprehensions create lists.
# 17. Lists can manage business inventory.
# 18. Lists can organize security events.
# 19. Functions can modify lists.
# 20. Many list methods return None.
