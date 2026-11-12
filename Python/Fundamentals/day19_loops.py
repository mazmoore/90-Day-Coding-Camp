
# ==========================================
# DAY 19 - LOOP PRACTICE
# Topic: Loops and Iteration
# ==========================================

# LESSON NOTES
#
# Loops allow programs to repeat
# instructions automatically.
#
# Python has two main loop types:
#
# 1. for loops
# 2. while loops
#
# A for loop iterates through
# elements of an iterable.
#
# A while loop repeats while
# its condition remains True.
#
# Loops can process:
#
# Strings
# Lists
# Tuples
# Dictionaries
# Sets
# Ranges
# Nested collections
#
# Important loop concepts:
#
# range()
# enumerate()
# zip()
# break
# continue
# pass
# else
#
# Nested loops place one loop
# inside another.
#
# Loops are useful for:
#
# Data processing
# Counting records
# Searching collections
# Filtering information
# Generating reports
# Analyzing security events


# EXAMPLE 1: Basic for Loop

for number in range(1, 6):
    print("Number:", number)


# EXAMPLE 2: Understanding range()
#
# range(start, stop, step)
#
# The stop value is excluded.

for number in range(0, 11, 2):
    print("Even number:", number)


# EXAMPLE 3: Counting Backward

for number in range(5, 0, -1):
    print("Countdown:", number)

print("Countdown complete.")


# EXAMPLE 4: Iterating Through a String

language = "Python"

for character in language:
    print("Character:", character)


# EXAMPLE 5: Iterating Through a List

languages = ["Python", "C", "C++"]

for language in languages:
    print("Language:", language)


# EXAMPLE 6: Iterating Through a Tuple

ports = (22, 80, 443, 3389)

for port in ports:
    print("Port:", port)


# EXAMPLE 7: Iterating Through a Set
#
# Sets have no guaranteed
# iteration order.

tools = {"Wireshark", "Nmap", "Python"}

for tool in tools:
    print("Tool:", tool)


# EXAMPLE 8: Iterating Through a Dictionary
#
# Iterating directly through
# a dictionary produces keys.

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

for key in student:
    print("Key:", key)


# EXAMPLE 9: Dictionary Values

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

for value in student.values():
    print("Value:", value)


# EXAMPLE 10: Dictionary Items

student = {
    "name": "Alex",
    "age": 23,
    "major": "Cyber Defense"
}

for key, value in student.items():
    print(f"{key}: {value}")


# EXAMPLE 11: Using enumerate()
#
# enumerate() provides an index
# and an element during iteration.

tools = ["Wireshark", "Nmap", "Python"]

for index, tool in enumerate(tools):
    print(index, tool)


# EXAMPLE 12: enumerate() Starting at One

tools = ["Wireshark", "Nmap", "Python"]

for number, tool in enumerate(tools, start=1):
    print(f"{number}. {tool}")


# EXAMPLE 13: Using zip()
#
# zip() pairs elements from
# multiple iterables.
#
# By default, iteration stops
# when the shortest input ends.

names = ["Alex", "Morgan", "Chris"]
grades = [90, 85, 95]

for name, grade in zip(names, grades):
    print(name, grade)


# EXAMPLE 14: Using zip() with Three Lists

names = ["Alex", "Morgan"]
roles = ["analyst", "admin"]
active = [True, False]

for name, role, status in zip(
    names,
    roles,
    active
):
    print(name, role, status)


# EXAMPLE 15: Basic while Loop
#
# The condition is checked
# before each iteration.

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# EXAMPLE 16: Counting Backward with while

count = 5

while count >= 1:
    print("Countdown:", count)
    count -= 1


# EXAMPLE 17: Processing a List with while

tasks = [
    "Review logs",
    "Check alerts",
    "Write report"
]

while tasks:
    current_task = tasks.pop(0)

    print("Processing:", current_task)

print("All tasks processed.")


# EXAMPLE 18: Using break
#
# break immediately exits
# the nearest enclosing loop.

for number in range(1, 11):
    if number == 6:
        break

    print("Number:", number)


# EXAMPLE 19: Searching with break

tools = [
    "Wireshark",
    "Nmap",
    "Python",
    "Linux"
]

for tool in tools:
    if tool == "Python":
        print("Python found.")
        break


# EXAMPLE 20: Using continue
#
# continue skips the rest
# of the current iteration.

for number in range(1, 11):
    if number == 5:
        continue

    print("Number:", number)


# EXAMPLE 21: Skipping Unwanted Values

events = [
    "login_success",
    "login_failed",
    "port_scan",
    "login_failed"
]

for event in events:
    if event == "login_success":
        continue

    print("Review event:", event)


# EXAMPLE 22: Using pass
#
# pass is a placeholder.
#
# It performs no operation.

for number in range(1, 6):
    if number == 3:
        pass

    print("Number:", number)


# EXAMPLE 23: for-else
#
# The else block runs if
# the loop finishes without
# encountering break.

tools = ["Wireshark", "Nmap", "Python"]

for tool in tools:
    if tool == "Java":
        print("Java found.")
        break
else:
    print("Java was not found.")


# EXAMPLE 24: while-else
#
# The else block runs when
# the loop ends normally.
#
# It does not run if break
# exits the loop.

count = 1

while count <= 3:
    print("Count:", count)
    count += 1
else:
    print("Loop completed normally.")


# EXAMPLE 25: Nested for Loops
#
# The inner loop completes
# for each outer-loop iteration.

for row in range(1, 4):
    for column in range(1, 4):
        print("Row:", row, "Column:", column)


# EXAMPLE 26: Multiplication Table

for row in range(1, 6):
    for column in range(1, 6):
        result = row * column

        print(
            f"{row} x {column} = {result}"
        )


# EXAMPLE 27: Nested List Iteration

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for number in row:
        print("Value:", number)


# EXAMPLE 28: Nested Dictionary Iteration

students = {
    "student_1": {
        "name": "Alex",
        "grade": 90
    },
    "student_2": {
        "name": "Morgan",
        "grade": 85
    }
}

for student_id, details in students.items():
    print("Student ID:", student_id)

    for key, value in details.items():
        print(key, ":", value)


# EXAMPLE 29: Counting with a Loop

numbers = [10, 20, 30, 40, 50]

count = 0

for number in numbers:
    count += 1

print("Total elements:", count)


# EXAMPLE 30: Calculating a Sum

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Total:", total)


# EXAMPLE 31: Calculating an Average

grades = [90, 85, 95, 88, 92]

total = 0

for grade in grades:
    total += grade

average = total / len(grades)

print("Average:", average)


# EXAMPLE 32: Finding a Maximum Value

numbers = [12, 45, 7, 89, 34]

highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number

print("Highest value:", highest)


# EXAMPLE 33: Finding a Minimum Value

numbers = [12, 45, 7, 89, 34]

lowest = numbers[0]

for number in numbers:
    if number < lowest:
        lowest = number

print("Lowest value:", lowest)


# EXAMPLE 34: Filtering with a Loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)


# EXAMPLE 35: Counting Matching Values

events = [
    "login_success",
    "login_failed",
    "login_failed",
    "port_scan",
    "login_failed"
]

failed_count = 0

for event in events:
    if event == "login_failed":
        failed_count += 1

print("Failed logins:", failed_count)


# EXAMPLE 36: Creating a Frequency Dictionary

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

print("Event counts:", event_counts)


# EXAMPLE 37: Collecting Unique Values

source_ips = [
    "192.0.2.10",
    "192.0.2.20",
    "192.0.2.10",
    "203.0.113.7"
]

unique_ips = set()

for ip in source_ips:
    unique_ips.add(ip)

print("Unique IPs:", sorted(unique_ips))


# EXAMPLE 38: Filtering Nested Records

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


# EXAMPLE 39: Grouping Records

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


# EXAMPLE 40: Flower Inventory Report

flower_inventory = {
    "Roses": 100,
    "Tulips": 75,
    "Lilies": 50
}

for flower, quantity in flower_inventory.items():
    print(f"{flower}: {quantity} available")


# EXAMPLE 41: Updating Inventory with a Loop

flower_inventory = {
    "Roses": 100,
    "Tulips": 75,
    "Lilies": 50
}

sales = {
    "Roses": 20,
    "Tulips": 10,
    "Lilies": 5
}

for flower, quantity_sold in sales.items():
    if flower in flower_inventory:
        flower_inventory[flower] -= quantity_sold

print("Updated inventory:", flower_inventory)


# EXAMPLE 42: Customer Order Revenue

orders = [
    {"order_id": "001", "total": 150.00},
    {"order_id": "002", "total": 85.00},
    {"order_id": "003", "total": 65.00}
]

revenue = 0

for order in orders:
    revenue += order["total"]

print(f"Total revenue: ${revenue:.2f}")


# EXAMPLE 43: Looping Through Order Items

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
    subtotal = item["quantity"] * item["price"]

    total += subtotal

    print(
        item["product"],
        f"Subtotal: ${subtotal:.2f}"
    )

print(f"Order total: ${total:.2f}")


# EXAMPLE 44: Using Loops in Functions

def count_failed_logins(events):
    count = 0

    for event in events:
        if event == "login_failed":
            count += 1

    return count


events = [
    "login_success",
    "login_failed",
    "login_failed"
]

result = count_failed_logins(events)

print("Failed logins:", result)


# EXAMPLE 45: Function with Nested Records

def calculate_revenue(orders):
    total = 0

    for order in orders:
        total += order["total"]

    return total


orders = [
    {"total": 75.00},
    {"total": 95.00},
    {"total": 65.00}
]

revenue = calculate_revenue(orders)

print(f"Revenue: ${revenue:.2f}")


# EXAMPLE 46: Loop Input Validation
#
# A while loop can repeat
# until valid input is entered.
#
# This example uses predefined
# values so it runs automatically
# without requiring user input.

attempts = ["abc", "-5", "10"]

valid_number = None

for attempt in attempts:
    if attempt.isdigit():
        valid_number = int(attempt)
        break

print("Valid number:", valid_number)


# EXAMPLE 47: Safe while Loop with Limit
#
# A counter ensures the loop
# cannot run indefinitely.

attempt = 1
maximum_attempts = 3

while attempt <= maximum_attempts:
    print("Attempt:", attempt)

    attempt += 1

print("Maximum attempts reached.")


# EXAMPLE 48: Using any()
#
# any() returns True when
# at least one element is truthy.
#
# A generator expression can
# evaluate a condition for each item.

events = [
    "login_success",
    "port_scan",
    "login_failed"
]

has_failed_login = any(
    event == "login_failed"
    for event in events
)

print("Failed login present:", has_failed_login)


# EXAMPLE 49: Using all()
#
# all() returns True when
# every element is truthy.

grades = [90, 85, 95, 88]

all_passing = all(
    grade >= 70
    for grade in grades
)

print("All passing:", all_passing)


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
    },
    {
        "event_type": "file_access",
        "username": "alex",
        "source_ip": "192.0.2.10"
    }
]

event_counts = {}
unique_ips = set()
failed_events = []

for event in security_events:
    event_type = event["event_type"]

    event_counts[event_type] = (
        event_counts.get(event_type, 0) + 1
    )

    unique_ips.add(event["source_ip"])

    if event_type == "login_failed":
        failed_events.append(event)

print("===== SECURITY EVENT REPORT =====")
print("Total events:", len(security_events))
print("Unique source IPs:", len(unique_ips))
print("Failed logins:", len(failed_events))

print("Event categories:")

for event_type, count in event_counts.items():
    print(f"{event_type}: {count}")

print("Source IP addresses:")

for ip in sorted(unique_ips):
    print(ip)


# WHAT I LEARNED
#
# 1. for loops iterate over collections.
# 2. while loops repeat while True.
# 3. range() generates number sequences.
# 4. enumerate() provides indexes.
# 5. zip() combines iterable elements.
# 6. break exits a loop.
# 7. continue skips an iteration.
# 8. pass is a placeholder.
# 9. Loops can have else blocks.
# 10. Nested loops process nested data.
# 11. Loops can calculate totals.
# 12. Loops can calculate averages.
# 13. Loops can find minimum values.
# 14. Loops can find maximum values.
# 15. Loops can filter collections.
# 16. Loops can count matching values.
# 17. Loops can build dictionaries.
# 18. Loops can collect unique values.
# 19. Loops can group records.
# 20. Loops can process business orders.
# 21. Loops can analyze security events.
# 22. Functions can contain loops.
# 23. Counters help prevent infinite loops.
# 24. any() checks whether a condition
#     is true for at least one item.
# 25. all() checks whether a condition
#     is true for every item.
