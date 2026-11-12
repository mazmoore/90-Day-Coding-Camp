
# ==========================================
# DAY 21 - RETURN STATEMENTS
# Topic: Function Outputs and Return Values
# ==========================================

# LESSON NOTES
#
# A function can receive information
# through parameters and arguments.
#
# A function can send information
# back to its caller using return.
#
# Example:
#
# def add_numbers(a, b):
#     return a + b
#
# result = add_numbers(10, 20)
#
# print(result)
#
# Important concepts:
#
# return
# Return values
# print() versus return
# Returning multiple values
# Returning collections
# Early returns
# Conditional returns
# Returning None
# Function composition
# Reusable calculations
#
# return immediately exits
# the current function.
#
# A function without an explicit
# return statement returns None.
#
# Functions that return results
# can be reused in calculations,
# conditions, reports, and programs.
#
# Day 22 will explore variable
# scope in greater depth.


# EXAMPLE 1: Basic Return Statement

def greet():
    return "Hello, Python!"


message = greet()

print("Message:", message)


# EXAMPLE 2: Returning a Number

def get_number():
    return 25


number = get_number()

print("Number:", number)


# EXAMPLE 3: Returning a Calculation

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Total:", result)


# EXAMPLE 4: print() Versus return
#
# print() displays information.
#
# return sends a value back
# to the function caller.

def print_total(a, b):
    print("Printed total:", a + b)


def return_total(a, b):
    return a + b


printed_result = print_total(10, 20)

returned_result = return_total(10, 20)

print("Printed function returned:", printed_result)
print("Returned function value:", returned_result)


# EXAMPLE 5: Storing a Returned Value

def multiply_numbers(a, b):
    return a * b


product = multiply_numbers(5, 4)

print("Product:", product)


# EXAMPLE 6: Using a Return Value in Math

def calculate_tax(amount, rate):
    return amount * rate


tax = calculate_tax(100, 0.08)

total = 100 + tax

print("Tax:", tax)
print("Total:", total)


# EXAMPLE 7: Returning a String

def create_greeting(name):
    return f"Hello, {name}!"


greeting = create_greeting("Alex")

print(greeting)


# EXAMPLE 8: Returning a Boolean

def is_adult(age):
    return age >= 18


result = is_adult(23)

print("Adult:", result)


# EXAMPLE 9: Conditional Return Values

def check_grade(grade):
    if grade >= 70:
        return "Pass"
    else:
        return "Fail"


print("Grade status:", check_grade(90))
print("Grade status:", check_grade(65))


# EXAMPLE 10: Early Return
#
# return exits the function
# immediately when executed.

def check_number(number):
    if number < 0:
        return "Negative number"

    return "Zero or positive number"


print(check_number(-5))
print(check_number(10))


# EXAMPLE 11: Multiple Return Paths

def classify_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


print("Letter grade:", classify_grade(88))


# EXAMPLE 12: Returning None
#
# A function without return
# automatically returns None.

def display_message():
    print("Welcome to Day 21!")


result = display_message()

print("Return value:", result)


# EXAMPLE 13: Explicitly Returning None

def find_student(name):
    students = ["Alex", "Morgan", "Chris"]

    if name in students:
        return name

    return None


result = find_student("Taylor")

print("Search result:", result)


# EXAMPLE 14: Checking for None
#
# Use is None or is not None
# to check for the None object.

def find_tool(name):
    tools = ["Wireshark", "Nmap", "Python"]

    if name in tools:
        return name

    return None


result = find_tool("Nmap")

if result is not None:
    print("Tool found:", result)
else:
    print("Tool not found.")


# EXAMPLE 15: Returning Multiple Values
#
# Comma-separated return values
# are packaged into a tuple.

def get_coordinates():
    return 10, 20


coordinates = get_coordinates()

print("Coordinates:", coordinates)
print("Type:", type(coordinates))


# EXAMPLE 16: Unpacking Returned Values

def calculate_stats(a, b):
    total = a + b
    difference = a - b

    return total, difference


total, difference = calculate_stats(20, 5)

print("Total:", total)
print("Difference:", difference)


# EXAMPLE 17: Returning Three Values

def calculate_number_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


values = [10, 20, 30, 40, 50]

minimum, maximum, average = calculate_number_stats(
    values
)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)


# EXAMPLE 18: Returning a List

def get_security_tools():
    return [
        "Wireshark",
        "Nmap",
        "Python"
    ]


tools = get_security_tools()

print("Tools:", tools)


# EXAMPLE 19: Returning a Tuple

def get_network_service():
    return ("SSH", 22, "TCP")


service = get_network_service()

print("Service:", service)


# EXAMPLE 20: Returning a Set

def get_unique_events(events):
    return set(events)


events = [
    "login_success",
    "login_failed",
    "login_failed",
    "port_scan"
]

unique_events = get_unique_events(events)

print("Unique events:", sorted(unique_events))


# EXAMPLE 21: Returning a Dictionary

def create_user(username, role):
    return {
        "username": username,
        "role": role,
        "active": True
    }


user = create_user("alex", "analyst")

print("User:", user)


# EXAMPLE 22: Returning Nested Data

def create_student(name, major, courses):
    return {
        "name": name,
        "major": major,
        "courses": courses.copy()
    }


student = create_student(
    "Alex",
    "Cyber Defense",
    ["Python", "Networking"]
)

print("Student:", student)


# EXAMPLE 23: Returning a Filtered List

def filter_passing_grades(grades):
    passing = []

    for grade in grades:
        if grade >= 70:
            passing.append(grade)

    return passing


grades = [90, 65, 85, 55, 95]

passing_grades = filter_passing_grades(grades)

print("Passing grades:", passing_grades)


# EXAMPLE 24: Returning a Count

def count_failed_logins(events):
    count = 0

    for event in events:
        if event == "login_failed":
            count += 1

    return count


events = [
    "login_success",
    "login_failed",
    "login_failed",
    "port_scan"
]

failed_count = count_failed_logins(events)

print("Failed logins:", failed_count)


# EXAMPLE 25: Returning a Frequency Dictionary

def count_event_types(events):
    counts = {}

    for event in events:
        counts[event] = counts.get(event, 0) + 1

    return counts


events = [
    "login_success",
    "login_failed",
    "login_failed",
    "port_scan"
]

event_counts = count_event_types(events)

print("Event counts:", event_counts)


# EXAMPLE 26: Returning the Maximum Value

def find_highest(numbers):
    if not numbers:
        return None

    highest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number

    return highest


numbers = [12, 45, 7, 89, 34]

print("Highest:", find_highest(numbers))


# EXAMPLE 27: Returning the Minimum Value

def find_lowest(numbers):
    if not numbers:
        return None

    lowest = numbers[0]

    for number in numbers:
        if number < lowest:
            lowest = number

    return lowest


numbers = [12, 45, 7, 89, 34]

print("Lowest:", find_lowest(numbers))


# EXAMPLE 28: Returning an Average
#
# Empty collections need
# special handling to avoid
# division by zero.

def calculate_average(numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


grades = [90, 85, 95, 88]

average = calculate_average(grades)

print("Average:", average)


# EXAMPLE 29: Returning a Search Result

def find_record(records, target_name):
    for record in records:
        if record["name"] == target_name:
            return record

    return None


students = [
    {"name": "Alex", "grade": 90},
    {"name": "Morgan", "grade": 85}
]

result = find_record(students, "Morgan")

print("Found record:", result)


# EXAMPLE 30: Returning a Boolean Search Result

def contains_failed_login(events):
    for event in events:
        if event == "login_failed":
            return True

    return False


events = [
    "login_success",
    "port_scan",
    "login_failed"
]

print(
    "Failed login present:",
    contains_failed_login(events)
)


# EXAMPLE 31: Function Composition
#
# A returned value can be
# passed into another function.

def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_total(subtotal, tax_rate):
    return subtotal * (1 + tax_rate)


subtotal = calculate_subtotal(75.00, 2)

total = calculate_total(subtotal, 0.08)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Total: ${total:.2f}")


# EXAMPLE 32: Calling a Function Inside Another

def calculate_square(number):
    return number ** 2


def calculate_sum_of_squares(a, b):
    return calculate_square(a) + calculate_square(b)


result = calculate_sum_of_squares(3, 4)

print("Sum of squares:", result)


# EXAMPLE 33: Returning a Formatted String

def format_currency(amount):
    return f"${amount:.2f}"


price = format_currency(75)

print("Formatted price:", price)


# EXAMPLE 34: Returning a Validation Result

def is_valid_port(port):
    if isinstance(port, bool):
        return False

    if not isinstance(port, int):
        return False

    return 1 <= port <= 65535


print("Port 22:", is_valid_port(22))
print("Port 70000:", is_valid_port(70000))
print("Port True:", is_valid_port(True))


# EXAMPLE 35: Returning a Status Message

def check_inventory(quantity):
    if quantity <= 0:
        return "Out of stock"

    if quantity < 10:
        return "Low stock"

    return "In stock"


print(check_inventory(0))
print(check_inventory(5))
print(check_inventory(100))


# EXAMPLE 36: Returning a Modified Copy
#
# The function creates a copy
# rather than changing the
# caller's original list.

def add_security_tool(tools, new_tool):
    updated = tools.copy()

    updated.append(new_tool)

    return updated


original_tools = ["Wireshark", "Nmap"]

updated_tools = add_security_tool(
    original_tools,
    "Python"
)

print("Original:", original_tools)
print("Updated:", updated_tools)


# EXAMPLE 37: Returning a New Dictionary

def update_user_role(user, new_role):
    updated = user.copy()

    updated["role"] = new_role

    return updated


original_user = {
    "username": "alex",
    "role": "employee"
}

updated_user = update_user_role(
    original_user,
    "analyst"
)

print("Original:", original_user)
print("Updated:", updated_user)


# EXAMPLE 38: Returning a List Comprehension

def get_even_numbers(numbers):
    return [
        number
        for number in numbers
        if number % 2 == 0
    ]


numbers = [1, 2, 3, 4, 5, 6]

print("Even numbers:", get_even_numbers(numbers))


# EXAMPLE 39: Returning a Dictionary Comprehension

def create_square_dictionary(numbers):
    return {
        number: number ** 2
        for number in numbers
    }


numbers = [1, 2, 3, 4, 5]

print(
    "Squares:",
    create_square_dictionary(numbers)
)


# EXAMPLE 40: Returning a Set Comprehension

def get_unique_usernames(records):
    return {
        record["username"]
        for record in records
    }


records = [
    {"username": "alex"},
    {"username": "morgan"},
    {"username": "alex"}
]

print(
    "Unique usernames:",
    sorted(get_unique_usernames(records))
)


# EXAMPLE 41: Flower Bouquet Subtotal

def calculate_bouquet_subtotal(price, quantity):
    return price * quantity


subtotal = calculate_bouquet_subtotal(
    75.00,
    3
)

print(f"Bouquet subtotal: ${subtotal:.2f}")


# EXAMPLE 42: Flower Inventory Value

def calculate_inventory_value(quantity, unit_cost):
    return quantity * unit_cost


inventory_value = calculate_inventory_value(
    100,
    3.50
)

print(f"Inventory value: ${inventory_value:.2f}")


# EXAMPLE 43: Customer Order Total

def calculate_order_total(items):
    total = 0

    for item in items:
        total += (
            item["quantity"] * item["price"]
        )

    return total


order_items = [
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

order_total = calculate_order_total(order_items)

print(f"Order total: ${order_total:.2f}")


# EXAMPLE 44: Returning a Customer Receipt

def create_receipt(order_id, customer, total):
    return (
        f"Order: {order_id}\n"
        f"Customer: {customer}\n"
        f"Total: ${total:.2f}"
    )


receipt = create_receipt(
    "001",
    "Alex",
    150.00
)

print(receipt)


# EXAMPLE 45: Returning a Security Event

def create_security_event(
    event_type,
    username,
    source_ip
):
    return {
        "event_type": event_type,
        "username": username,
        "source_ip": source_ip
    }


event = create_security_event(
    "login_failed",
    "admin",
    "192.0.2.10"
)

print("Security event:", event)


# EXAMPLE 46: Filtering Security Events

def filter_security_events(events, target_type):
    matching_events = []

    for event in events:
        if event["event_type"] == target_type:
            matching_events.append(event.copy())

    return matching_events


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

failed_events = filter_security_events(
    security_events,
    "login_failed"
)

print("Failed events:", failed_events)


# EXAMPLE 47: Counting Unique Source IPs

def count_unique_ips(events):
    unique_ips = set()

    for event in events:
        unique_ips.add(event["source_ip"])

    return len(unique_ips)


security_events = [
    {"source_ip": "192.0.2.10"},
    {"source_ip": "192.0.2.20"},
    {"source_ip": "192.0.2.10"}
]

unique_count = count_unique_ips(security_events)

print("Unique source IPs:", unique_count)


# EXAMPLE 48: Returning Grouped Security Events

def group_events_by_ip(events):
    grouped = {}

    for event in events:
        ip = event["source_ip"]

        if ip not in grouped:
            grouped[ip] = []

        grouped[ip].append(event["event_type"])

    return grouped


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

grouped_events = group_events_by_ip(
    security_events
)

print("Grouped events:", grouped_events)


# EXAMPLE 49: Returning Multiple Report Results

def analyze_security_events(events):
    event_counts = {}
    unique_ips = set()

    for event in events:
        event_type = event["event_type"]

        event_counts[event_type] = (
            event_counts.get(event_type, 0) + 1
        )

        unique_ips.add(event["source_ip"])

    return event_counts, unique_ips


security_events = [
    {
        "event_type": "login_failed",
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "login_failed",
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "port_scan",
        "source_ip": "203.0.113.7"
    }
]

counts, unique_ips = analyze_security_events(
    security_events
)

print("Event counts:", counts)
print("Unique IPs:", sorted(unique_ips))


# EXAMPLE 50: Reusable Security Report
#
# Separate functions calculate
# and return information.
#
# Another function uses those
# results to display a report.

def count_event_categories(events):
    counts = {}

    for event in events:
        event_type = event["event_type"]

        counts[event_type] = (
            counts.get(event_type, 0) + 1
        )

    return counts


def find_unique_ips(events):
    return {
        event["source_ip"]
        for event in events
    }


def find_failed_logins(events):
    return [
        event.copy()
        for event in events
        if event["event_type"] == "login_failed"
    ]


def create_report_data(events):
    return {
        "total_events": len(events),
        "event_counts": count_event_categories(events),
        "unique_ips": find_unique_ips(events),
        "failed_logins": find_failed_logins(events)
    }


def display_report(report):
    print("===== SECURITY EVENT REPORT =====")
    print("Total events:", report["total_events"])

    print(
        "Unique IP addresses:",
        len(report["unique_ips"])
    )

    print(
        "Failed logins:",
        len(report["failed_logins"])
    )

    print("Event categories:")

    for event_type, count in report["event_counts"].items():
        print(f"{event_type}: {count}")

    print("Source IP addresses:")

    for ip in sorted(report["unique_ips"]):
        print(ip)


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

report_data = create_report_data(
    security_events
)

display_report(report_data)


# WHAT I LEARNED
#
# 1. return sends values to a caller.
# 2. print() displays information.
# 3. print() does not return its text.
# 4. Returned values can be stored.
# 5. Returned values can be reused.
# 6. Functions can return numbers.
# 7. Functions can return strings.
# 8. Functions can return Booleans.
# 9. Functions can return None.
# 10. return immediately exits a function.
# 11. Functions can have multiple return paths.
# 12. Multiple return values form a tuple.
# 13. Returned tuples can be unpacked.
# 14. Functions can return lists.
# 15. Functions can return tuples.
# 16. Functions can return sets.
# 17. Functions can return dictionaries.
# 18. Functions can return nested data.
# 19. Functions can filter collections.
# 20. Functions can return counts.
# 21. Functions can return search results.
# 22. Functions can call other functions.
# 23. Functions can return validation results.
# 24. Functions can return formatted strings.
# 25. Copying can preserve original data.
# 26. Comprehensions can produce results.
# 27. Functions support business calculations.
# 28. Functions support security analysis.
# 29. Functions can build reusable reports.
