
# ==========================================
# DAY 20 - FUNCTIONS WITH PARAMETERS
# Topic: Passing Information to Functions
# ==========================================

# LESSON NOTES
#
# A function is a reusable block of code.
#
# Functions are defined using def.
#
# Parameters are variable names
# listed in a function definition.
#
# Arguments are actual values
# passed when calling a function.
#
# Example:
#
# def greet(name):
#     print("Hello", name)
#
# greet("Alex")
#
# name is a parameter.
# "Alex" is an argument.
#
# Important concepts:
#
# Positional arguments
# Keyword arguments
# Default parameters
# Multiple parameters
# *args
# **kwargs
# Argument unpacking
# Parameter validation
#
# Functions help reduce repetition
# and organize programs.
#
# Day 21 will explore return
# statements in greater depth.


# EXAMPLE 1: Function Without Parameters

def greet():
    print("Hello, welcome to Python!")


greet()


# EXAMPLE 2: Function with One Parameter

def greet_user(name):
    print("Hello,", name)


greet_user("Alex")


# EXAMPLE 3: Calling with Different Arguments

def greet_student(name):
    print("Welcome,", name)


greet_student("Alex")
greet_student("Morgan")
greet_student("Chris")


# EXAMPLE 4: Two Parameters

def display_student(name, major):
    print("Name:", name)
    print("Major:", major)


display_student("Alex", "Cyber Defense")


# EXAMPLE 5: Three Parameters

def display_profile(name, age, major):
    print("Name:", name)
    print("Age:", age)
    print("Major:", major)


display_profile("Alex", 23, "Cyber Defense")


# EXAMPLE 6: Positional Arguments
#
# Positional arguments are matched
# according to their order.

def display_order(customer, product):
    print("Customer:", customer)
    print("Product:", product)


display_order("Alex", "Rose Bouquet")


# EXAMPLE 7: Argument Order Matters

def subtract_numbers(first, second):
    result = first - second

    print("Difference:", result)


subtract_numbers(20, 5)
subtract_numbers(5, 20)


# EXAMPLE 8: Keyword Arguments
#
# Keyword arguments identify
# parameters by name.

def display_employee(name, department):
    print("Name:", name)
    print("Department:", department)


display_employee(
    department="IT",
    name="Morgan"
)


# EXAMPLE 9: Mixing Positional and Keyword Arguments
#
# Positional arguments must appear
# before keyword arguments.

def display_device(name, status, location):
    print("Device:", name)
    print("Status:", status)
    print("Location:", location)


display_device(
    "Server-01",
    status="Active",
    location="Lab"
)


# EXAMPLE 10: Default Parameters
#
# A default value is used when
# no argument is supplied.

def greet_person(name="Guest"):
    print("Hello,", name)


greet_person()
greet_person("Alex")


# EXAMPLE 11: Multiple Default Parameters

def display_account(
    username,
    role="employee",
    active=True
):
    print("Username:", username)
    print("Role:", role)
    print("Active:", active)


display_account("alex")
display_account("morgan", "analyst")
display_account("chris", "admin", False)


# EXAMPLE 12: Overriding Default Values

def display_service(service, port=22):
    print("Service:", service)
    print("Port:", port)


display_service("SSH")
display_service("Training SSH", 2222)


# EXAMPLE 13: Required and Optional Parameters
#
# Required positional parameters
# must precede parameters with
# default values.

def display_product(name, price, category="Flowers"):
    print("Product:", name)
    print("Price:", price)
    print("Category:", category)


display_product("Rose Bouquet", 75.00)


# EXAMPLE 14: Function with Numeric Parameters

def add_numbers(a, b):
    total = a + b

    print("Total:", total)


add_numbers(10, 20)


# EXAMPLE 15: Function with String Parameters

def display_full_name(first_name, last_name):
    full_name = first_name + " " + last_name

    print("Full name:", full_name)


display_full_name("Alex", "Morgan")


# EXAMPLE 16: Function with Boolean Parameters

def display_account_status(username, active):
    if active:
        print(username, "is active.")
    else:
        print(username, "is inactive.")


display_account_status("alex", True)
display_account_status("guest", False)


# EXAMPLE 17: Passing a List

def display_tools(tools):
    for tool in tools:
        print("Tool:", tool)


security_tools = [
    "Wireshark",
    "Nmap",
    "Python"
]

display_tools(security_tools)


# EXAMPLE 18: Passing a Tuple

def display_ports(ports):
    for port in ports:
        print("Port:", port)


network_ports = (22, 80, 443, 3389)

display_ports(network_ports)


# EXAMPLE 19: Passing a Set

def display_unique_tools(tools):
    for tool in sorted(tools):
        print("Tool:", tool)


tools = {
    "Wireshark",
    "Nmap",
    "Python"
}

display_unique_tools(tools)


# EXAMPLE 20: Passing a Dictionary

def display_user(user):
    for key, value in user.items():
        print(f"{key}: {value}")


user_profile = {
    "username": "alex",
    "role": "analyst",
    "active": True
}

display_user(user_profile)


# EXAMPLE 21: Passing Nested Data

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


# EXAMPLE 22: Functions with Conditional Logic

def check_grade(name, grade):
    if grade >= 70:
        print(name, "passed.")
    else:
        print(name, "did not pass.")


check_grade("Alex", 90)
check_grade("Morgan", 65)


# EXAMPLE 23: Functions with Loops

def print_numbers(start, stop):
    for number in range(start, stop + 1):
        print(number)


print_numbers(1, 5)


# EXAMPLE 24: Function Calling Another Function

def greet_user(name):
    print("Hello,", name)


def welcome_student(name, major):
    greet_user(name)
    print("Major:", major)


welcome_student("Alex", "Cyber Defense")


# EXAMPLE 25: Local Parameters
#
# Parameters are local names
# within a function.
#
# The argument's value is supplied
# when the function is called.

def display_message(message):
    print("Message:", message)


display_message("Python functions are reusable.")


# EXAMPLE 26: Mutable List Arguments
#
# A function can modify a list
# passed as an argument.
#
# The caller sees the modification.

def add_tool(tools, new_tool):
    tools.append(new_tool)


security_tools = ["Wireshark", "Nmap"]

add_tool(security_tools, "Python")

print("Updated tools:", security_tools)


# EXAMPLE 27: Avoiding Unwanted List Changes
#
# Copy the list before modifying it.

def display_with_new_tool(tools, new_tool):
    updated_tools = tools.copy()

    updated_tools.append(new_tool)

    print("Updated copy:", updated_tools)


security_tools = ["Wireshark", "Nmap"]

display_with_new_tool(
    security_tools,
    "Python"
)

print("Original tools:", security_tools)


# EXAMPLE 28: Immutable Arguments
#
# Integers cannot be modified in place.
#
# Reassigning a parameter does not
# change the caller's variable.

def increase_number(number):
    number += 1

    print("Inside function:", number)


value = 10

increase_number(value)

print("Outside function:", value)


# EXAMPLE 29: *args
#
# *args collects additional
# positional arguments into a tuple.

def display_numbers(*numbers):
    print("Numbers:", numbers)


display_numbers(10, 20, 30, 40)


# EXAMPLE 30: Summing *args

def add_multiple_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    print("Total:", total)


add_multiple_numbers(10, 20, 30, 40)


# EXAMPLE 31: Required Parameter with *args

def display_event_types(category, *events):
    print("Category:", category)

    for event in events:
        print("Event:", event)


display_event_types(
    "Authentication",
    "login_success",
    "login_failed"
)


# EXAMPLE 32: **kwargs
#
# **kwargs collects extra
# keyword arguments into
# a dictionary.

def display_information(**information):
    for key, value in information.items():
        print(key, ":", value)


display_information(
    name="Alex",
    age=23,
    major="Cyber Defense"
)


# EXAMPLE 33: Required Parameter with **kwargs

def display_security_event(event_type, **details):
    print("Event type:", event_type)

    for key, value in details.items():
        print(key, ":", value)


display_security_event(
    "login_failed",
    username="admin",
    source_ip="192.0.2.10"
)


# EXAMPLE 34: Combining *args and **kwargs
#
# *args captures additional
# positional arguments.
#
# **kwargs captures additional
# keyword arguments.

def display_report(title, *items, **details):
    print("Report:", title)

    for item in items:
        print("Item:", item)

    for key, value in details.items():
        print(key, ":", value)


display_report(
    "Security Summary",
    "login_failed",
    "port_scan",
    analyst="Alex",
    status="Review"
)


# EXAMPLE 35: Unpacking a List
#
# * unpacks an iterable into
# positional arguments.

def display_coordinates(x, y):
    print("X:", x)
    print("Y:", y)


coordinates = [10, 20]

display_coordinates(*coordinates)


# EXAMPLE 36: Unpacking a Tuple

def display_service(service, port):
    print("Service:", service)
    print("Port:", port)


service_details = ("SSH", 22)

display_service(*service_details)


# EXAMPLE 37: Unpacking a Dictionary
#
# ** unpacks dictionary entries
# into keyword arguments.
#
# Keys must match parameter names.

def display_user_profile(username, role):
    print("Username:", username)
    print("Role:", role)


profile = {
    "username": "alex",
    "role": "analyst"
}

display_user_profile(**profile)


# EXAMPLE 38: Keyword-Only Parameters
#
# Parameters after * must be
# supplied by keyword.

def display_connection(service, *, port):
    print("Service:", service)
    print("Port:", port)


display_connection("SSH", port=22)


# EXAMPLE 39: Positional-Only Parameters
#
# Parameters before / must
# be supplied positionally.

def multiply_numbers(a, b, /):
    print("Product:", a * b)


multiply_numbers(5, 4)


# EXAMPLE 40: Parameter Type Hints
#
# Type hints describe expected types.
#
# Python does not automatically
# enforce them at runtime.

def greet_analyst(name: str, shift: str) -> None:
    print(f"{name} works the {shift} shift.")


greet_analyst("Alex", "morning")


# EXAMPLE 41: Validating Parameters

def display_port(port):
    if not isinstance(port, int) or isinstance(port, bool):
        print("Port must be an integer.")
    elif port < 1 or port > 65535:
        print("Port must be between 1 and 65535.")
    else:
        print("Valid port:", port)


display_port(22)
display_port(70000)
display_port("SSH")


# EXAMPLE 42: Flower Product Function

def display_bouquet(name, price, quantity=1):
    total = price * quantity

    print("Bouquet:", name)
    print("Quantity:", quantity)
    print(f"Total: ${total:.2f}")


display_bouquet("Rose Bouquet", 75.00)
display_bouquet("Tulip Bouquet", 65.00, 2)


# EXAMPLE 43: Flower Inventory Function

def display_inventory(flower, quantity, price):
    print("Flower:", flower)
    print("Quantity:", quantity)
    print(f"Unit price: ${price:.2f}")


display_inventory("Roses", 100, 3.50)


# EXAMPLE 44: Customer Order Function

def display_order(
    order_id,
    customer,
    product,
    quantity,
    unit_price
):
    total = quantity * unit_price

    print("===== CUSTOMER ORDER =====")
    print("Order ID:", order_id)
    print("Customer:", customer)
    print("Product:", product)
    print("Quantity:", quantity)
    print(f"Total: ${total:.2f}")


display_order(
    "001",
    "Alex",
    "Rose Bouquet",
    2,
    75.00
)


# EXAMPLE 45: Security Event Function

def log_security_event(event_type, username, source_ip):
    print("===== SECURITY EVENT =====")
    print("Event:", event_type)
    print("Username:", username)
    print("Source IP:", source_ip)


log_security_event(
    "login_failed",
    "admin",
    "192.0.2.10"
)


# EXAMPLE 46: Counting Events with a Parameter

def count_failed_logins(events):
    count = 0

    for event in events:
        if event == "login_failed":
            count += 1

    print("Failed logins:", count)


security_events = [
    "login_success",
    "login_failed",
    "login_failed",
    "port_scan"
]

count_failed_logins(security_events)


# EXAMPLE 47: Custom Event Filtering

def display_matching_events(events, target_type):
    for event in events:
        if event["event_type"] == target_type:
            print(event)


security_events = [
    {
        "event_type": "login_failed",
        "username": "admin"
    },
    {
        "event_type": "login_success",
        "username": "alex"
    },
    {
        "event_type": "login_failed",
        "username": "guest"
    }
]

display_matching_events(
    security_events,
    "login_failed"
)


# EXAMPLE 48: Default Security Report Parameters

def display_security_summary(
    events,
    title="Security Event Summary"
):
    print("=====", title, "=====")

    for event in events:
        print("Event:", event)


events = [
    "login_success",
    "login_failed",
    "port_scan"
]

display_security_summary(events)

display_security_summary(
    events,
    title="Daily Training Report"
)


# EXAMPLE 49: Mutable Default Argument Warning
#
# Avoid using mutable objects
# such as [] or {} as defaults.
#
# Mutable defaults are created
# when the function is defined,
# not every time it is called.
#
# Use None when a new list
# should be created per call.

def add_record(record, records=None):
    if records is None:
        records = []

    records.append(record)

    print("Records:", records)


add_record("login_failed")
add_record("port_scan")


# EXAMPLE 50: Security Event Report with Parameters

def display_event_counts(events):
    event_counts = {}

    for event in events:
        event_type = event["event_type"]

        event_counts[event_type] = (
            event_counts.get(event_type, 0) + 1
        )

    print("Event categories:")

    for event_type, count in event_counts.items():
        print(f"{event_type}: {count}")


def display_unique_ips(events):
    unique_ips = set()

    for event in events:
        unique_ips.add(event["source_ip"])

    print("Unique source IPs:", len(unique_ips))

    for ip in sorted(unique_ips):
        print("IP:", ip)


def display_full_report(
    events,
    title="Security Monitoring Report"
):
    print("=====", title, "=====")
    print("Total events:", len(events))

    display_event_counts(events)
    display_unique_ips(events)


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

display_full_report(security_events)


# WHAT I LEARNED
#
# 1. Functions are reusable blocks of code.
# 2. Parameters appear in definitions.
# 3. Arguments are supplied during calls.
# 4. Positional arguments follow order.
# 5. Keyword arguments use parameter names.
# 6. Default parameters provide fallback values.
# 7. Functions can accept multiple arguments.
# 8. Functions can accept strings and numbers.
# 9. Functions can accept Booleans.
# 10. Functions can accept lists and tuples.
# 11. Functions can accept sets and dictionaries.
# 12. Functions can process nested data.
# 13. Functions can contain conditionals.
# 14. Functions can contain loops.
# 15. Functions can call other functions.
# 16. Mutable arguments can be modified.
# 17. Copying helps avoid unwanted changes.
# 18. *args collects positional arguments.
# 19. **kwargs collects keyword arguments.
# 20. * unpacks positional arguments.
# 21. ** unpacks keyword arguments.
# 22. Parameters can be keyword-only.
# 23. Parameters can be positional-only.
# 24. Type hints document expected types.
# 25. Parameters should be validated.
# 26. Mutable default arguments need care.
# 27. Functions help organize business logic.
# 28. Functions support security reporting.
