
# ==========================================
# DAY 16 - DICTIONARIES
# Topic: Dictionaries and Key-Value Data
# ==========================================

# LESSON NOTES
#
# A dictionary stores information
# as key-value pairs.
#
# Dictionaries are created using
# curly braces {}.
#
# Example:
#
# student = {
#     "name": "Alex",
#     "age": 23
# }
#
# "name" is a key.
# "Alex" is its associated value.
#
# Dictionaries are:
#
# 1. Mutable
# 2. Insertion-ordered
# 3. Based on key-value pairs
# 4. Able to store different data types
#
# Dictionary keys must be unique
# and hashable.
#
# Strings, integers, and tuples
# containing only hashable values
# can be used as keys.
#
# Lists cannot be dictionary keys.
#
# Values may contain many data types.
#
# Dictionaries are useful for:
#
# Student records
# User profiles
# Customer information
# Inventory management
# Security logs
# Network configurations


# EXAMPLE 1: Creating a Dictionary

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

print("Student:", student)


# EXAMPLE 2: Checking the Data Type

student = {
    "name": "Alex",
    "age": 23
}

print("Data type:", type(student))


# EXAMPLE 3: Creating an Empty Dictionary

security_event = {}

print("Empty dictionary:", security_event)


# EXAMPLE 4: Accessing Dictionary Values
#
# Dictionary values are accessed
# using their keys.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])


# EXAMPLE 5: Using get()
#
# get() retrieves a value by key.
#
# Unlike square bracket access,
# get() returns None by default
# when the key does not exist.

student = {
    "name": "Alex",
    "age": 23
}

print("Name:", student.get("name"))
print("GPA:", student.get("gpa"))


# EXAMPLE 6: Using a Default Value
#
# get() can return a custom
# default when a key is absent.

student = {
    "name": "Alex",
    "age": 23
}

gpa = student.get("gpa", "Not available")

print("GPA:", gpa)


# EXAMPLE 7: Modifying Dictionary Values
#
# Dictionaries are mutable.
#
# Existing values can be updated
# using their keys.

student = {
    "name": "Alex",
    "age": 23
}

student["age"] = 24

print("Updated student:", student)


# EXAMPLE 8: Adding New Key-Value Pairs
#
# Assigning a new key adds
# a new dictionary entry.

student = {
    "name": "Alex",
    "age": 23
}

student["major"] = "Cyber Defense"

print("Updated student:", student)


# EXAMPLE 9: Dictionary Keys Must Be Unique
#
# Duplicate keys do not create
# separate dictionary entries.
#
# The later value replaces
# the earlier value.

student = {
    "name": "Alex",
    "name": "Morgan"
}

print("Student:", student)


# EXAMPLE 10: Dictionary Length
#
# len() counts key-value pairs.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

print("Number of fields:", len(student))


# EXAMPLE 11: Checking Key Membership
#
# in checks whether a key
# exists in a dictionary.

student = {
    "name": "Alex",
    "age": 23
}

print("name" in student)
print("major" in student)


# EXAMPLE 12: Using not in

user = {
    "username": "alex",
    "role": "analyst"
}

if "email" not in user:
    print("Email field is missing.")
else:
    print("Email field exists.")


# EXAMPLE 13: Using keys()
#
# keys() returns a view
# of dictionary keys.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

print("Keys:", student.keys())


# EXAMPLE 14: Using values()
#
# values() returns a view
# of dictionary values.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

print("Values:", student.values())


# EXAMPLE 15: Using items()
#
# items() returns a view
# of key-value pairs.

student = {
    "name": "Alex",
    "age": 23
}

print("Items:", student.items())


# EXAMPLE 16: Iterating Through Keys
#
# A for loop over a dictionary
# iterates through its keys.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

for key in student:
    print("Key:", key)


# EXAMPLE 17: Iterating Through Values

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

for value in student.values():
    print("Value:", value)


# EXAMPLE 18: Iterating Through Key-Value Pairs
#
# items() allows each key
# and value to be unpacked.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

for key, value in student.items():
    print(key, ":", value)


# EXAMPLE 19: Using update()
#
# update() adds new entries
# and replaces existing values.

student = {
    "name": "Alex",
    "age": 23
}

student.update({
    "age": 24,
    "major": "Cyber Defense"
})

print("Updated student:", student)


# EXAMPLE 20: Using pop()
#
# pop(key) removes an entry
# and returns its value.
#
# It raises KeyError if the
# key is absent and no
# default is provided.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

removed_major = student.pop("major")

print("Removed:", removed_major)
print("Remaining:", student)


# EXAMPLE 21: Safe pop()
#
# Providing a default prevents
# KeyError for a missing key.

student = {
    "name": "Alex",
    "age": 23
}

removed = student.pop("gpa", None)

print("Removed value:", removed)


# EXAMPLE 22: Using popitem()
#
# popitem() removes and returns
# the most recently inserted pair.
#
# Calling it on an empty dictionary
# raises KeyError.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

removed_pair = student.popitem()

print("Removed pair:", removed_pair)
print("Remaining:", student)


# EXAMPLE 23: Using del
#
# del removes an entry by key.
#
# It raises KeyError if the
# specified key does not exist.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

del student["age"]

print("Updated student:", student)


# EXAMPLE 24: Using clear()
#
# clear() removes all entries.

student = {
    "name": "Alex",
    "age": 23
}

student.clear()

print("Cleared dictionary:", student)


# EXAMPLE 25: Copying a Dictionary
#
# copy() creates a shallow copy.
#
# Top-level changes are independent.
#
# Nested mutable objects may still
# be shared between the dictionaries.

original = {
    "name": "Alex",
    "age": 23
}

copied = original.copy()

copied["age"] = 24

print("Original:", original)
print("Copied:", copied)


# EXAMPLE 26: Dictionary References
#
# Assignment does not create
# an independent dictionary.

original = {
    "name": "Alex"
}

reference = original

reference["name"] = "Morgan"

print("Original:", original)
print("Reference:", reference)


# EXAMPLE 27: Using setdefault()
#
# setdefault() returns an existing
# value or inserts a default value
# when the key is absent.

student = {
    "name": "Alex"
}

student.setdefault("major", "Cyber Defense")

print("Student:", student)


# EXAMPLE 28: Creating a Dictionary with dict()

student = dict(
    name="Alex",
    age=23,
    major="Cyber Defense"
)

print("Student:", student)


# EXAMPLE 29: Different Value Types
#
# Dictionary values can include
# strings, numbers, Booleans,
# lists, and tuples.

student = {
    "name": "Alex",
    "age": 23,
    "enrolled": True,
    "courses": ["Python", "Networking"],
    "grades": (90, 85, 95)
}

print("Student record:", student)


# EXAMPLE 30: Nested Dictionaries
#
# A dictionary can contain
# another dictionary.

students = {
    "student_1": {
        "name": "Alex",
        "major": "Cyber Defense"
    },
    "student_2": {
        "name": "Morgan",
        "major": "Information Technology"
    }
}

print(students["student_1"]["name"])


# EXAMPLE 31: Iterating Through Nested Dictionaries

students = {
    "student_1": {
        "name": "Alex",
        "major": "Cyber Defense"
    },
    "student_2": {
        "name": "Morgan",
        "major": "Information Technology"
    }
}

for student_id, information in students.items():
    print("Student ID:", student_id)
    print("Name:", information["name"])
    print("Major:", information["major"])


# EXAMPLE 32: Dictionary of Network Ports
#
# This is a stored reference
# of common service ports.
#
# It does not scan a network.

network_ports = {
    "SSH": 22,
    "HTTP": 80,
    "HTTPS": 443,
    "RDP": 3389
}

for service, port in network_ports.items():
    print(f"{service}: {port}")


# EXAMPLE 33: Counting Security Events
#
# Dictionaries can store counts
# for different event categories.

event_counts = {
    "success": 0,
    "failed": 0
}

events = [
    "success",
    "failed",
    "failed",
    "success",
    "failed"
]

for event in events:
    if event in event_counts:
        event_counts[event] += 1

print("Event counts:", event_counts)


# EXAMPLE 34: Counting Multiple Event Types
#
# get() can supply a starting
# count of zero.

events = [
    "login_success",
    "login_failed",
    "port_scan",
    "login_failed",
    "file_access"
]

event_counts = {}

for event in events:
    event_counts[event] = (
        event_counts.get(event, 0) + 1
    )

print("Event summary:", event_counts)


# EXAMPLE 35: Flower Inventory Dictionary
#
# Keys identify flower varieties.
# Values represent available quantities.

flower_inventory = {
    "Roses": 100,
    "Tulips": 75,
    "Lilies": 50
}

for flower, quantity in flower_inventory.items():
    print(f"{flower}: {quantity} available")


# EXAMPLE 36: Updating Flower Inventory

flower_inventory = {
    "Roses": 100,
    "Tulips": 75
}

flower_inventory["Roses"] -= 25

print("Updated inventory:", flower_inventory)


# EXAMPLE 37: Flower Product Pricing

bouquet_prices = {
    "Rose Bouquet": 75.00,
    "Tulip Bouquet": 65.00,
    "Lily Bouquet": 85.00
}

for product, price in bouquet_prices.items():
    print(f"{product}: ${price:.2f}")


# EXAMPLE 38: Customer Order Record

order = {
    "order_id": "001",
    "customer": "Alex",
    "product": "Rose Bouquet",
    "quantity": 2,
    "unit_price": 75.00
}

total = order["quantity"] * order["unit_price"]

print("===== CUSTOMER ORDER =====")
print("Order:", order["order_id"])
print("Customer:", order["customer"])
print("Product:", order["product"])
print(f"Total: ${total:.2f}")


# EXAMPLE 39: Security Event Record

security_event = {
    "event_type": "login_failed",
    "username": "admin",
    "source_ip": "192.0.2.10",
    "port": 22
}

for key, value in security_event.items():
    print(f"{key}: {value}")


# EXAMPLE 40: Basic User Profile

user_profile = {
    "username": "cyberstudent",
    "role": "analyst",
    "active": True
}

print("Username:", user_profile["username"])
print("Role:", user_profile["role"])
print("Active:", user_profile["active"])


# EXAMPLE 41: Dictionary Function

def display_profile(profile):
    for key, value in profile.items():
        print(f"{key}: {value}")


profile = {
    "username": "alex",
    "role": "analyst"
}

display_profile(profile)


# EXAMPLE 42: Returning a Dictionary

def create_security_event(event_type, username):
    return {
        "event_type": event_type,
        "username": username
    }


event = create_security_event(
    "login_failed",
    "admin"
)

print("Created event:", event)


# EXAMPLE 43: Dictionary Comprehension
#
# A dictionary comprehension creates
# a dictionary using a concise expression.

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print("Squares:", squares)


# EXAMPLE 44: Dictionary Input
#
# This example collects basic
# user information.

username = input("Enter username: ")
role = input("Enter role: ")

user = {
    "username": username,
    "role": role
}

print("User record:", user)


# EXAMPLE 45: Basic Security Event Report

events = [
    "login_success",
    "login_failed",
    "port_scan",
    "login_failed",
    "file_access",
    "login_success"
]

event_counts = {}

for event in events:
    event_counts[event] = (
        event_counts.get(event, 0) + 1
    )

print("===== SECURITY EVENT REPORT =====")

for event_type, count in event_counts.items():
    print(f"{event_type}: {count}")

print("Total events:", len(events))


# WHAT I LEARNED
#
# 1. Dictionaries store key-value pairs.
# 2. Dictionaries use curly braces {}.
# 3. Keys must be unique and hashable.
# 4. Values can contain different types.
# 5. Dictionaries are mutable.
# 6. Dictionaries preserve insertion order.
# 7. Keys provide access to values.
# 8. get() safely retrieves values.
# 9. Existing values can be updated.
# 10. New key-value pairs can be added.
# 11. keys() provides dictionary keys.
# 12. values() provides dictionary values.
# 13. items() provides key-value pairs.
# 14. update() modifies dictionaries.
# 15. pop() removes entries by key.
# 16. popitem() removes the last pair.
# 17. clear() empties dictionaries.
# 18. copy() creates a shallow copy.
# 19. Dictionaries can be nested.
# 20. Dictionaries can count events.
# 21. Functions can return dictionaries.
# 22. Dictionaries support security reports.
