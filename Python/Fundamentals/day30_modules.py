
# ==========================================
# DAY 30 - PYTHON MODULES
# Topic: Imports and Reusable Code
# ==========================================

# LESSON NOTES
#
# A module is usually a Python file
# containing reusable code.
#
# Modules can contain:
#
# Variables
# Functions
# Classes
# Constants
# Executable statements
#
# A package organizes modules
# under a common import path.
#
# IMPORT EXAMPLES:
#
# import math
# from math import sqrt
# import math as m
# from math import sqrt as square_root
#
# MODULE NAMESPACES:
#
# math.sqrt(25)
#
# The dot accesses a name
# defined inside the module.
#
# MAIN GUARD:
#
# if __name__ == "__main__":
#
# Code inside the main guard runs
# when a file is executed directly,
# not during an ordinary import.
#
# IMPORTANT:
#
# Python executes module-level code
# during the first normal import.
#
# Modules are generally cached
# in sys.modules.
#
# Imports can fail if modules
# are unavailable.
#
# Never import untrusted code.
#
# Avoid naming your own files:
#
# math.py
# json.py
# csv.py
# random.py
#
# These names may shadow
# standard library modules.
#
# Avoid wildcard imports.
#
# Use descriptive module names.
#
# All security and business
# information below is fictional.


# ==========================================
# SECTION 1 - IMPORTS
# ==========================================

import math
import random
import statistics
import json
import csv
import sys
import os
import importlib
import io

from pathlib import Path
from tempfile import TemporaryDirectory
from collections import Counter
from decimal import Decimal
from datetime import datetime
from functools import reduce
from operator import mul


# ==========================================
# SECTION 2 - BASIC MODULE IMPORTS
# ==========================================

def run_lesson(folder):

    base = Path(folder)

    # EXAMPLE 1: Import a Module

    print(
        "Example 1:",
        math.sqrt(64)
    )


    # EXAMPLE 2: Module Constants

    print(
        "Example 2:",
        math.pi
    )


    # EXAMPLE 3: Another Module Function

    print(
        "Example 3:",
        math.factorial(5)
    )


    # EXAMPLE 4: Import Specific Function

    from math import ceil

    print(
        "Example 4:",
        ceil(4.2)
    )


    # EXAMPLE 5: Import Multiple Names

    from math import floor, trunc

    print(
        "Example 5:",
        floor(4.9),
        trunc(-4.9)
    )


    # EXAMPLE 6: Module Alias

    import math as m

    print(
        "Example 6:",
        m.sqrt(81)
    )


    # EXAMPLE 7: Function Alias

    from math import sqrt as square_root

    print(
        "Example 7:",
        square_root(49)
    )


    # EXAMPLE 8: Module Namespace

    print(
        "Example 8:",
        math.pow(2, 3)
    )


    # EXAMPLE 9: Check Module Name

    print(
        "Example 9:",
        math.__name__
    )


    # EXAMPLE 10: Inspect Module Names

    math_names = dir(math)

    print(
        "Example 10:",
        "sqrt" in math_names
    )


    # ======================================
    # SECTION 3 - STANDARD LIBRARY MODULES
    # ======================================

    # EXAMPLE 11: Random Module
    #
    # This is for simulation.
    # random is not suitable
    # for generating secrets.

    generator = random.Random(30)

    print(
        "Example 11:",
        generator.randint(1, 10)
    )


    # EXAMPLE 12: Statistics Module

    values = [10, 20, 30, 40, 50]

    print(
        "Example 12:",
        statistics.mean(values)
    )


    # EXAMPLE 13: Median

    print(
        "Example 13:",
        statistics.median(values)
    )


    # EXAMPLE 14: JSON Module

    settings = {
        "logging": True,
        "environment": "lab"
    }

    json_text = json.dumps(settings)

    print(
        "Example 14:",
        json_text
    )


    # EXAMPLE 15: Parse JSON

    parsed_settings = json.loads(
        json_text
    )

    print(
        "Example 15:",
        parsed_settings["environment"]
    )


    # EXAMPLE 16: Counter Module

    events = [
        "LOGIN_FAILED",
        "LOGIN_FAILED",
        "PORT_SCAN",
        "LOGIN_SUCCESS"
    ]

    counts = Counter(events)

    print(
        "Example 16:",
        dict(counts)
    )


    # EXAMPLE 17: Decimal Module

    price = Decimal("75.00")

    quantity = 3

    print(
        "Example 17:",
        price * quantity
    )


    # EXAMPLE 18: Datetime Module

    timestamp = datetime(
        2026, 11, 11, 10, 30
    )

    print(
        "Example 18:",
        timestamp.isoformat()
    )


    # EXAMPLE 19: pathlib Module

    report_path = (
        base / "training_report.txt"
    )

    report_path.write_text(
        "Synthetic training report",
        encoding="utf-8"
    )

    print(
        "Example 19:",
        report_path.exists()
    )


    # EXAMPLE 20: CSV Module

    buffer = io.StringIO(
        newline=""
    )

    writer = csv.writer(buffer)

    writer.writerow([
        "event",
        "severity"
    ])

    writer.writerow([
        "PORT_SCAN",
        "MEDIUM"
    ])

    print(
        "Example 20:",
        buffer.getvalue().strip()
    )


    # ======================================
    # SECTION 4 - MODULE INFORMATION
    # ======================================

    # EXAMPLE 21: Module Documentation

    print(
        "Example 21:",
        bool(math.__doc__)
    )


    # EXAMPLE 22: Module File Location
    #
    # Not every module has __file__.
    # Built-in modules may not
    # have a source file path.

    print(
        "Example 22:",
        getattr(
            json,
            "__file__",
            None
        )
    )


    # EXAMPLE 23: Module Dictionary

    print(
        "Example 23:",
        "sqrt" in math.__dict__
    )


    # EXAMPLE 24: Module Attributes

    print(
        "Example 24:",
        hasattr(math, "sqrt")
    )


    # EXAMPLE 25: getattr()

    function = getattr(
        math,
        "sqrt"
    )

    print(
        "Example 25:",
        function(100)
    )


    # EXAMPLE 26: Inspect Loaded Modules

    print(
        "Example 26:",
        "math" in sys.modules
    )


    # EXAMPLE 27: sys.version_info

    print(
        "Example 27:",
        sys.version_info.major,
        sys.version_info.minor
    )


    # EXAMPLE 28: sys.path
    #
    # Python searches import
    # locations listed in sys.path.

    print(
        "Example 28:",
        len(sys.path) > 0
    )


    # EXAMPLE 29: Module Availability

    import importlib.util

    specification = (
        importlib.util.find_spec("json")
    )

    print(
        "Example 29:",
        specification is not None
    )


    # EXAMPLE 30: Import Error Handling

    try:
        import module_that_does_not_exist_30

    except ModuleNotFoundError:
        print(
            "Example 30:",
            "Module not available."
        )


    # ======================================
    # SECTION 5 - CUSTOM MODULES
    # ======================================

    # The following examples create
    # temporary Python modules.
    #
    # They demonstrate how separate
    # files can work together.
    #
    # The temporary folder is added
    # to sys.path for this lesson.
    #
    # Only locally generated,
    # trusted training code is used.

    module_folder = base / "modules"

    module_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    # Unique names help avoid
    # collisions with other modules.

    helper_path = (
        module_folder
        / "day30_flower_helpers.py"
    )

    helper_path.write_text(
        '''
BUSINESS_NAME = "Golden Aura Florals"

def calculate_subtotal(price, quantity):
    return price * quantity

def format_product(name):
    return name.strip().title()

def inventory_available(stock, requested):
    return requested > 0 and stock >= requested
'''.strip() + "\n",
        encoding="utf-8"
    )

    sys.path.insert(
        0,
        str(module_folder)
    )

    # EXAMPLE 31: Import Custom Module

    import day30_flower_helpers

    print(
        "Example 31:",
        day30_flower_helpers.BUSINESS_NAME
    )


    # EXAMPLE 32: Custom Function

    subtotal = (
        day30_flower_helpers.calculate_subtotal(
            75,
            2
        )
    )

    print(
        "Example 32:",
        subtotal
    )


    # EXAMPLE 33: Another Custom Function

    product_name = (
        day30_flower_helpers.format_product(
            "  rose bouquet  "
        )
    )

    print(
        "Example 33:",
        product_name
    )


    # EXAMPLE 34: Custom Validation

    available = (
        day30_flower_helpers.inventory_available(
            10,
            3
        )
    )

    print(
        "Example 34:",
        available
    )


    # EXAMPLE 35: Import Specific Name

    from day30_flower_helpers import (
        calculate_subtotal
    )

    print(
        "Example 35:",
        calculate_subtotal(95, 2)
    )


    # EXAMPLE 36: Alias Custom Function

    from day30_flower_helpers import (
        format_product as clean_name
    )

    print(
        "Example 36:",
        clean_name("  luxury bouquet ")
    )


    # EXAMPLE 37: Custom Module Namespace

    print(
        "Example 37:",
        "inventory_available"
        in dir(day30_flower_helpers)
    )


    # EXAMPLE 38: Cached Module

    imported_again = (
        importlib.import_module(
            "day30_flower_helpers"
        )
    )

    print(
        "Example 38:",
        imported_again is day30_flower_helpers
    )


    # EXAMPLE 39: Module Main Guard

    guard_path = (
        module_folder
        / "day30_guard_demo.py"
    )

    guard_path.write_text(
        '''
def greet():
    return "Hello from the module"

if __name__ == "__main__":
    print("Executed directly")
'''.strip() + "\n",
        encoding="utf-8"
    )

    import day30_guard_demo

    print(
        "Example 39:",
        day30_guard_demo.greet()
    )

    # The main-guard print statement
    # does not run during import.


    # EXAMPLE 40: Reload a Module
    #
    # Reloading re-executes the
    # module's top-level code.
    #
    # It is not a substitute for
    # restarting a complex program.

    reloaded = importlib.reload(
        day30_flower_helpers
    )

    print(
        "Example 40:",
        reloaded.BUSINESS_NAME
    )


    # ======================================
    # SECTION 6 - PACKAGES
    # ======================================

    package_folder = (
        module_folder / "day30_security_tools"
    )

    package_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    init_path = (
        package_folder / "__init__.py"
    )

    init_path.write_text(
        '''
PACKAGE_NAME = "Security Training Tools"
'''.strip() + "\n",
        encoding="utf-8"
    )

    validator_path = (
        package_folder / "validators.py"
    )

    validator_path.write_text(
        '''
from ipaddress import ip_address

def valid_ip(address):
    try:
        ip_address(address)
        return True
    except (ValueError, TypeError):
        return False

def valid_severity(value):
    return value in {
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    }
'''.strip() + "\n",
        encoding="utf-8"
    )

    analyzer_path = (
        package_folder / "analyzers.py"
    )

    analyzer_path.write_text(
        '''
from collections import Counter

def count_events(events):
    return dict(Counter(events))

def count_failed_logins(events):
    return sum(
        event == "LOGIN_FAILED"
        for event in events
    )
'''.strip() + "\n",
        encoding="utf-8"
    )

    # EXAMPLE 41: Import Package

    import day30_security_tools

    print(
        "Example 41:",
        day30_security_tools.PACKAGE_NAME
    )


    # EXAMPLE 42: Import Submodule

    from day30_security_tools import validators

    print(
        "Example 42:",
        validators.valid_ip(
            "192.0.2.10"
        )
    )


    # EXAMPLE 43: Package Function

    print(
        "Example 43:",
        validators.valid_severity(
            "HIGH"
        )
    )


    # EXAMPLE 44: Import Another Submodule

    from day30_security_tools import analyzers

    print(
        "Example 44:",
        analyzers.count_events(
            events
        )
    )


    # EXAMPLE 45: Reuse Analysis Function

    print(
        "Example 45:",
        analyzers.count_failed_logins(
            events
        )
    )


    # EXAMPLE 46: Import Nested Function

    from day30_security_tools.validators import (
        valid_ip
    )

    print(
        "Example 46:",
        valid_ip("203.0.113.5")
    )


    # EXAMPLE 47: Package Namespace

    print(
        "Example 47:",
        validators.__name__
    )


    # EXAMPLE 48: Inspect Package Path

    print(
        "Example 48:",
        list(
            day30_security_tools.__path__
        )
    )


    # EXAMPLE 49: Combine Modules

    sample_events = [
        {
            "source_ip": "192.0.2.10",
            "event_type": "LOGIN_FAILED",
            "severity": "HIGH"
        },
        {
            "source_ip": "203.0.113.5",
            "event_type": "PORT_SCAN",
            "severity": "MEDIUM"
        },
        {
            "source_ip": "198.51.100.20",
            "event_type": "LOGIN_SUCCESS",
            "severity": "LOW"
        }
    ]

    valid_events = [
        event
        for event in sample_events
        if validators.valid_ip(
            event["source_ip"]
        )
        and validators.valid_severity(
            event["severity"]
        )
    ]

    event_types = [
        event["event_type"]
        for event in valid_events
    ]

    print(
        "Example 49:",
        analyzers.count_events(
            event_types
        )
    )


    # ======================================
    # EXAMPLE 50 - MODULAR SECURITY
    # EVENT ANALYSIS SYSTEM
    # ======================================

    # This example uses multiple
    # custom modules to:
    #
    # Validate security events
    # Count event types
    # Count failed logins
    # Generate a summary
    # Export a JSON report
    #
    # All data is synthetic.

    training_events = [
        {
            "source_ip": "192.0.2.10",
            "event_type": "LOGIN_FAILED",
            "severity": "HIGH"
        },
        {
            "source_ip": "192.0.2.10",
            "event_type": "LOGIN_FAILED",
            "severity": "HIGH"
        },
        {
            "source_ip": "198.51.100.20",
            "event_type": "LOGIN_SUCCESS",
            "severity": "LOW"
        },
        {
            "source_ip": "203.0.113.5",
            "event_type": "PORT_SCAN",
            "severity": "MEDIUM"
        },
        {
            "source_ip": "invalid-ip",
            "event_type": "PORT_SCAN",
            "severity": "HIGH"
        }
    ]


    def validate_event(event):
        if not isinstance(event, dict):
            return False

        required = {
            "source_ip",
            "event_type",
            "severity"
        }

        if not required.issubset(
            event.keys()
        ):
            return False

        if not all(
            isinstance(event[key], str)
            for key in required
        ):
            return False

        if not validators.valid_ip(
            event["source_ip"]
        ):
            return False

        if not validators.valid_severity(
            event["severity"]
        ):
            return False

        return event["event_type"] in {
            "LOGIN_FAILED",
            "LOGIN_SUCCESS",
            "PORT_SCAN",
            "FILE_ACCESS"
        }


    def analyze_records(records):
        accepted = [
            event.copy()
            for event in records
            if validate_event(event)
        ]

        rejected_count = (
            len(records) - len(accepted)
        )

        types = [
            event["event_type"]
            for event in accepted
        ]

        return {
            "total": len(records),
            "accepted": len(accepted),
            "rejected": rejected_count,
            "event_counts": (
                analyzers.count_events(
                    types
                )
            ),
            "failed_logins": (
                analyzers.count_failed_logins(
                    types
                )
            ),
            "unique_ips": sorted({
                event["source_ip"]
                for event in accepted
            })
        }


    def save_report(report, path):
        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )


    final_report = analyze_records(
        training_events
    )

    final_path = (
        base / "modular_security_report.json"
    )

    save_report(
        final_report,
        final_path
    )

    print(
        "\nExample 50:",
        json.dumps(
            final_report,
            indent=4
        )
    )

    print(
        "Report saved:",
        final_path.exists()
    )

    # Remove the temporary directory
    # from the import search path.
    #
    # This does not unload modules
    # from sys.modules.

    sys.path.remove(
        str(module_folder)
    )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    with TemporaryDirectory(
        prefix="day30_modules_"
    ) as training_folder:

        run_lesson(training_folder)


# ==========================================
# WHAT I LEARNED
# ==========================================
#
# 1. Modules organize reusable code.
# 2. import loads a module.
# 3. from imports specific names.
# 4. as creates import aliases.
# 5. Modules have namespaces.
# 6. Module constants can be accessed.
# 7. Modules can contain functions.
# 8. Modules can contain classes.
# 9. Module names can be inspected.
# 10. dir() lists module attributes.
# 11. Standard library modules exist.
# 12. random supports simulations.
# 13. statistics supports analysis.
# 14. json handles structured data.
# 15. csv handles tabular data.
# 16. Counter counts occurrences.
# 17. Decimal supports money values.
# 18. datetime handles dates.
# 19. pathlib handles paths.
# 20. io supports memory streams.
# 21. Modules contain documentation.
# 22. __file__ may show a source path.
# 23. __dict__ stores module names.
# 24. hasattr() checks attributes.
# 25. getattr() retrieves attributes.
# 26. sys.modules caches imports.
# 27. sys.version_info shows version.
# 28. sys.path lists import locations.
# 29. find_spec() checks availability.
# 30. Imports may raise errors.
# 31. Custom Python files are modules.
# 32. Custom functions can be reused.
# 33. Modules can contain constants.
# 34. Validation functions can be shared.
# 35. Specific functions can be imported.
# 36. Custom functions can be aliased.
# 37. Modules have separate namespaces.
# 38. Imports normally use a cache.
# 39. Main guards control execution.
# 40. importlib.reload() re-executes code.
# 41. Packages organize modules.
# 42. __init__.py initializes packages.
# 43. Submodules can be imported.
# 44. Package functions can be reused.
# 45. Analysis functions can be shared.
# 46. Nested import paths are supported.
# 47. Packages have namespaces.
# 48. Packages have search paths.
# 49. Multiple modules can cooperate.
# 50. Modular design supports
#     cybersecurity and business tools.
