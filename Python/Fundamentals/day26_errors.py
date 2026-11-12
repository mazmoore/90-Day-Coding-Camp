
# ==========================================
# DAY 26 - ERROR HANDLING
# Topic: Exceptions and Reliable Programs
# ==========================================

# LESSON NOTES
#
# An error occurs when a program
# encounters a problem.
#
# A syntax error prevents Python
# from parsing the program.
#
# An exception occurs during
# program execution.
#
# Common exceptions include:
#
# ValueError
# TypeError
# ZeroDivisionError
# IndexError
# KeyError
# FileNotFoundError
# PermissionError
# AttributeError
# OverflowError
# RuntimeError
# AssertionError
#
# Python uses:
#
# try
# except
# else
# finally
# raise
#
# try:
#     Code that may fail.
#
# except:
#     Handle an expected exception.
#
# else:
#     Run when no exception occurs.
#
# finally:
#     Run whether an exception
#     occurs or not.
#
# raise:
#     Explicitly trigger an exception.
#
# Best practices:
#
# Catch specific exceptions.
# Keep try blocks focused.
# Provide useful error messages.
# Avoid hiding unexpected errors.
# Do not expose sensitive information.
# Validate input before processing.
# Clean up resources properly.
# Never use exceptions as a substitute
# for authentication or authorization.
#
# All data in this lesson is synthetic.


# ==========================================
# SECTION 1 - BASIC EXCEPTIONS
# ==========================================


# EXAMPLE 1: Basic try/except
#
# int() raises ValueError when
# a string cannot be converted.

try:
    number = int("abc")
    print(number)

except ValueError:
    print("Example 1: Invalid integer.")


# EXAMPLE 2: Successful Conversion

try:
    number = int("25")
    print("Example 2:", number)

except ValueError:
    print("Invalid integer.")


# EXAMPLE 3: ZeroDivisionError

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Example 3: Cannot divide by zero.")


# EXAMPLE 4: TypeError

try:
    result = "10" + 5
    print(result)

except TypeError:
    print("Example 4: Incompatible types.")


# EXAMPLE 5: IndexError

numbers = [10, 20, 30]

try:
    print(numbers[10])

except IndexError:
    print("Example 5: Index does not exist.")


# EXAMPLE 6: KeyError

user = {
    "username": "alex",
    "role": "analyst"
}

try:
    print(user["email"])

except KeyError:
    print("Example 6: Missing dictionary key.")


# EXAMPLE 7: AttributeError

value = 25

try:
    value.append(10)

except AttributeError:
    print("Example 7: Method not available.")


# EXAMPLE 8: FileNotFoundError
#
# Use a deliberately missing
# filename for this example.

try:
    with open(
        "__day26_missing_example__.txt",
        "r",
        encoding="utf-8"
    ) as file:
        print(file.read())

except FileNotFoundError:
    print("Example 8: File not found.")


# EXAMPLE 9: Multiple except Blocks

value = "invalid"

try:
    number = int(value)
    result = 100 / number
    print(result)

except ValueError:
    print("Example 9: Invalid number.")

except ZeroDivisionError:
    print("Example 9: Division by zero.")


# EXAMPLE 10: Catching Multiple Types
#
# A tuple of exception classes
# can be used with except.

try:
    result = int(None)
    print(result)

except (ValueError, TypeError):
    print("Example 10: Conversion failed.")


# ==========================================
# SECTION 2 - EXCEPTION INFORMATION
# ==========================================


# EXAMPLE 11: Exception Object
#
# as error gives access
# to the exception object.

try:
    number = int("hello")

except ValueError as error:
    print("Example 11:", error)


# EXAMPLE 12: Exception Class Name

try:
    result = 5 / 0

except ZeroDivisionError as error:
    print(
        "Example 12:",
        type(error).__name__
    )


# EXAMPLE 13: Specific Error Messages

def convert_age(value):
    try:
        return int(value)

    except ValueError:
        print("Age must contain a valid integer.")
        return None

    except TypeError:
        print("Age must not be a missing value.")
        return None


print("Example 13:", convert_age("abc"))


# EXAMPLE 14: Exception Handling in a Function

def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return None


print("Example 14:", safe_divide(10, 2))
print("Example 14:", safe_divide(10, 0))


# EXAMPLE 15: Returning Error Information

def divide_with_message(a, b):
    try:
        result = a / b
        return True, result, None

    except (TypeError, ZeroDivisionError):
        return False, None, "Division failed."


print(
    "Example 15:",
    divide_with_message(10, 0)
)


# ==========================================
# SECTION 3 - ELSE AND FINALLY
# ==========================================


# EXAMPLE 16: try/except/else
#
# else runs only when the
# try block succeeds.

try:
    number = int("50")

except ValueError:
    print("Conversion failed.")

else:
    print("Example 16: Converted:", number)


# EXAMPLE 17: else with Failure

try:
    number = int("invalid")

except ValueError:
    print("Example 17: Conversion failed.")

else:
    print("Converted:", number)


# EXAMPLE 18: finally Block
#
# finally runs after the
# try/except handling.

try:
    result = 10 / 2
    print("Example 18:", result)

except ZeroDivisionError:
    print("Division failed.")

finally:
    print("Example 18: Finished.")


# EXAMPLE 19: finally After an Error

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Example 19: Division failed.")

finally:
    print("Example 19: Cleanup step.")


# EXAMPLE 20: All Four Blocks

try:
    number = int("15")

except ValueError:
    print("Invalid number.")

else:
    print("Example 20: Valid:", number)

finally:
    print("Example 20: Validation attempt ended.")


# ==========================================
# SECTION 4 - RAISING EXCEPTIONS
# ==========================================


# EXAMPLE 21: raise ValueError
#
# raise explicitly triggers
# an exception.

def require_positive(number):
    if number <= 0:
        raise ValueError(
            "Number must be positive."
        )

    return number


try:
    require_positive(-5)

except ValueError as error:
    print("Example 21:", error)


# EXAMPLE 22: Raising TypeError

def require_string(value):
    if not isinstance(value, str):
        raise TypeError(
            "Expected a string."
        )

    return value


try:
    require_string(123)

except TypeError as error:
    print("Example 22:", error)


# EXAMPLE 23: Raising for Invalid Quantity

def validate_quantity(quantity):
    if isinstance(quantity, bool):
        raise TypeError(
            "Quantity cannot be Boolean."
        )

    if not isinstance(quantity, int):
        raise TypeError(
            "Quantity must be an integer."
        )

    if quantity < 1:
        raise ValueError(
            "Quantity must be positive."
        )

    return quantity


try:
    validate_quantity(0)

except (TypeError, ValueError) as error:
    print("Example 23:", error)


# EXAMPLE 24: Raising for Missing Product

def get_product(catalog, product_id):
    if product_id not in catalog:
        raise KeyError(
            "Unknown product ID."
        )

    return catalog[product_id]


catalog = {
    "F001": "Rose Bouquet"
}

try:
    get_product(catalog, "F999")

except KeyError:
    print("Example 24: Product not found.")


# EXAMPLE 25: Re-Raising an Exception
#
# A bare raise inside except
# re-raises the current exception.

def convert_required_number(value):
    try:
        return int(value)

    except ValueError:
        print("Example 25: Conversion logged.")
        raise


try:
    convert_required_number("invalid")

except ValueError:
    print("Example 25: Caller handled failure.")


# ==========================================
# SECTION 5 - CUSTOM EXCEPTIONS
# ==========================================


# EXAMPLE 26: Custom Exception Class
#
# Custom exceptions can describe
# application-specific problems.

class InvalidOrderError(Exception):
    pass


try:
    raise InvalidOrderError(
        "Order does not meet requirements."
    )

except InvalidOrderError as error:
    print("Example 26:", error)


# EXAMPLE 27: Inventory Exception

class InsufficientStockError(Exception):
    pass


def check_stock(available, requested):
    if requested > available:
        raise InsufficientStockError(
            "Not enough inventory."
        )

    return True


try:
    check_stock(5, 10)

except InsufficientStockError as error:
    print("Example 27:", error)


# EXAMPLE 28: Custom Exception Hierarchy

class FlowerOrderError(Exception):
    pass


class InvalidProductError(FlowerOrderError):
    pass


try:
    raise InvalidProductError(
        "Product is unavailable."
    )

except FlowerOrderError as error:
    print("Example 28:", error)


# EXAMPLE 29: Exception Chaining
#
# raise ... from ... connects
# a new error to its cause.

def parse_order_quantity(value):
    try:
        return int(value)

    except ValueError as error:
        raise InvalidOrderError(
            "Invalid order quantity."
        ) from error


try:
    parse_order_quantity("abc")

except InvalidOrderError as error:
    print("Example 29:", error)
    print(
        "Original error:",
        type(error.__cause__).__name__
    )


# EXAMPLE 30: Custom Error with Details

class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message

        super().__init__(
            f"{field}: {message}"
        )


try:
    raise ValidationError(
        "quantity",
        "Must be greater than zero."
    )

except ValidationError as error:
    print("Example 30:", error.field)
    print("Example 30:", error.message)


# ==========================================
# SECTION 6 - SAFE DATA PROCESSING
# ==========================================


# EXAMPLE 31: Handling Invalid List Values

values = ["10", "20", "invalid", "30"]

valid_numbers = []

for value in values:
    try:
        valid_numbers.append(int(value))

    except ValueError:
        print("Example 31: Skipped:", value)

print("Valid numbers:", valid_numbers)


# EXAMPLE 32: Counting Conversion Errors

values = ["5", "bad", "10", "wrong"]

error_count = 0

for value in values:
    try:
        int(value)

    except ValueError:
        error_count += 1

print("Example 32: Errors:", error_count)


# EXAMPLE 33: Separating Valid and Invalid

def separate_numbers(values):
    valid = []
    invalid = []

    for value in values:
        try:
            valid.append(int(value))

        except (ValueError, TypeError):
            invalid.append(value)

    return valid, invalid


numbers, rejected = separate_numbers(
    ["10", "abc", "25", None]
)

print("Example 33: Valid:", numbers)
print("Example 33: Invalid:", rejected)


# EXAMPLE 34: Safe Dictionary Access
#
# get() is often simpler than
# handling KeyError when a
# missing key is expected.

user = {
    "username": "alex"
}

role = user.get("role", "unknown")

print("Example 34: Role:", role)


# EXAMPLE 35: Safe List Access

def get_list_item(items, index):
    try:
        return items[index]

    except (IndexError, TypeError):
        return None


print(
    "Example 35:",
    get_list_item(["a", "b"], 5)
)


# EXAMPLE 36: Handling Nested Data

record = {
    "user": {
        "username": "alex"
    }
}

try:
    role = record["user"]["role"]

except KeyError:
    role = "unknown"

print("Example 36: Role:", role)


# EXAMPLE 37: Safe Float Conversion

def safe_float(value):
    try:
        return float(value)

    except (ValueError, TypeError, OverflowError):
        return None


print("Example 37:", safe_float("19.95"))
print("Example 37:", safe_float("invalid"))


# EXAMPLE 38: Rejecting Nonfinite Numbers
#
# float() accepts strings such as
# "nan" and "inf".
#
# These may be inappropriate
# for financial calculations.

import math


def parse_finite_float(value):
    result = safe_float(value)

    if result is None:
        return None

    if not math.isfinite(result):
        return None

    return result


print(
    "Example 38:",
    parse_finite_float("25.50")
)

print(
    "Example 38:",
    parse_finite_float("nan")
)


# EXAMPLE 39: Using Decimal for Money
#
# Decimal can avoid some
# binary floating-point
# representation issues.
#
# Real financial systems require
# explicit rounding and
# currency rules.

from decimal import Decimal, InvalidOperation


def parse_money(value):
    try:
        amount = Decimal(str(value))

    except (InvalidOperation, ValueError, TypeError):
        return None

    if not amount.is_finite():
        return None

    if amount < 0:
        return None

    return amount


print("Example 39:", parse_money("19.99"))
print("Example 39:", parse_money("invalid"))


# EXAMPLE 40: Safe File Reading
#
# File reading is covered
# in more detail on Day 27.

def read_text_file(path):
    try:
        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:
            return file.read()

    except FileNotFoundError:
        return None

    except PermissionError:
        return None


print(
    "Example 40:",
    read_text_file(
        "__day26_missing_example__.txt"
    )
)


# ==========================================
# SECTION 7 - BUSINESS APPLICATIONS
# ==========================================


# EXAMPLE 41: Flower Price Validation

def require_valid_price(price):
    amount = parse_money(price)

    if amount is None:
        raise ValueError(
            "Price must be a nonnegative amount."
        )

    return amount


try:
    price = require_valid_price("-25.00")

except ValueError as error:
    print("Example 41:", error)


# EXAMPLE 42: Flower Inventory Validation

def reserve_flowers(stock, quantity):
    validate_quantity(quantity)

    if quantity > stock:
        raise InsufficientStockError(
            "Requested quantity exceeds stock."
        )

    return stock - quantity


try:
    remaining = reserve_flowers(5, 8)

except InsufficientStockError as error:
    print("Example 42:", error)


# EXAMPLE 43: Safe Order Subtotal

def calculate_flower_subtotal(price, quantity):
    amount = require_valid_price(price)
    count = validate_quantity(quantity)

    return amount * count


try:
    subtotal = calculate_flower_subtotal(
        "75.00",
        2
    )

    print("Example 43:", subtotal)

except (TypeError, ValueError) as error:
    print("Example 43: Invalid order:", error)


# EXAMPLE 44: Processing Multiple Orders

sample_orders = [
    {
        "price": "75.00",
        "quantity": 2
    },
    {
        "price": "invalid",
        "quantity": 1
    },
    {
        "price": "65.00",
        "quantity": 3
    }
]

accepted_subtotals = []

for order in sample_orders:
    try:
        subtotal = calculate_flower_subtotal(
            order["price"],
            order["quantity"]
        )

    except (KeyError, TypeError, ValueError):
        print("Example 44: Order rejected.")
        continue

    accepted_subtotals.append(subtotal)

print(
    "Example 44: Accepted subtotals:",
    accepted_subtotals
)


# EXAMPLE 45: Order Result with Errors

def process_training_order(order):
    try:
        subtotal = calculate_flower_subtotal(
            order["price"],
            order["quantity"]
        )

    except KeyError:
        return {
            "accepted": False,
            "error": "Missing required field."
        }

    except (TypeError, ValueError):
        return {
            "accepted": False,
            "error": "Invalid price or quantity."
        }

    return {
        "accepted": True,
        "subtotal": subtotal
    }


print(
    "Example 45:",
    process_training_order({
        "price": "85.00",
        "quantity": 2
    })
)


# ==========================================
# SECTION 8 - CYBERSECURITY APPLICATIONS
# ==========================================


# EXAMPLE 46: Validating Network Ports

def parse_network_port(value):
    if isinstance(value, bool):
        raise TypeError(
            "Port cannot be Boolean."
        )

    if isinstance(value, int):
        port = value

    elif isinstance(value, str):
        cleaned = value.strip()

        if not cleaned.isascii():
            raise ValueError(
                "Port must use ASCII digits."
            )

        if not cleaned.isdecimal():
            raise ValueError(
                "Port must contain digits."
            )

        port = int(cleaned)

    else:
        raise TypeError(
            "Unsupported port type."
        )

    if not 1 <= port <= 65535:
        raise ValueError(
            "Port outside valid range."
        )

    return port


for value in ["22", "70000", "abc"]:
    try:
        port = parse_network_port(value)
        print("Example 46: Valid port:", port)

    except (TypeError, ValueError) as error:
        print("Example 46:", error)


# EXAMPLE 47: Validating IP Addresses

import ipaddress


def parse_ip_address(value):
    if not isinstance(value, str):
        raise TypeError(
            "IP address must be a string."
        )

    try:
        return ipaddress.ip_address(value)

    except ValueError as error:
        raise ValueError(
            "Invalid IP address syntax."
        ) from error


for address in [
    "192.0.2.10",
    "999.999.999.999"
]:
    try:
        parsed = parse_ip_address(address)
        print("Example 47:", parsed)

    except (TypeError, ValueError) as error:
        print("Example 47:", error)


# EXAMPLE 48: Handling Malformed Security Events
#
# All records are synthetic.
#
# Documentation IP addresses
# are used in sample data.

def validate_security_event(event):
    if not isinstance(event, dict):
        raise TypeError(
            "Event must be a dictionary."
        )

    required = {
        "event_type",
        "source_ip",
        "severity"
    }

    missing = required - event.keys()

    if missing:
        raise ValueError(
            "Security event missing fields."
        )

    allowed_types = {
        "login_success",
        "login_failed",
        "port_scan",
        "file_access"
    }

    allowed_severities = {
        "low",
        "medium",
        "high"
    }

    if event["event_type"] not in allowed_types:
        raise ValueError(
            "Unsupported event type."
        )

    if event["severity"] not in allowed_severities:
        raise ValueError(
            "Unsupported severity."
        )

    parse_ip_address(event["source_ip"])

    return True


security_events = [
    {
        "event_type": "login_failed",
        "source_ip": "192.0.2.10",
        "severity": "high"
    },
    {
        "event_type": "port_scan",
        "source_ip": "invalid-ip",
        "severity": "medium"
    }
]

for event in security_events:
    try:
        validate_security_event(event)

    except (TypeError, ValueError) as error:
        print("Example 48: Rejected:", error)

    else:
        print("Example 48: Event accepted.")


# EXAMPLE 49: Safe Security Event Processing
#
# Separate valid and invalid
# records without losing track
# of rejected events.

def process_security_events(events):
    accepted = []
    rejected = []

    for index, event in enumerate(events, start=1):
        try:
            validate_security_event(event)

        except (TypeError, ValueError) as error:
            rejected.append({
                "record_number": index,
                "error": str(error)
            })

        else:
            accepted.append(event.copy())

    return {
        "accepted": accepted,
        "rejected": rejected,
        "accepted_count": len(accepted),
        "rejected_count": len(rejected)
    }


report = process_security_events(
    security_events
)

print("Example 49: Accepted:", report["accepted_count"])
print("Example 49: Rejected:", report["rejected_count"])


# EXAMPLE 50: COMPLETE ERROR HANDLING REPORT
#
# This example combines:
#
# Custom exceptions
# try/except/else/finally
# Input validation
# Structured records
# Safe conversions
# Error reporting
# Functions
# Return values
# Loops
#
# All data is synthetic.


class SecurityRecordError(Exception):
    pass


def require_security_record(event):
    try:
        validate_security_event(event)

    except (TypeError, ValueError) as error:
        raise SecurityRecordError(
            "Invalid security record."
        ) from error

    return event


def analyze_security_records(events):
    accepted = []
    rejected = []
    failed_logins = 0

    for index, event in enumerate(events, start=1):
        try:
            valid_event = require_security_record(
                event
            )

        except SecurityRecordError as error:
            rejected.append({
                "record_number": index,
                "reason": str(error)
            })

        else:
            accepted.append(valid_event.copy())

            if valid_event["event_type"] == "login_failed":
                failed_logins += 1

        finally:
            print(
                "Example 50: Processed record",
                index
            )

    return {
        "total_received": len(events),
        "accepted_count": len(accepted),
        "rejected_count": len(rejected),
        "failed_logins": failed_logins,
        "accepted_events": accepted,
        "rejected_events": rejected
    }


def display_security_report(report):
    print("\n===== SECURITY EVENT REPORT =====")

    print(
        "Total received:",
        report["total_received"]
    )

    print(
        "Accepted:",
        report["accepted_count"]
    )

    print(
        "Rejected:",
        report["rejected_count"]
    )

    print(
        "Failed logins:",
        report["failed_logins"]
    )

    print("\nRejected records:")

    for rejected in report["rejected_events"]:
        print(
            "Record:",
            rejected["record_number"],
            "-",
            rejected["reason"]
        )


training_events = [
    {
        "event_type": "login_failed",
        "source_ip": "198.51.100.10",
        "severity": "high"
    },
    {
        "event_type": "login_success",
        "source_ip": "192.0.2.15",
        "severity": "low"
    },
    {
        "event_type": "port_scan",
        "source_ip": "203.0.113.5",
        "severity": "medium"
    },
    {
        "event_type": "unknown",
        "source_ip": "192.0.2.25",
        "severity": "high"
    },
    {
        "event_type": "file_access",
        "source_ip": "invalid-ip",
        "severity": "low"
    }
]

security_report = analyze_security_records(
    training_events
)

display_security_report(security_report)


# ==========================================
# WHAT I LEARNED
# ==========================================
#
# 1. Exceptions represent runtime problems.
# 2. Syntax errors prevent parsing.
# 3. try contains potentially failing code.
# 4. except handles expected exceptions.
# 5. ValueError represents invalid values.
# 6. TypeError represents type problems.
# 7. ZeroDivisionError handles division by zero.
# 8. IndexError handles invalid list indices.
# 9. KeyError handles missing dictionary keys.
# 10. FileNotFoundError handles missing files.
# 11. AttributeError handles missing attributes.
# 12. Multiple except blocks are supported.
# 13. Exception classes can be grouped.
# 14. Exception objects contain information.
# 15. Functions can handle errors.
# 16. Functions can return error results.
# 17. else runs after successful try blocks.
# 18. finally runs during cleanup.
# 19. raise explicitly triggers exceptions.
# 20. Exceptions can be re-raised.
# 21. Custom exception classes are possible.
# 22. Exception inheritance organizes errors.
# 23. Exception chaining preserves causes.
# 24. Error objects can contain details.
# 25. Loops can continue after bad records.
# 26. Invalid records can be counted.
# 27. Valid and invalid data can be separated.
# 28. get() can handle expected missing keys.
# 29. Numeric conversions may fail.
# 30. Nonfinite numbers require attention.
# 31. Decimal supports decimal arithmetic.
# 32. File operations may raise exceptions.
# 33. Flower orders need error handling.
# 34. Inventory errors can be represented.
# 35. Security event records need validation.
# 36. Malformed events should be tracked.
# 37. Error reports support troubleshooting.
# 38. Specific exceptions are preferable.
# 39. Sensitive details should be protected.
# 40. Error handling improves reliability.
