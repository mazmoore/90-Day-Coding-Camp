
# ==========================================
# DAY 22 - VARIABLE SCOPE
# Topic: Local, Global, and Enclosing Scope
# ==========================================

# LESSON NOTES
#
# Variable scope determines where
# a name can be accessed in a program.
#
# Python uses the LEGB rule:
#
# L - Local
# E - Enclosing
# G - Global
# B - Built-in
#
# Python searches these scopes
# in that order when resolving
# a variable name.
#
# LOCAL SCOPE:
# Names defined inside a function.
#
# ENCLOSING SCOPE:
# Names in an outer function
# surrounding a nested function.
#
# GLOBAL SCOPE:
# Names defined at module level.
#
# BUILT-IN SCOPE:
# Names provided by Python,
# such as len(), print(), and sum().
#
# Important concepts:
#
# Local variables
# Global variables
# Function parameters
# Variable shadowing
# global
# nonlocal
# Nested functions
# Closures
# Mutable objects
# Avoiding shared state
#
# Good program design usually
# favors parameters and return
# values over changing globals.


# EXAMPLE 1: Local Variable
#
# A local variable is created
# inside a function.

def display_message():
    message = "Hello from a function!"

    print(message)


display_message()


# EXAMPLE 2: Local Variables Are Separate
#
# Each function can have its
# own local variables.

def first_function():
    message = "First function"

    print(message)


def second_function():
    message = "Second function"

    print(message)


first_function()
second_function()


# EXAMPLE 3: Local Variable Lifetime
#
# A local variable normally
# exists during its function call.
#
# Its name is not automatically
# available outside the function.

def create_number():
    number = 25

    print("Inside:", number)


create_number()

# Do not uncomment this line:
#
# print(number)
#
# It would raise NameError.


# EXAMPLE 4: Global Variable
#
# A module-level variable
# has global scope in this module.

language = "Python"


def display_language():
    print("Language:", language)


display_language()


# EXAMPLE 5: Reading a Global Variable
#
# Functions can read global
# variables without global.

application_name = "Coding Camp"


def display_application():
    print("Application:", application_name)


display_application()


# EXAMPLE 6: Local and Global Names
#
# A local name can have
# the same spelling as
# a global name.

status = "Global status"


def display_status():
    status = "Local status"

    print("Inside:", status)


display_status()

print("Outside:", status)


# EXAMPLE 7: Variable Shadowing
#
# A local name shadows a
# global name with the same name.

username = "global_user"


def display_username():
    username = "local_user"

    print("Inside:", username)


display_username()

print("Outside:", username)


# EXAMPLE 8: Function Parameters Are Local

def greet_user(name):
    print("Hello,", name)


greet_user("Alex")


# EXAMPLE 9: Reusing Parameter Names

def display_student(name):
    print("Student:", name)


def display_employee(name):
    print("Employee:", name)


display_student("Alex")
display_employee("Morgan")


# EXAMPLE 10: Returning Local Values
#
# return allows a caller
# to use a function's result.

def calculate_total(a, b):
    total = a + b

    return total


result = calculate_total(10, 20)

print("Returned total:", result)


# EXAMPLE 11: Avoiding Global Variables
#
# Pass information as parameters.

def display_course(course_name):
    print("Course:", course_name)


course = "Python Fundamentals"

display_course(course)


# EXAMPLE 12: Updating a Value with return
#
# Reassignment inside a function
# does not automatically update
# the caller's variable.

def increase_count(count):
    count += 1

    return count


count = 5

count = increase_count(count)

print("Updated count:", count)


# EXAMPLE 13: Using global
#
# global declares that assignments
# to a name refer to the
# module-level variable.

total_visits = 0


def record_visit():
    global total_visits

    total_visits += 1


record_visit()
record_visit()

print("Total visits:", total_visits)


# EXAMPLE 14: global Is Not Always Needed
#
# Reading a global does not
# require a global declaration.

maximum_attempts = 3


def display_attempt_limit():
    print("Maximum attempts:", maximum_attempts)


display_attempt_limit()


# EXAMPLE 15: Global State Warning
#
# Changing global variables can
# make functions harder to test.
#
# Prefer explicit parameters
# and return values when possible.

def add_visit(current_visits):
    return current_visits + 1


visits = 0

visits = add_visit(visits)
visits = add_visit(visits)

print("Visits:", visits)


# EXAMPLE 16: Enclosing Scope
#
# A nested function can read
# names from an outer function.

def outer_function():
    message = "Hello from outer function"

    def inner_function():
        print(message)

    inner_function()


outer_function()


# EXAMPLE 17: Local Versus Enclosing Scope
#
# A local variable in the
# inner function can shadow
# an enclosing variable.

def outer_function():
    message = "Outer message"

    def inner_function():
        message = "Inner message"

        print("Inner:", message)

    inner_function()

    print("Outer:", message)


outer_function()


# EXAMPLE 18: Using nonlocal
#
# nonlocal allows reassignment
# of a variable in an
# enclosing function scope.

def outer_counter():
    count = 0

    def increase():
        nonlocal count

        count += 1

    increase()
    increase()

    print("Enclosing count:", count)


outer_counter()


# EXAMPLE 19: Nested Functions
#
# Functions can be defined
# inside other functions.

def create_report():
    title = "Security Report"

    def display_title():
        print(title)

    display_title()


create_report()


# EXAMPLE 20: Returning a Nested Function
#
# A function can return
# another function.

def create_greeting():
    message = "Welcome!"

    def greet():
        return message

    return greet


greeting_function = create_greeting()

print(greeting_function())


# EXAMPLE 21: Closure
#
# A closure retains access
# to variables from its
# enclosing function.

def create_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)

print("Double:", double(5))
print("Triple:", triple(5))


# EXAMPLE 22: Closure with nonlocal

def create_counter():
    count = 0

    def increment():
        nonlocal count

        count += 1

        return count

    return increment


counter = create_counter()

print(counter())
print(counter())
print(counter())


# EXAMPLE 23: Independent Closures
#
# Each call creates a new
# enclosing environment.

counter_a = create_counter()
counter_b = create_counter()

print("Counter A:", counter_a())
print("Counter A:", counter_a())
print("Counter B:", counter_b())


# EXAMPLE 24: Built-in Scope
#
# Python provides built-in
# names such as len().

tools = ["Wireshark", "Nmap", "Python"]

print("Tool count:", len(tools))


# EXAMPLE 25: Avoid Shadowing Built-ins
#
# Avoid variable names such as:
#
# list
# dict
# set
# str
# sum
# max
# min
#
# Use descriptive names instead.

numbers = [10, 20, 30]

total = sum(numbers)

print("Total:", total)


# EXAMPLE 26: LEGB Resolution
#
# Python searches local,
# enclosing, global, and
# built-in scopes in order.

scope_label = "Global"


def demonstrate_scope():
    scope_label = "Enclosing"

    def inner():
        scope_label = "Local"

        print("Resolved:", scope_label)

    inner()


demonstrate_scope()


# EXAMPLE 27: Global Fallback
#
# If no local or enclosing
# name exists, Python can
# use a global name.

report_title = "Daily Security Summary"


def show_report():
    print(report_title)


show_report()


# EXAMPLE 28: UnboundLocalError Warning
#
# Assigning to a name anywhere
# in a function normally makes
# that name local throughout
# the function.
#
# Reading it before assignment
# can cause UnboundLocalError.
#
# This is intentionally commented
# out to keep the lesson runnable.
#
# score = 10
#
# def broken_example():
#     print(score)
#     score = 20
#
# broken_example()


# EXAMPLE 29: Correcting Scope Problems
#
# Prefer passing a value and
# returning the updated result.

def update_score(score):
    return score + 10


score = 10

score = update_score(score)

print("Updated score:", score)


# EXAMPLE 30: Mutable List Arguments
#
# A function can mutate
# a list passed to it.
#
# This is not the same as
# reassigning a global name.

def add_tool(tools):
    tools.append("Python")


security_tools = ["Wireshark", "Nmap"]

add_tool(security_tools)

print("Tools:", security_tools)


# EXAMPLE 31: Avoiding Mutable Side Effects
#
# Copy a list when the
# original should remain unchanged.

def create_updated_tools(tools):
    updated = tools.copy()

    updated.append("Python")

    return updated


original_tools = ["Wireshark", "Nmap"]

updated_tools = create_updated_tools(
    original_tools
)

print("Original:", original_tools)
print("Updated:", updated_tools)


# EXAMPLE 32: Dictionary Mutation
#
# Mutable dictionaries can
# be changed inside functions.

def update_status(user):
    user["active"] = True


user = {
    "username": "alex",
    "active": False
}

update_status(user)

print("Updated user:", user)


# EXAMPLE 33: Returning a Modified Dictionary
#
# A copy can prevent changes
# to the original dictionary.

def activate_user(user):
    updated = user.copy()

    updated["active"] = True

    return updated


original_user = {
    "username": "alex",
    "active": False
}

new_user = activate_user(original_user)

print("Original:", original_user)
print("New:", new_user)


# EXAMPLE 34: Scope Inside Loops
#
# A for loop does not create
# a separate local scope.
#
# At module level, its variable
# remains a module-level name.

for number in range(1, 4):
    print("Loop number:", number)

print("After loop:", number)


# EXAMPLE 35: Scope Inside if Statements
#
# if blocks do not create
# separate local scopes.

condition = True

if condition:
    message = "Condition was true"

print(message)


# EXAMPLE 36: Comprehension Scope
#
# In Python 3, a list
# comprehension has its
# own iteration-variable scope.

numbers = [1, 2, 3]

squares = [
    value ** 2
    for value in numbers
]

print("Squares:", squares)


# EXAMPLE 37: Function Call State
#
# Local variables are created
# during each function call.

def calculate_square(number):
    result = number ** 2

    return result


print(calculate_square(3))
print(calculate_square(4))
print(calculate_square(5))


# EXAMPLE 38: Recursion and Local Scope
#
# Each recursive call has
# its own local parameters.
#
# A base case stops recursion.

def countdown(number):
    if number <= 0:
        return

    print("Countdown:", number)

    countdown(number - 1)


countdown(3)


# EXAMPLE 39: Using Constants
#
# Uppercase names are a
# naming convention for constants.
#
# Python does not enforce
# their immutability.

MAX_LOGIN_ATTEMPTS = 3


def display_login_policy():
    print("Maximum attempts:", MAX_LOGIN_ATTEMPTS)


display_login_policy()


# EXAMPLE 40: Configuration Parameters
#
# Passing configuration values
# avoids unnecessary global state.

def display_server(name, port):
    print("Server:", name)
    print("Port:", port)


server_name = "training-server"
server_port = 2222

display_server(server_name, server_port)


# EXAMPLE 41: Flower Inventory Scope

def calculate_remaining_stock(
    current_quantity,
    quantity_sold
):
    return current_quantity - quantity_sold


rose_quantity = 100

rose_quantity = calculate_remaining_stock(
    rose_quantity,
    25
)

print("Remaining roses:", rose_quantity)


# EXAMPLE 42: Flower Pricing Function
#
# The function receives all
# information through parameters.

def calculate_bouquet_total(price, quantity):
    subtotal = price * quantity

    return subtotal


bouquet_total = calculate_bouquet_total(
    75.00,
    2
)

print(f"Bouquet total: ${bouquet_total:.2f}")


# EXAMPLE 43: Customer Order Scope

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

order_total = calculate_order_total(
    order_items
)

print(f"Order total: ${order_total:.2f}")


# EXAMPLE 44: Security Event Counter
#
# A function uses a local
# counter and returns the result.

def count_failed_logins(events):
    count = 0

    for event in events:
        if event == "login_failed":
            count += 1

    return count


security_events = [
    "login_success",
    "login_failed",
    "login_failed",
    "port_scan"
]

failed_count = count_failed_logins(
    security_events
)

print("Failed logins:", failed_count)


# EXAMPLE 45: Security Configuration Scope
#
# Explicit configuration makes
# a function easier to reuse.

def create_security_summary(events, config):
    return {
        "server": config["server"],
        "total_events": len(events),
        "environment": config["environment"]
    }


configuration = {
    "server": "training-server",
    "environment": "lab"
}

events = [
    "login_success",
    "login_failed"
]

summary = create_security_summary(
    events,
    configuration
)

print("Summary:", summary)


# EXAMPLE 46: Independent Security Counters
#
# Closures can keep separate
# counters without globals.

def create_event_counter():
    count = 0

    def record_event():
        nonlocal count

        count += 1

        return count

    return record_event


server_a_counter = create_event_counter()
server_b_counter = create_event_counter()

print("Server A:", server_a_counter())
print("Server A:", server_a_counter())
print("Server B:", server_b_counter())


# EXAMPLE 47: Avoiding Shared Report State
#
# Return a new dictionary
# instead of modifying a
# shared global report.

def create_event_report(events):
    counts = {}

    for event in events:
        counts[event] = (
            counts.get(event, 0) + 1
        )

    return counts


events_a = [
    "login_failed",
    "port_scan"
]

events_b = [
    "login_success",
    "login_failed",
    "login_failed"
]

report_a = create_event_report(events_a)
report_b = create_event_report(events_b)

print("Report A:", report_a)
print("Report B:", report_b)


# EXAMPLE 48: Testing Independent Calls
#
# A reusable function should
# produce appropriate results
# for different inputs.

def calculate_total(numbers):
    return sum(numbers)


first_result = calculate_total([10, 20])
second_result = calculate_total([5, 15])

print("First result:", first_result)
print("Second result:", second_result)


# EXAMPLE 49: Nested Security Report Function
#
# An inner function can access
# the outer function's parameters.

def build_security_report(events):
    def count_events():
        return len(events)

    def count_unique_ips():
        unique_ips = {
            event["source_ip"]
            for event in events
        }

        return len(unique_ips)

    return {
        "total_events": count_events(),
        "unique_ips": count_unique_ips()
    }


security_events = [
    {"source_ip": "192.0.2.10"},
    {"source_ip": "192.0.2.20"},
    {"source_ip": "192.0.2.10"}
]

report = build_security_report(
    security_events
)

print("Security report:", report)


# EXAMPLE 50: Reusable Security Analysis
#
# This example uses:
#
# Local variables
# Function parameters
# Return values
# Nested functions
# No mutable global report state

def analyze_security_events(events):
    def count_categories():
        counts = {}

        for event in events:
            event_type = event["event_type"]

            counts[event_type] = (
                counts.get(event_type, 0) + 1
            )

        return counts

    def collect_unique_ips():
        return {
            event["source_ip"]
            for event in events
        }

    event_counts = count_categories()
    unique_ips = collect_unique_ips()

    return {
        "total_events": len(events),
        "event_counts": event_counts,
        "unique_ips": unique_ips
    }


def display_security_report(report):
    print("===== SECURITY EVENT REPORT =====")
    print("Total events:", report["total_events"])

    print(
        "Unique source IPs:",
        len(report["unique_ips"])
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
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "login_failed",
        "source_ip": "198.51.100.5"
    },
    {
        "event_type": "login_failed",
        "source_ip": "198.51.100.5"
    },
    {
        "event_type": "port_scan",
        "source_ip": "203.0.113.7"
    }
]

report_data = analyze_security_events(
    security_events
)

display_security_report(report_data)


# WHAT I LEARNED
#
# 1. Scope determines name accessibility.
# 2. Python uses LEGB name resolution.
# 3. Local variables belong to functions.
# 4. Parameters are local names.
# 5. Module-level names are global.
# 6. Functions can read global names.
# 7. Local names can shadow globals.
# 8. global allows global reassignment.
# 9. nonlocal allows enclosing reassignment.
# 10. Nested functions can access outer names.
# 11. Closures retain enclosing bindings.
# 12. Built-in names are provided by Python.
# 13. Avoid shadowing built-in functions.
# 14. return transfers values to callers.
# 15. Mutable arguments can be changed.
# 16. Copies can prevent unwanted mutation.
# 17. Loops do not create block scope.
# 18. if statements do not create block scope.
# 19. Comprehensions have their own scope.
# 20. Recursive calls have local variables.
# 21. Constants use uppercase conventions.
# 22. Parameters reduce global dependencies.
# 23. Functions should manage state clearly.
# 24. Local state supports reusable analysis.
# 25. Scope matters in cybersecurity programs.
