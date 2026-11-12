
# ==========================================
# DAY 24 - INPUT VALIDATION
# Topic: Checking and Validating Input
# ==========================================

# LESSON NOTES
#
# Input validation checks whether
# information meets the requirements
# of a program.
#
# Input may come from:
#
# Users
# Forms
# Files
# APIs
# Databases
# Network messages
# Other programs
#
# Validation helps prevent:
#
# Incorrect calculations
# Unexpected program behavior
# Invalid records
# Missing information
# Unsupported selections
# Some security vulnerabilities
#
# Important concepts:
#
# Data type validation
# Empty input validation
# Numeric validation
# Range validation
# String validation
# Membership validation
# Boolean validation
# Dictionary validation
# Repeated input
# Error messages
# Safe conversion
# try and except
# Validation functions
# Fail-closed decisions
#
# IMPORTANT:
#
# Validation does not replace
# authentication, authorization,
# parameterized SQL queries,
# output encoding, or other
# security controls.
#
# Never trust input solely
# because it came from
# a familiar source.
#
# The examples use synthetic data.
#
# Day 26 will cover exception
# handling in greater depth.


# EXAMPLE 1: Basic Input Validation
#
# Check whether a value
# meets a minimum requirement.

age = 23

is_valid = age >= 18

print("Valid age:", is_valid)


# EXAMPLE 2: Checking Data Types

value = 25

is_integer = isinstance(value, int)

print("Integer:", is_integer)


# EXAMPLE 3: Rejecting Boolean as Integer
#
# In Python, bool is a
# subclass of int.
#
# Explicitly reject bool when
# a numeric integer is required.

def is_valid_integer(value):
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
    )


print(is_valid_integer(25))
print(is_valid_integer(True))


# EXAMPLE 4: Validating a String

username = "alex"

is_valid = isinstance(username, str)

print("Valid string:", is_valid)


# EXAMPLE 5: Rejecting Empty Strings

username = ""

is_valid = bool(username)

print("Nonempty username:", is_valid)


# EXAMPLE 6: Removing Surrounding Whitespace
#
# strip() removes leading
# and trailing whitespace.

username = "   alex   "

clean_username = username.strip()

print("Clean username:", clean_username)


# EXAMPLE 7: Rejecting Whitespace-Only Input

username = "     "

is_valid = bool(username.strip())

print("Valid username:", is_valid)


# EXAMPLE 8: Minimum String Length

password = "TrainingPass123"

minimum_length = 12

is_valid = len(password) >= minimum_length

print("Meets minimum length:", is_valid)


# EXAMPLE 9: Maximum String Length

username = "alex"

maximum_length = 20

is_valid = len(username) <= maximum_length

print("Within maximum length:", is_valid)


# EXAMPLE 10: Combined Length Validation

def is_valid_username_length(username):
    if not isinstance(username, str):
        return False

    return 3 <= len(username) <= 20


print(is_valid_username_length("alex"))
print(is_valid_username_length("ab"))


# EXAMPLE 11: Alphabetic Input
#
# isalpha() checks whether
# all characters are letters.

name = "Alex"

is_valid = name.isalpha()

print("Alphabetic:", is_valid)


# EXAMPLE 12: Numeric String Input
#
# isdigit() checks digit characters.
#
# It does not validate every
# possible numeric format.

quantity_text = "25"

is_valid = quantity_text.isdigit()

print("Digit string:", is_valid)


# EXAMPLE 13: Alphanumeric Input

username = "alex123"

is_valid = username.isalnum()

print("Alphanumeric:", is_valid)


# EXAMPLE 14: Normalizing Case
#
# casefold() supports
# case-insensitive comparisons.

response = "YES"

normalized = response.strip().casefold()

print("Normalized:", normalized)


# EXAMPLE 15: Allowed Values

response = "yes"

allowed = {"yes", "no"}

is_valid = response in allowed

print("Allowed response:", is_valid)


# EXAMPLE 16: Validating Menu Selections

selection = "2"

valid_options = {"1", "2", "3"}

is_valid = selection in valid_options

print("Valid selection:", is_valid)


# EXAMPLE 17: Validating Numeric Ranges

quantity = 5

is_valid = 1 <= quantity <= 100

print("Valid quantity:", is_valid)


# EXAMPLE 18: Rejecting Negative Quantities

quantity = -3

is_valid = quantity >= 0

print("Valid inventory quantity:", is_valid)


# EXAMPLE 19: Validating Prices

price = 75.00

is_valid = (
    isinstance(price, (int, float))
    and not isinstance(price, bool)
    and price >= 0
)

print("Valid basic price:", is_valid)


# EXAMPLE 20: Floating-Point Conversion
#
# float() can convert valid
# numeric strings.
#
# Invalid strings raise ValueError.

price_text = "75.50"

price = float(price_text)

print("Converted price:", price)


# EXAMPLE 21: Safe Integer Conversion
#
# try and except can catch
# expected conversion failures.

def parse_integer(value):
    try:
        return int(value)
    except (ValueError, TypeError, OverflowError):
        return None


print(parse_integer("25"))
print(parse_integer("abc"))


# EXAMPLE 22: Safe Float Conversion

def parse_float(value):
    try:
        return float(value)
    except (ValueError, TypeError, OverflowError):
        return None


print(parse_float("75.50"))
print(parse_float("invalid"))


# EXAMPLE 23: Validate After Conversion
#
# Conversion and validation
# are separate steps.

def validate_quantity(value):
    quantity = parse_integer(value)

    if quantity is None:
        return False

    return 1 <= quantity <= 100


print(validate_quantity("5"))
print(validate_quantity("150"))
print(validate_quantity("abc"))


# EXAMPLE 24: Avoiding Ambiguous Integer Parsing
#
# int(3.9) produces 3.
#
# That truncation may not
# be appropriate for quantities.
#
# Validate accepted input
# formats before converting.

def parse_quantity_text(value):
    if not isinstance(value, str):
        return None

    cleaned = value.strip()

    if not cleaned.isascii() or not cleaned.isdecimal():
        return None

    return int(cleaned)


print(parse_quantity_text("12"))
print(parse_quantity_text("3.9"))
print(parse_quantity_text("-2"))


# EXAMPLE 25: Validating Optional Values
#
# None can represent
# an absent optional value.

def validate_optional_note(note):
    if note is None:
        return True

    return (
        isinstance(note, str)
        and len(note) <= 200
    )


print(validate_optional_note(None))
print(validate_optional_note("Leave at desk"))
print(validate_optional_note(123))


# EXAMPLE 26: Returning Validation Messages

def validate_age(age):
    if not is_valid_integer(age):
        return False, "Age must be an integer."

    if age < 18:
        return False, "Age must be at least 18."

    return True, "Age accepted."


print(validate_age(23))
print(validate_age(16))


# EXAMPLE 27: Early Return Validation
#
# Reject invalid information
# before performing more work.

def validate_product_name(name):
    if not isinstance(name, str):
        return False

    if not name.strip():
        return False

    if len(name) > 50:
        return False

    return True


print(validate_product_name("Rose Bouquet"))
print(validate_product_name("   "))


# EXAMPLE 28: Multiple Validation Rules

def validate_username(username):
    if not isinstance(username, str):
        return False

    if not 3 <= len(username) <= 20:
        return False

    if not username.isascii():
        return False

    return all(
        character.isalnum() or character == "_"
        for character in username
    )


print(validate_username("alex_123"))
print(validate_username("alex!"))


# EXAMPLE 29: Checking Required Dictionary Keys

def has_required_keys(record):
    required = {
        "username",
        "role",
        "active"
    }

    return (
        isinstance(record, dict)
        and required.issubset(record.keys())
    )


record = {
    "username": "alex",
    "role": "analyst",
    "active": True
}

print("Required keys:", has_required_keys(record))


# EXAMPLE 30: Validating Dictionary Values

def validate_user_record(record):
    if not isinstance(record, dict):
        return False

    if not has_required_keys(record):
        return False

    if not validate_username(record["username"]):
        return False

    if record["role"] not in {"admin", "analyst", "viewer"}:
        return False

    return isinstance(record["active"], bool)


user = {
    "username": "alex",
    "role": "analyst",
    "active": True
}

print("Valid user:", validate_user_record(user))


# EXAMPLE 31: Validating a List

def validate_tools(tools):
    if not isinstance(tools, list):
        return False

    if not tools:
        return False

    return all(
        isinstance(tool, str) and bool(tool.strip())
        for tool in tools
    )


tools = ["Python", "Wireshark", "Nmap"]

print("Valid tools:", validate_tools(tools))


# EXAMPLE 32: Validating Each Record

def filter_valid_users(records):
    return [
        record
        for record in records
        if validate_user_record(record)
    ]


records = [
    {
        "username": "alex",
        "role": "analyst",
        "active": True
    },
    {
        "username": "x!",
        "role": "viewer",
        "active": True
    }
]

valid_users = filter_valid_users(records)

print("Valid users:", valid_users)


# EXAMPLE 33: Simulated Repeated Input
#
# Real input() waits for
# a user to type a response.
#
# This example uses prepared
# responses so it runs
# without stopping.

responses = ["abc", "-2", "5"]

accepted_quantity = None

for response in responses:
    quantity = parse_quantity_text(response)

    if quantity is None:
        print("Invalid number:", response)
        continue

    if quantity < 1:
        print("Quantity must be positive.")
        continue

    accepted_quantity = quantity
    break

print("Accepted quantity:", accepted_quantity)


# EXAMPLE 34: Limited Validation Attempts
#
# Limit repeated attempts
# instead of looping forever.

responses = ["wrong", "invalid", "yes"]

allowed = {"yes", "no"}

accepted = None

for response in responses[:3]:
    normalized = response.strip().casefold()

    if normalized in allowed:
        accepted = normalized
        break

print("Accepted response:", accepted)


# EXAMPLE 35: Reusable Menu Validation

def validate_menu_option(selection, options):
    if not isinstance(selection, str):
        return False

    return selection.strip() in options


options = {"1", "2", "3"}

print(validate_menu_option("2", options))
print(validate_menu_option("9", options))


# EXAMPLE 36: Email Format Check
#
# This is a simplified
# format check only.
#
# It does not verify that
# an email address exists
# or can receive messages.

def has_basic_email_format(email):
    if not isinstance(email, str):
        return False

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    return (
        bool(local)
        and "." in domain
        and not domain.startswith(".")
        and not domain.endswith(".")
        and " " not in email
    )


print(has_basic_email_format("alex@example.com"))
print(has_basic_email_format("invalid-email"))


# EXAMPLE 37: Validating a Date
#
# datetime can reject
# impossible calendar dates.

from datetime import datetime


def is_valid_date(value):
    if not isinstance(value, str):
        return False

    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


print(is_valid_date("2026-11-11"))
print(is_valid_date("2026-02-30"))


# EXAMPLE 38: Validating a Network Port

def is_valid_port(port):
    return (
        is_valid_integer(port)
        and 1 <= port <= 65535
    )


print(is_valid_port(22))
print(is_valid_port(70000))
print(is_valid_port(True))


# EXAMPLE 39: Validating an IP Address
#
# Use the standard library
# instead of manually
# checking dotted strings.

import ipaddress


def is_valid_ip(value):
    if not isinstance(value, str):
        return False

    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


print(is_valid_ip("192.0.2.10"))
print(is_valid_ip("999.999.999.999"))


# EXAMPLE 40: Validating Event Types

def is_valid_event_type(event_type):
    allowed_types = {
        "login_success",
        "login_failed",
        "port_scan",
        "file_access"
    }

    return (
        isinstance(event_type, str)
        and event_type in allowed_types
    )


print(is_valid_event_type("login_failed"))
print(is_valid_event_type("unknown_event"))


# EXAMPLE 41: Flower Quantity Validation

def validate_flower_quantity(quantity):
    return (
        is_valid_integer(quantity)
        and 1 <= quantity <= 100
    )


print(validate_flower_quantity(5))
print(validate_flower_quantity(-3))


# EXAMPLE 42: Flower Product Selection

def validate_flower_selection(selection):
    available_products = {
        "rose bouquet",
        "tulip bouquet",
        "mixed bouquet"
    }

    if not isinstance(selection, str):
        return False

    normalized = selection.strip().casefold()

    return normalized in available_products


print(validate_flower_selection("Rose Bouquet"))
print(validate_flower_selection("Unknown Bouquet"))


# EXAMPLE 43: Delivery Area Validation
#
# These are example supported
# cities for a training program.

def validate_delivery_city(city):
    supported_cities = {
        "las cruces",
        "el paso"
    }

    if not isinstance(city, str):
        return False

    normalized = city.strip().casefold()

    return normalized in supported_cities


print(validate_delivery_city("Las Cruces"))
print(validate_delivery_city("Phoenix"))


# EXAMPLE 44: Customer Name Validation

def validate_customer_name(name):
    if not isinstance(name, str):
        return False

    cleaned = name.strip()

    return 2 <= len(cleaned) <= 60


print(validate_customer_name("Alex Morgan"))
print(validate_customer_name(" "))


# EXAMPLE 45: Flower Order Validation

def validate_flower_order(order):
    if not isinstance(order, dict):
        return False

    required = {
        "customer",
        "product",
        "quantity",
        "delivery_city"
    }

    if not required.issubset(order.keys()):
        return False

    return (
        validate_customer_name(order["customer"])
        and validate_flower_selection(order["product"])
        and validate_flower_quantity(order["quantity"])
        and validate_delivery_city(order["delivery_city"])
    )


order = {
    "customer": "Alex Morgan",
    "product": "Rose Bouquet",
    "quantity": 2,
    "delivery_city": "Las Cruces"
}

print("Valid order:", validate_flower_order(order))


# EXAMPLE 46: Validating Security Records

def validate_security_event(event):
    if not isinstance(event, dict):
        return False

    required = {
        "event_type",
        "source_ip",
        "severity"
    }

    if not required.issubset(event.keys()):
        return False

    allowed_severities = {
        "low",
        "medium",
        "high"
    }

    return (
        is_valid_event_type(event["event_type"])
        and is_valid_ip(event["source_ip"])
        and isinstance(event["severity"], str)
        and event["severity"] in allowed_severities
    )


event = {
    "event_type": "login_failed",
    "source_ip": "192.0.2.10",
    "severity": "high"
}

print("Valid security event:", validate_security_event(event))


# EXAMPLE 47: Separating Valid and Invalid Data

def separate_events(events):
    valid_events = []
    invalid_events = []

    for event in events:
        if validate_security_event(event):
            valid_events.append(event.copy())
        else:
            invalid_events.append(event)

    return valid_events, invalid_events


events = [
    {
        "event_type": "login_failed",
        "source_ip": "192.0.2.10",
        "severity": "high"
    },
    {
        "event_type": "unknown_event",
        "source_ip": "999.999.999.999",
        "severity": "high"
    }
]

valid_events, invalid_events = separate_events(events)

print("Valid events:", len(valid_events))
print("Invalid events:", len(invalid_events))


# EXAMPLE 48: Fail-Closed Access Decision
#
# Missing or invalid data
# should not automatically
# grant access.
#
# This is a training simulation,
# not a complete access system.

def validate_access_request(request):
    if not isinstance(request, dict):
        return False

    required = {
        "active",
        "locked",
        "role"
    }

    if not required.issubset(request.keys()):
        return False

    if not isinstance(request["active"], bool):
        return False

    if not isinstance(request["locked"], bool):
        return False

    if request["role"] not in {"admin", "analyst"}:
        return False

    return (
        request["active"]
        and not request["locked"]
    )


request = {
    "active": True,
    "locked": False,
    "role": "analyst"
}

print("Access allowed:", validate_access_request(request))


# EXAMPLE 49: Returning Validation Errors
#
# A validator can return
# both a result and a
# list of useful error messages.

def validate_order_with_errors(order):
    errors = []

    if not isinstance(order, dict):
        return False, ["Order must be a dictionary."]

    if not validate_customer_name(order.get("customer")):
        errors.append("Invalid customer name.")

    if not validate_flower_selection(order.get("product")):
        errors.append("Invalid product selection.")

    if not validate_flower_quantity(order.get("quantity")):
        errors.append("Invalid quantity.")

    if not validate_delivery_city(order.get("delivery_city")):
        errors.append("Unsupported delivery city.")

    return len(errors) == 0, errors


order = {
    "customer": "Alex Morgan",
    "product": "Rose Bouquet",
    "quantity": -2,
    "delivery_city": "Las Cruces"
}

is_valid, errors = validate_order_with_errors(order)

print("Order valid:", is_valid)
print("Validation errors:", errors)


# EXAMPLE 50: Complete Input Validation Workflow
#
# This example combines:
#
# String validation
# Numeric validation
# Allowed values
# Dictionary validation
# Error messages
# Return values
# Business calculations
#
# It prepares for Day 25.
#
# Prices are fictional
# training values.

PRODUCT_PRICES = {
    "rose bouquet": 75.00,
    "tulip bouquet": 65.00,
    "mixed bouquet": 85.00
}


def validate_order_data(order):
    valid, errors = validate_order_with_errors(order)

    if not valid:
        return False, errors

    return True, []


def calculate_order_subtotal(order):
    product = order["product"].strip().casefold()

    price = PRODUCT_PRICES[product]

    return price * order["quantity"]


def create_order_summary(order):
    valid, errors = validate_order_data(order)

    if not valid:
        return {
            "accepted": False,
            "errors": errors
        }

    subtotal = calculate_order_subtotal(order)

    return {
        "accepted": True,
        "customer": order["customer"].strip(),
        "product": order["product"].strip(),
        "quantity": order["quantity"],
        "delivery_city": order["delivery_city"].strip(),
        "subtotal": subtotal
    }


def display_order_summary(summary):
    print("===== FLOWER ORDER SUMMARY =====")

    if not summary["accepted"]:
        print("Order rejected.")

        for error in summary["errors"]:
            print("Error:", error)

        return

    print("Customer:", summary["customer"])
    print("Product:", summary["product"])
    print("Quantity:", summary["quantity"])
    print("Delivery:", summary["delivery_city"])

    print(
        f"Subtotal: ${summary['subtotal']:.2f}"
    )


sample_order = {
    "customer": "Alex Morgan",
    "product": "Rose Bouquet",
    "quantity": 2,
    "delivery_city": "Las Cruces"
}

summary = create_order_summary(sample_order)

display_order_summary(summary)


# WHAT I LEARNED
#
# 1. Input validation checks data.
# 2. Input may come from many sources.
# 3. Data types should be validated.
# 4. Empty strings may be rejected.
# 5. Whitespace can affect input.
# 6. String lengths can be checked.
# 7. Character rules can be checked.
# 8. Input can be normalized.
# 9. Allowed values can be enforced.
# 10. Numeric ranges can be checked.
# 11. Negative values may be invalid.
# 12. Conversions may raise exceptions.
# 13. try/except handles expected errors.
# 14. Conversion and validation differ.
# 15. Validation functions return results.
# 16. Early returns reject bad input.
# 17. Dictionary keys can be checked.
# 18. Dictionary values can be checked.
# 19. Lists can be validated.
# 20. Repeated input can be limited.
# 21. Email format checks have limits.
# 22. Dates can be validated.
# 23. Network ports can be validated.
# 24. IP addresses can be validated.
# 25. Event categories can be checked.
# 26. Business orders require validation.
# 27. Security records require validation.
# 28. Invalid data can be separated.
# 29. Fail-closed decisions reject bad data.
# 30. Error messages explain failures.
# 31. Validation should precede processing.
# 32. Validation alone is not security.
