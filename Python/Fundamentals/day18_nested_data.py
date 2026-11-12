
# ==========================================
# DAY 18 - NESTED DATA STRUCTURES
# Topic: Combining Python Collections
# ==========================================

# LESSON NOTES
#
# A nested data structure contains
# one collection inside another.
#
# Python collections include:
#
# Lists
# Tuples
# Dictionaries
# Sets
#
# Nested structures help organize
# information with multiple levels.
#
# Examples:
#
# A list of student dictionaries
# A dictionary of customer orders
# A list containing other lists
# A dictionary containing lists
# A dictionary containing sets
#
# Nested structures are useful for:
#
# Student management
# Inventory tracking
# Customer orders
# Security event records
# Network configurations
# Log analysis
#
# Accessing nested data often requires
# multiple indexes or keys.
#
# Example:
#
# student["courses"][0]
#
# First, Python accesses "courses".
# Then, it accesses index 0.


# EXAMPLE 1: Nested Lists
#
# A nested list contains
# one or more lists.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Nested list:", numbers)


# EXAMPLE 2: Accessing Nested Lists
#
# The first index selects
# an inner list.
#
# The second index selects
# an element inside that list.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("First row:", numbers[0])
print("First value:", numbers[0][0])
print("Center value:", numbers[1][1])


# EXAMPLE 3: Modifying Nested Lists

numbers = [
    [1, 2, 3],
    [4, 5, 6]
]

numbers[0][1] = 20

print("Updated nested list:", numbers)


# EXAMPLE 4: Iterating Through Nested Lists
#
# Nested loops can process
# multiple levels of data.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for number in row:
        print("Number:", number)


# EXAMPLE 5: Accessing Rows and Columns
#
# enumerate() provides row
# and column indexes.

matrix = [
    [10, 20],
    [30, 40]
]

for row_index, row in enumerate(matrix):
    for column_index, value in enumerate(row):
        print(
            "Row:", row_index,
            "Column:", column_index,
            "Value:", value
        )


# EXAMPLE 6: Nested Tuples
#
# Tuples can contain other tuples.

coordinates = (
    (10, 20),
    (30, 40),
    (50, 60)
)

print("Coordinates:", coordinates)
print("First pair:", coordinates[0])


# EXAMPLE 7: Unpacking Nested Tuples

coordinates = (
    (10, 20),
    (30, 40),
    (50, 60)
)

for x, y in coordinates:
    print("X:", x, "Y:", y)


# EXAMPLE 8: Dictionary Containing a List

student = {
    "name": "Alex",
    "courses": [
        "Python",
        "Networking",
        "Cybersecurity"
    ]
}

print("Student:", student)
print("Courses:", student["courses"])


# EXAMPLE 9: Accessing a List in a Dictionary

student = {
    "name": "Alex",
    "courses": [
        "Python",
        "Networking",
        "Cybersecurity"
    ]
}

print("First course:", student["courses"][0])
print("Last course:", student["courses"][-1])


# EXAMPLE 10: Modifying a Nested List

student = {
    "name": "Alex",
    "courses": ["Python", "Networking"]
}

student["courses"].append("Cybersecurity")

print("Updated student:", student)


# EXAMPLE 11: Dictionary Containing a Tuple
#
# A tuple can store fixed values
# inside a dictionary.

student = {
    "name": "Alex",
    "grades": (90, 85, 95)
}

print("Grades:", student["grades"])
print("Highest:", max(student["grades"]))


# EXAMPLE 12: Dictionary Containing a Set
#
# Sets store unique values.

user = {
    "username": "alex",
    "permissions": {
        "read",
        "write"
    }
}

print("Permissions:", user["permissions"])


# EXAMPLE 13: Modifying a Nested Set

user = {
    "username": "alex",
    "permissions": {"read", "write"}
}

user["permissions"].add("execute")

print("Updated permissions:", user["permissions"])


# EXAMPLE 14: Nested Dictionaries
#
# A dictionary can contain
# other dictionaries.

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

print("Students:", students)


# EXAMPLE 15: Accessing Nested Dictionaries

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

print("First student:", students["student_1"]["name"])
print("Second major:", students["student_2"]["major"])


# EXAMPLE 16: Modifying Nested Dictionaries

students = {
    "student_1": {
        "name": "Alex",
        "major": "Cyber Defense"
    }
}

students["student_1"]["major"] = "Computer Science"

print("Updated students:", students)


# EXAMPLE 17: Adding a Nested Record

students = {
    "student_1": {
        "name": "Alex",
        "major": "Cyber Defense"
    }
}

students["student_2"] = {
    "name": "Morgan",
    "major": "Information Technology"
}

print("Students:", students)


# EXAMPLE 18: Iterating Through Nested Dictionaries

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

    for key, value in information.items():
        print(key, ":", value)


# EXAMPLE 19: List of Dictionaries
#
# Each dictionary represents
# one record.

students = [
    {
        "name": "Alex",
        "grade": 90
    },
    {
        "name": "Morgan",
        "grade": 85
    },
    {
        "name": "Chris",
        "grade": 95
    }
]

print("Student records:", students)


# EXAMPLE 20: Accessing a List of Dictionaries

students = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 85}
]

print("First name:", students[0]["name"])
print("Second grade:", students[1]["grade"])


# EXAMPLE 21: Iterating Through Records

students = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 85},
    {"name": "Chris", "grade": 95}
]

for student in students:
    print(
        student["name"],
        "earned",
        student["grade"]
    )


# EXAMPLE 22: Updating a Record

students = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 85}
]

students[1]["grade"] = 92

print("Updated records:", students)


# EXAMPLE 23: Adding a Record

students = [
    {"name": "Alex", "grade": 90}
]

students.append({
    "name": "Morgan",
    "grade": 85
})

print("Student records:", students)


# EXAMPLE 24: Filtering Nested Records

students = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 75},
    {"name": "Chris", "grade": 95}
]

high_grades = []

for student in students:
    if student["grade"] >= 90:
        high_grades.append(student)

print("High grades:", high_grades)


# EXAMPLE 25: Calculating a Nested Average

students = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 85},
    {"name": "Chris", "grade": 95}
]

total = 0

for student in students:
    total += student["grade"]

average = total / len(students)

print("Average grade:", average)


# EXAMPLE 26: Dictionary of Lists
#
# Each key identifies
# a collection of values.

courses = {
    "Python": ["Alex", "Morgan"],
    "Networking": ["Chris", "Taylor"],
    "Cybersecurity": ["Alex", "Chris"]
}

print("Python students:", courses["Python"])


# EXAMPLE 27: Iterating Through a Dictionary of Lists

courses = {
    "Python": ["Alex", "Morgan"],
    "Networking": ["Chris", "Taylor"]
}

for course, students in courses.items():
    print("Course:", course)

    for student in students:
        print("Student:", student)


# EXAMPLE 28: Dictionary of Tuples

network_services = {
    "SSH": (22, "TCP"),
    "HTTP": (80, "TCP"),
    "HTTPS": (443, "TCP")
}

for service, details in network_services.items():
    port, protocol = details

    print(service, port, protocol)


# EXAMPLE 29: Dictionary of Sets
#
# Each username has a set
# of assigned permission labels.

user_permissions = {
    "alex": {"read", "write"},
    "morgan": {"read"},
    "chris": {"read", "write", "execute"}
}

for username, permissions in user_permissions.items():
    print(username, sorted(permissions))


# EXAMPLE 30: Comparing Nested Permissions
#
# This compares stored labels.
#
# It does not grant or deny
# actual system access.

user_permissions = {
    "alex": {"read", "write"},
    "morgan": {"read"}
}

required_permissions = {"read", "write"}

for username, permissions in user_permissions.items():
    missing = required_permissions - permissions

    print(username, "missing:", sorted(missing))


# EXAMPLE 31: Flower Inventory Records

flower_inventory = [
    {
        "flower": "Roses",
        "quantity": 100,
        "price": 3.50
    },
    {
        "flower": "Tulips",
        "quantity": 75,
        "price": 2.75
    },
    {
        "flower": "Lilies",
        "quantity": 50,
        "price": 4.25
    }
]

for item in flower_inventory:
    print(
        item["flower"],
        "Quantity:", item["quantity"],
        "Price:", item["price"]
    )


# EXAMPLE 32: Updating Flower Inventory

flower_inventory = [
    {"flower": "Roses", "quantity": 100},
    {"flower": "Tulips", "quantity": 75}
]

flower_inventory[0]["quantity"] -= 25

print("Updated inventory:", flower_inventory)


# EXAMPLE 33: Customer Order with Nested Items
#
# One order can contain
# multiple products.

order = {
    "order_id": "001",
    "customer": "Alex",
    "items": [
        {
            "product": "Rose Bouquet",
            "quantity": 2,
            "price": 75.00
        },
        {
            "product": "Tulip Bouquet",
            "quantity": 1,
            "price": 65.00
        }
    ]
}

print("Order:", order["order_id"])

for item in order["items"]:
    print(item["product"], item["quantity"])


# EXAMPLE 34: Calculating an Order Total

order = {
    "order_id": "001",
    "items": [
        {
            "product": "Rose Bouquet",
            "quantity": 2,
            "price": 75.00
        },
        {
            "product": "Tulip Bouquet",
            "quantity": 1,
            "price": 65.00
        }
    ]
}

total = 0

for item in order["items"]:
    total += item["quantity"] * item["price"]

print(f"Order total: ${total:.2f}")


# EXAMPLE 35: Multiple Customer Orders

orders = [
    {
        "order_id": "001",
        "customer": "Alex",
        "total": 150.00
    },
    {
        "order_id": "002",
        "customer": "Morgan",
        "total": 85.00
    },
    {
        "order_id": "003",
        "customer": "Chris",
        "total": 65.00
    }
]

for order in orders:
    print(
        order["order_id"],
        order["customer"],
        order["total"]
    )


# EXAMPLE 36: Total Revenue from Orders

orders = [
    {"order_id": "001", "total": 150.00},
    {"order_id": "002", "total": 85.00},
    {"order_id": "003", "total": 65.00}
]

revenue = 0

for order in orders:
    revenue += order["total"]

print(f"Total revenue: ${revenue:.2f}")


# EXAMPLE 37: Security Event Records
#
# Each event is represented
# by a dictionary.

security_events = [
    {
        "event_type": "login_success",
        "username": "alex",
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "login_failed",
        "username": "admin",
        "source_ip": "198.51.100.5"
    },
    {
        "event_type": "port_scan",
        "username": "unknown",
        "source_ip": "203.0.113.7"
    }
]

for event in security_events:
    print(
        event["event_type"],
        event["username"],
        event["source_ip"]
    )


# EXAMPLE 38: Filtering Failed Logins

security_events = [
    {
        "event_type": "login_success",
        "username": "alex"
    },
    {
        "event_type": "login_failed",
        "username": "admin"
    },
    {
        "event_type": "login_failed",
        "username": "guest"
    }
]

failed_events = []

for event in security_events:
    if event["event_type"] == "login_failed":
        failed_events.append(event)

print("Failed events:", failed_events)


# EXAMPLE 39: Counting Event Categories

security_events = [
    {"event_type": "login_success"},
    {"event_type": "login_failed"},
    {"event_type": "port_scan"},
    {"event_type": "login_failed"}
]

event_counts = {}

for event in security_events:
    event_type = event["event_type"]

    event_counts[event_type] = (
        event_counts.get(event_type, 0) + 1
    )

print("Event counts:", event_counts)


# EXAMPLE 40: Unique Source IP Addresses
#
# Sets identify unique values.
#
# The original event records
# remain unchanged.

security_events = [
    {"source_ip": "192.0.2.10"},
    {"source_ip": "192.0.2.20"},
    {"source_ip": "192.0.2.10"},
    {"source_ip": "203.0.113.7"}
]

unique_ips = set()

for event in security_events:
    unique_ips.add(event["source_ip"])

print("Unique IPs:", sorted(unique_ips))


# EXAMPLE 41: Grouping Events by Source IP

security_events = [
    {
        "event_type": "login_failed",
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "port_scan",
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "login_success",
        "source_ip": "198.51.100.5"
    }
]

events_by_ip = {}

for event in security_events:
    ip = event["source_ip"]

    if ip not in events_by_ip:
        events_by_ip[ip] = []

    events_by_ip[ip].append(event["event_type"])

print("Grouped events:", events_by_ip)


# EXAMPLE 42: Nested Data in Functions

def display_students(students):
    for student in students:
        print(
            student["name"],
            student["grade"]
        )


student_records = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 85}
]

display_students(student_records)


# EXAMPLE 43: Returning Nested Data

def create_security_event(event_type, username, ip):
    return {
        "event_type": event_type,
        "username": username,
        "source_ip": ip
    }


event = create_security_event(
    "login_failed",
    "admin",
    "192.0.2.10"
)

print("Created event:", event)


# EXAMPLE 44: Safe Nested Access
#
# get() can provide default
# values for missing keys.

event = {
    "event_type": "login_failed",
    "details": {
        "username": "admin"
    }
}

details = event.get("details", {})

username = details.get("username", "unknown")
source_ip = details.get("source_ip", "not recorded")

print("Username:", username)
print("Source IP:", source_ip)


# EXAMPLE 45: Shallow Copy of Nested Data
#
# copy() creates a shallow copy.
#
# Nested mutable objects remain shared.

original = {
    "name": "Alex",
    "courses": ["Python", "Networking"]
}

copied = original.copy()

copied["courses"].append("Cybersecurity")

print("Original:", original)
print("Copied:", copied)


# EXAMPLE 46: Deep Copy of Nested Data
#
# deepcopy() creates independent
# copies of nested mutable objects.

import copy

original = {
    "name": "Alex",
    "courses": ["Python", "Networking"]
}

copied = copy.deepcopy(original)

copied["courses"].append("Cybersecurity")

print("Original:", original)
print("Deep copy:", copied)


# EXAMPLE 47: Nested List Comprehension
#
# This creates a flat list
# from a nested list.

numbers = [
    [1, 2, 3],
    [4, 5, 6]
]

flattened = [
    number
    for row in numbers
    for number in row
]

print("Flattened:", flattened)


# EXAMPLE 48: Filtering Nested Records
#
# A list comprehension can select
# records that meet a condition.

students = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 75},
    {"name": "Chris", "grade": 95}
]

high_grades = [
    student
    for student in students
    if student["grade"] >= 90
]

print("High grades:", high_grades)


# EXAMPLE 49: Nested Security Configuration

security_configuration = {
    "server": {
        "name": "training-server",
        "services": {
            "SSH": 22,
            "HTTPS": 443
        }
    },
    "users": [
        {
            "username": "alex",
            "role": "analyst"
        },
        {
            "username": "morgan",
            "role": "admin"
        }
    ]
}

print(
    "Server:",
    security_configuration["server"]["name"]
)

print(
    "SSH port:",
    security_configuration["server"]["services"]["SSH"]
)

print(
    "First user:",
    security_configuration["users"][0]["username"]
)


# EXAMPLE 50: Basic Security Event Report

security_events = [
    {
        "event_type": "login_success",
        "username": "alex",
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "login_failed",
        "username": "admin",
        "source_ip": "198.51.100.5"
    },
    {
        "event_type": "login_failed",
        "username": "guest",
        "source_ip": "198.51.100.5"
    },
    {
        "event_type": "port_scan",
        "username": "unknown",
        "source_ip": "203.0.113.7"
    }
]

event_counts = {}
unique_ips = set()

for event in security_events:
    event_type = event["event_type"]

    event_counts[event_type] = (
        event_counts.get(event_type, 0) + 1
    )

    unique_ips.add(event["source_ip"])

print("===== SECURITY EVENT REPORT =====")
print("Total events:", len(security_events))
print("Unique source IPs:", len(unique_ips))

for event_type, count in event_counts.items():
    print(event_type, ":", count)

print("Source IP addresses:")

for ip in sorted(unique_ips):
    print(ip)


# WHAT I LEARNED
#
# 1. Nested structures combine collections.
# 2. Lists can contain other lists.
# 3. Dictionaries can contain lists.
# 4. Dictionaries can contain tuples.
# 5. Dictionaries can contain sets.
# 6. Dictionaries can contain dictionaries.
# 7. Lists can contain dictionaries.
# 8. Multiple indexes access nested lists.
# 9. Multiple keys access nested dictionaries.
# 10. Nested loops process nested data.
# 11. Nested records can be modified.
# 12. Nested records can be filtered.
# 13. Nested numeric values can be analyzed.
# 14. Sets identify unique values.
# 15. Dictionaries can group event records.
# 16. Functions can accept nested data.
# 17. Functions can return nested data.
# 18. get() supports safe key access.
# 19. Shallow copies share nested objects.
# 20. Deep copies duplicate nested objects.
# 21. Comprehensions can process nested data.
# 22. Nested data supports security analysis.
