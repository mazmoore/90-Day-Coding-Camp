
# ==========================================
# DAY 23 - BOOLEAN LOGIC
# Topic: True, False, and Logical Operators
# ==========================================

# LESSON NOTES
#
# Boolean values represent
# one of two possible states:
#
# True
# False
#
# Boolean values are used
# to evaluate conditions.
#
# Python's Boolean type is bool.
#
# Comparison operators:
#
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
#
# Logical operators:
#
# and
# or
# not
#
# Other important concepts:
#
# Truthy values
# Falsy values
# Short-circuit evaluation
# Operator precedence
# Chained comparisons
# Membership testing
# Identity testing
# Boolean functions
#
# Boolean logic is useful for:
#
# Input validation
# Login checks
# Permission checks
# Inventory decisions
# Security monitoring
# Event filtering
# Alert conditions


# EXAMPLE 1: Boolean Values
#
# Boolean values must use
# capitalized True and False.

is_active = True
is_locked = False

print("Active:", is_active)
print("Locked:", is_locked)


# EXAMPLE 2: Boolean Data Type

status = True

print("Value:", status)
print("Type:", type(status))


# EXAMPLE 3: Equality Operator
#
# == checks whether two
# values are equal.

number = 10

print("Equal to 10:", number == 10)
print("Equal to 5:", number == 5)


# EXAMPLE 4: Inequality Operator
#
# != checks whether values
# are different.

username = "alex"

print("Not admin:", username != "admin")
print("Not alex:", username != "alex")


# EXAMPLE 5: Greater Than

score = 85

print("Above 70:", score > 70)
print("Above 90:", score > 90)


# EXAMPLE 6: Less Than

temperature = 25

print("Below 30:", temperature < 30)
print("Below 20:", temperature < 20)


# EXAMPLE 7: Greater Than or Equal To

grade = 90

print("At least 90:", grade >= 90)
print("At least 95:", grade >= 95)


# EXAMPLE 8: Less Than or Equal To

attempts = 3

print("At most 3:", attempts <= 3)
print("At most 2:", attempts <= 2)


# EXAMPLE 9: Combining Comparisons

age = 23

is_adult = age >= 18
is_under_30 = age < 30

print("Adult:", is_adult)
print("Under 30:", is_under_30)


# EXAMPLE 10: Logical and
#
# and is True only when
# both conditions are True.

has_username = True
has_password = True

can_attempt_login = (
    has_username and has_password
)

print("Can attempt login:", can_attempt_login)


# EXAMPLE 11: and with False

has_username = True
has_password = False

can_attempt_login = (
    has_username and has_password
)

print("Can attempt login:", can_attempt_login)


# EXAMPLE 12: Logical or
#
# or is True when at least
# one condition is True.

is_admin = False
is_analyst = True

has_review_role = is_admin or is_analyst

print("Has review role:", has_review_role)


# EXAMPLE 13: or with False Values

is_admin = False
is_analyst = False

has_review_role = is_admin or is_analyst

print("Has review role:", has_review_role)


# EXAMPLE 14: Logical not
#
# not reverses a Boolean value.

account_locked = False

print("Account locked:", account_locked)
print("Account unlocked:", not account_locked)


# EXAMPLE 15: and Truth Table

values = [True, False]

for first in values:
    for second in values:
        print(
            first,
            "and",
            second,
            "=",
            first and second
        )


# EXAMPLE 16: or Truth Table

values = [True, False]

for first in values:
    for second in values:
        print(
            first,
            "or",
            second,
            "=",
            first or second
        )


# EXAMPLE 17: not Truth Table

for value in [True, False]:
    print("not", value, "=", not value)


# EXAMPLE 18: Multiple and Conditions

age = 23
has_id = True
account_active = True

eligible = (
    age >= 18
    and has_id
    and account_active
)

print("Eligible:", eligible)


# EXAMPLE 19: Multiple or Conditions

event_type = "port_scan"

needs_review = (
    event_type == "login_failed"
    or event_type == "port_scan"
    or event_type == "malware_alert"
)

print("Needs review:", needs_review)


# EXAMPLE 20: Combining and and or
#
# Parentheses clarify grouping.
#
# This example requires:
#
# An active account
# AND
# An admin or analyst role.

role = "analyst"
account_active = True

has_access = (
    account_active
    and (
        role == "admin"
        or role == "analyst"
    )
)

print("Has access:", has_access)


# EXAMPLE 21: Operator Precedence
#
# For these Boolean operators:
#
# not is evaluated before and.
# and is evaluated before or.
#
# Parentheses are recommended
# when conditions become complex.

result = True or False and False

print("Result:", result)


# EXAMPLE 22: Chained Comparisons
#
# Python supports comparisons
# such as 1 <= number <= 10.

number = 7

within_range = 1 <= number <= 10

print("Within range:", within_range)


# EXAMPLE 23: Checking Numeric Ranges

port = 443

valid_port = 1 <= port <= 65535

print("Valid port range:", valid_port)


# EXAMPLE 24: Membership with in

tools = [
    "Wireshark",
    "Nmap",
    "Python"
]

has_python = "Python" in tools

print("Python available:", has_python)


# EXAMPLE 25: Membership with not in

tools = [
    "Wireshark",
    "Nmap",
    "Python"
]

missing_java = "Java" not in tools

print("Java missing:", missing_java)


# EXAMPLE 26: Membership in a Dictionary
#
# in checks dictionary keys
# unless another view is used.

user = {
    "username": "alex",
    "role": "analyst"
}

print("Has role key:", "role" in user)
print("Has email key:", "email" in user)


# EXAMPLE 27: Membership in a Set

permissions = {
    "read",
    "write"
}

can_read = "read" in permissions
can_execute = "execute" in permissions

print("Read label present:", can_read)
print("Execute label present:", can_execute)


# EXAMPLE 28: Identity with is
#
# is checks object identity.
#
# It is not the same as ==.
#
# Use is None for checking None.

result = None

print("Result is None:", result is None)
print("Result is not None:", result is not None)


# EXAMPLE 29: Equality Versus Identity
#
# == compares values.
#
# is compares object identity.

first = [1, 2, 3]
second = [1, 2, 3]
alias = first

print("Equal values:", first == second)
print("Same object:", first is second)
print("Alias same object:", first is alias)


# EXAMPLE 30: Truthy Values
#
# Nonempty collections and
# nonzero numbers are truthy.

username = "alex"

if username:
    print("Username is not empty.")


# EXAMPLE 31: Falsy Values
#
# Common falsy values:
#
# False
# None
# 0
# 0.0
# ""
# []
# ()
# {}
# set()

values = [
    False,
    None,
    0,
    "",
    [],
    {}
]

for value in values:
    print(value, "->", bool(value))


# EXAMPLE 32: bool() Conversion

print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Python'):", bool("Python"))
print("bool(''):", bool(""))


# EXAMPLE 33: Checking an Empty List

events = []

if not events:
    print("No security events recorded.")


# EXAMPLE 34: Checking a Nonempty Dictionary

user = {
    "username": "alex"
}

if user:
    print("User information is available.")


# EXAMPLE 35: Short-Circuit and
#
# If the first condition is False,
# Python does not need to
# evaluate the second condition.

events = []

has_first_event = (
    len(events) > 0
    and events[0] == "login_failed"
)

print("First event failed:", has_first_event)


# EXAMPLE 36: Short-Circuit or
#
# If the first condition is True,
# Python does not need to
# evaluate the second condition.

is_admin = True
has_special_permission = False

allowed = (
    is_admin
    or has_special_permission
)

print("Allowed:", allowed)


# EXAMPLE 37: and/or Return Operands
#
# and and or can return
# operands rather than bool.
#
# Use bool() when an actual
# Boolean result is required.

username = ""

display_name = username or "Guest"

print("Display name:", display_name)


# EXAMPLE 38: Boolean Function

def is_passing(grade):
    return grade >= 70


print("90 passes:", is_passing(90))
print("65 passes:", is_passing(65))


# EXAMPLE 39: Boolean Validation Function

def is_valid_port(port):
    if isinstance(port, bool):
        return False

    return (
        isinstance(port, int)
        and 1 <= port <= 65535
    )


print("Port 22:", is_valid_port(22))
print("Port 70000:", is_valid_port(70000))
print("Port True:", is_valid_port(True))


# EXAMPLE 40: Password Rule Check
#
# This checks basic rules only.
#
# It is not a complete
# password security assessment.
#
# Never print or store real
# account passwords in logs.

def meets_basic_password_rules(password):
    has_length = len(password) >= 12

    has_digit = any(
        character.isdigit()
        for character in password
    )

    has_letter = any(
        character.isalpha()
        for character in password
    )

    return (
        has_length
        and has_digit
        and has_letter
    )


sample_password = "TrainingPass123"

print(
    "Meets basic rules:",
    meets_basic_password_rules(sample_password)
)


# EXAMPLE 41: Flower Inventory Decision

rose_quantity = 8
minimum_stock = 10

needs_restock = rose_quantity < minimum_stock

print("Needs restock:", needs_restock)


# EXAMPLE 42: Flower Order Eligibility

inventory_available = True
delivery_area_supported = True
payment_confirmed = True

can_process_order = (
    inventory_available
    and delivery_area_supported
    and payment_confirmed
)

print("Can process order:", can_process_order)


# EXAMPLE 43: Customer Discount Eligibility

order_total = 150.00
is_loyal_customer = True

eligible_for_discount = (
    order_total >= 200
    or is_loyal_customer
)

print(
    "Discount eligible:",
    eligible_for_discount
)


# EXAMPLE 44: Account Access Decision
#
# This is a simplified
# training example.
#
# Real access control requires
# server-side enforcement and
# additional security controls.

account_active = True
account_locked = False
role = "analyst"

can_review_events = (
    account_active
    and not account_locked
    and role in {"analyst", "admin"}
)

print("Can review events:", can_review_events)


# EXAMPLE 45: Failed Login Alert Condition
#
# A threshold is a condition
# used to decide whether
# further review is needed.
#
# This is not a production
# intrusion detection rule.

failed_attempts = 5
alert_threshold = 3

should_alert = failed_attempts >= alert_threshold

print("Alert condition met:", should_alert)


# EXAMPLE 46: Suspicious Event Classification
#
# These categories are
# simplified training labels.

event_type = "port_scan"
source_known = False

needs_review = (
    event_type in {
        "login_failed",
        "port_scan",
        "malware_alert"
    }
    and not source_known
)

print("Needs review:", needs_review)


# EXAMPLE 47: Filtering with Boolean Logic

security_events = [
    {
        "event_type": "login_failed",
        "severity": "high"
    },
    {
        "event_type": "login_success",
        "severity": "low"
    },
    {
        "event_type": "port_scan",
        "severity": "medium"
    }
]

review_events = []

for event in security_events:
    if (
        event["event_type"] == "login_failed"
        or event["severity"] == "high"
    ):
        review_events.append(event)

print("Review events:", review_events)


# EXAMPLE 48: Using any() and all()

security_checks = {
    "firewall_enabled": True,
    "logging_enabled": True,
    "updates_current": False
}

all_checks_pass = all(
    security_checks.values()
)

any_check_failed = any(
    not status
    for status in security_checks.values()
)

print("All checks pass:", all_checks_pass)
print("Any check failed:", any_check_failed)


# EXAMPLE 49: Boolean Security Policy Function
#
# This function evaluates
# simple permission labels.
#
# It does not enforce access
# on a real system.

def can_access_report(user, required_role):
    account_active = user.get("active", False)
    account_locked = user.get("locked", True)

    user_role = user.get("role")

    return (
        account_active
        and not account_locked
        and user_role == required_role
    )


user = {
    "username": "alex",
    "role": "analyst",
    "active": True,
    "locked": False
}

print(
    "Report access:",
    can_access_report(user, "analyst")
)


# EXAMPLE 50: Boolean Security Event Report
#
# This example combines:
#
# Boolean conditions
# Comparison operators
# Logical operators
# Membership checks
# Functions
# Loops
# Nested dictionaries
#
# All event records are synthetic.

def needs_security_review(event):
    event_type = event["event_type"]
    severity = event["severity"]

    review_types = {
        "login_failed",
        "port_scan",
        "malware_alert"
    }

    return (
        event_type in review_types
        and severity in {"medium", "high"}
    )


def is_failed_login(event):
    return event["event_type"] == "login_failed"


def analyze_events(events):
    review_events = []
    failed_logins = 0

    for event in events:
        if needs_security_review(event):
            review_events.append(event.copy())

        if is_failed_login(event):
            failed_logins += 1

    return {
        "total_events": len(events),
        "failed_logins": failed_logins,
        "review_events": review_events,
        "has_review_events": bool(review_events)
    }


def display_report(report):
    print("===== SECURITY REVIEW REPORT =====")
    print("Total events:", report["total_events"])
    print("Failed logins:", report["failed_logins"])

    print(
        "Events requiring review:",
        len(report["review_events"])
    )

    print(
        "Review needed:",
        report["has_review_events"]
    )

    for event in report["review_events"]:
        print(
            event["event_type"],
            event["severity"],
            event["source_ip"]
        )


security_events = [
    {
        "event_type": "login_success",
        "severity": "low",
        "source_ip": "192.0.2.10"
    },
    {
        "event_type": "login_failed",
        "severity": "high",
        "source_ip": "198.51.100.5"
    },
    {
        "event_type": "port_scan",
        "severity": "medium",
        "source_ip": "203.0.113.7"
    },
    {
        "event_type": "file_access",
        "severity": "low",
        "source_ip": "192.0.2.20"
    }
]

report = analyze_events(security_events)

display_report(report)


# WHAT I LEARNED
#
# 1. Boolean values are True and False.
# 2. bool is Python's Boolean type.
# 3. == checks equality.
# 4. != checks inequality.
# 5. > and < compare numeric values.
# 6. >= and <= include equality.
# 7. and combines required conditions.
# 8. or accepts alternative conditions.
# 9. not reverses truth values.
# 10. Truth tables show logical outcomes.
# 11. Parentheses clarify complex logic.
# 12. not, and, or have precedence rules.
# 13. Python supports chained comparisons.
# 14. in checks membership.
# 15. not in checks absence.
# 16. is checks object identity.
# 17. Truthy values behave like True.
# 18. Falsy values behave like False.
# 19. bool() performs truth-value conversion.
# 20. Short-circuiting can skip expressions.
# 21. and/or can return non-Boolean operands.
# 22. Functions can return Boolean results.
# 23. Boolean logic supports validation.
# 24. Boolean logic supports inventory checks.
# 25. Boolean logic supports access decisions.
# 26. Boolean logic supports event filtering.
# 27. any() and all() combine conditions.
# 28. Boolean logic supports security reports.
