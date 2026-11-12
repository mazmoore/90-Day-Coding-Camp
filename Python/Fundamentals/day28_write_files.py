
# ==========================================
# DAY 28 - WRITING FILES
# Topic: File Output and Data Persistence
# ==========================================

# LESSON NOTES
#
# Writing files allows Python programs
# to save information outside memory.
#
# File writing is useful for:
#
# Business records
# Inventory records
# Application reports
# Security investigation summaries
# Configuration files
# Log files
# Data exports
#
# FILE MODES:
#
# "w"  = Write, replacing existing data.
# "a"  = Append to the end of a file.
# "x"  = Create only if file is absent.
# "w+" = Write and read; truncates file.
# "a+" = Append and read.
# "wb" = Write binary data.
#
# IMPORTANT:
#
# "w" can erase existing file contents.
#
# "a" preserves existing contents.
#
# "x" raises FileExistsError when
# the file already exists.
#
# COMMON METHODS:
#
# write()
# writelines()
# flush()
# seek()
# read()
#
# BEST PRACTICES:
#
# Use context managers.
# Specify text encoding.
# Handle expected exceptions.
# Validate data before saving.
# Avoid storing passwords in plaintext.
# Avoid recording sensitive information.
# Use safe, controlled file paths.
# Avoid overwriting important files.
# Consider atomic replacement when
# updating important application data.
#
# All examples use synthetic data.


# ==========================================
# SECTION 1 - IMPORTS AND SETUP
# ==========================================

from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime
from collections import Counter
import json
import os


def run_lesson(folder):

    base = Path(folder)

    # All training files are stored
    # inside the temporary directory.

    # ======================================
    # SECTION 2 - BASIC FILE WRITING
    # ======================================

    # EXAMPLE 1: Create a Text File

    path = base / "example01.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("Hello, Python!")

    print("Example 1:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 2: Write Multiple Lines

    path = base / "example02.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("First line\n")
        file.write("Second line\n")
        file.write("Third line\n")

    print("Example 2:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 3: Overwrite Existing Data

    path = base / "example03.txt"

    path.write_text(
        "Original content",
        encoding="utf-8"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("Replacement content")

    print("Example 3:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 4: Append to a File

    path = base / "example04.txt"

    path.write_text(
        "First entry\n",
        encoding="utf-8"
    )

    with open(
        path,
        "a",
        encoding="utf-8"
    ) as file:
        file.write("Second entry\n")

    print("Example 4:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 5: Append Multiple Entries

    path = base / "example05.txt"

    with open(
        path,
        "a",
        encoding="utf-8"
    ) as file:
        file.write("Entry A\n")
        file.write("Entry B\n")
        file.write("Entry C\n")

    print("Example 5:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 6: Exclusive Creation

    path = base / "example06.txt"

    with open(
        path,
        "x",
        encoding="utf-8"
    ) as file:
        file.write("Created safely.")

    print("Example 6:", path.exists())


    # EXAMPLE 7: Handle Existing File

    try:
        with open(
            path,
            "x",
            encoding="utf-8"
        ) as file:
            file.write("New content")

    except FileExistsError:
        print(
            "Example 7: File already exists."
        )


    # EXAMPLE 8: writelines()

    path = base / "example08.txt"

    lines = [
        "Rose Bouquet\n",
        "Tulip Arrangement\n",
        "Luxury Arrangement\n"
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.writelines(lines)

    print("Example 8:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 9: writelines() Does Not
    # Automatically Add Newlines

    path = base / "example09.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.writelines([
            "Rose",
            "Tulip",
            "Orchid"
        ])

    print("Example 9:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 10: Write a Variable

    path = base / "example10.txt"

    flower_name = "Sunflower Bouquet"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(flower_name)

    print("Example 10:", path.read_text(
        encoding="utf-8"
    ))


    # ======================================
    # SECTION 3 - FORMATTING FILE OUTPUT
    # ======================================

    # EXAMPLE 11: Write Numbers as Text

    path = base / "example11.txt"

    quantity = 12

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(str(quantity))

    print("Example 11:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 12: Write f-Strings

    path = base / "example12.txt"

    product = "Rose Bouquet"
    price = 75.00

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            f"{product}: ${price:.2f}\n"
        )

    print("Example 12:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 13: Write List Items

    path = base / "example13.txt"

    flowers = [
        "Roses",
        "Tulips",
        "Orchids"
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for flower in flowers:
            file.write(flower + "\n")

    print("Example 13:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 14: Write Dictionary Values

    path = base / "example14.txt"

    product = {
        "name": "Luxury Bouquet",
        "price": 125.00,
        "quantity": 3
    }

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for key, value in product.items():
            file.write(
                f"{key}: {value}\n"
            )

    print("Example 14:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 15: Write Numbered Lines

    path = base / "example15.txt"

    products = [
        "Rose Bouquet",
        "Tulip Arrangement",
        "Orchid Arrangement"
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for number, product in enumerate(
            products,
            start=1
        ):
            file.write(
                f"{number}. {product}\n"
            )

    print("Example 15:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 16: Write a Header

    path = base / "example16.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            "GOLDEN AURA FLORALS\n"
        )
        file.write(
            "Inventory Report\n"
        )
        file.write(
            "================\n"
        )

    print("Example 16:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 17: Write a Timestamp

    path = base / "example17.txt"

    timestamp = datetime(
        2026, 11, 11, 14, 30
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            timestamp.isoformat()
        )

    print("Example 17:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 18: Write Unicode Text

    path = base / "example18.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            "Rosé Arrangement 🌸\n"
        )

    print("Example 18:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 19: Write Empty Content

    path = base / "example19.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("")

    print(
        "Example 19: File size:",
        path.stat().st_size
    )


    # EXAMPLE 20: Write Joined Strings

    path = base / "example20.txt"

    items = [
        "Rose",
        "Tulip",
        "Orchid"
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            "\n".join(items) + "\n"
        )

    print("Example 20:", path.read_text(
        encoding="utf-8"
    ))


    # ======================================
    # SECTION 4 - PATHLIB AND DIRECTORIES
    # ======================================

    # EXAMPLE 21: Path.write_text()

    path = base / "example21.txt"

    path.write_text(
        "Written using pathlib.",
        encoding="utf-8"
    )

    print("Example 21:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 22: Path.write_bytes()

    path = base / "example22.bin"

    path.write_bytes(
        b"Binary training data"
    )

    print(
        "Example 22:",
        path.read_bytes()
    )


    # EXAMPLE 23: Create a Directory

    reports = base / "reports"

    reports.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        "Example 23:",
        reports.is_dir()
    )


    # EXAMPLE 24: Write Inside a Directory

    path = reports / "summary.txt"

    path.write_text(
        "Training report created.",
        encoding="utf-8"
    )

    print("Example 24:", path.exists())


    # EXAMPLE 25: Check Before Writing
    #
    # This illustrates an existence
    # check, not an atomic guarantee.
    #
    # Use exclusive creation ("x")
    # when the file must not exist.

    path = base / "example25.txt"

    if not path.exists():
        path.write_text(
            "First version",
            encoding="utf-8"
        )

    print("Example 25:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 26: Write and Read Mode

    path = base / "example26.txt"

    with open(
        path,
        "w+",
        encoding="utf-8"
    ) as file:
        file.write("Read and write example.")

        file.seek(0)

        content = file.read()

    print("Example 26:", content)


    # EXAMPLE 27: Append and Read Mode

    path = base / "example27.txt"

    path.write_text(
        "First line\n",
        encoding="utf-8"
    )

    with open(
        path,
        "a+",
        encoding="utf-8"
    ) as file:
        file.write("Second line\n")

        file.seek(0)

        content = file.read()

    print("Example 27:", content)


    # EXAMPLE 28: flush()
    #
    # flush() sends buffered
    # Python output to the
    # underlying file object.
    #
    # It does not guarantee
    # durable disk storage.

    path = base / "example28.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("Buffered output.")
        file.flush()

        print(
            "Example 28:",
            path.read_text(
                encoding="utf-8"
            )
        )


    # EXAMPLE 29: Verify File Contents

    path = base / "example29.txt"

    expected = "Verified content"

    path.write_text(
        expected,
        encoding="utf-8"
    )

    actual = path.read_text(
        encoding="utf-8"
    )

    print(
        "Example 29:",
        actual == expected
    )


    # EXAMPLE 30: Handle Write Errors

    invalid_path = (
        base / "missing_directory" / "file.txt"
    )

    try:
        invalid_path.write_text(
            "Training data",
            encoding="utf-8"
        )

    except FileNotFoundError:
        print(
            "Example 30: Parent directory missing."
        )


    # ======================================
    # SECTION 5 - STRUCTURED DATA
    # ======================================

    # EXAMPLE 31: Save JSON Dictionary

    path = base / "example31.json"

    settings = {
        "application": "training_monitor",
        "logging": True,
        "environment": "lab"
    }

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            settings,
            file,
            indent=4
        )

    print("Example 31:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 32: Save JSON List

    path = base / "example32.json"

    events = [
        {
            "event": "LOGIN_FAILED",
            "source_ip": "192.0.2.10"
        },
        {
            "event": "PORT_SCAN",
            "source_ip": "203.0.113.5"
        }
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            events,
            file,
            indent=4
        )

    print(
        "Example 32:",
        json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )
    )


    # EXAMPLE 33: JSON Unicode Support

    path = base / "example33.json"

    data = {
        "product": "Rosé Bouquet 🌸"
    }

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("Example 33:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 34: Save Key-Value Settings

    path = base / "example34.txt"

    configuration = {
        "environment": "lab",
        "logging": "enabled",
        "mode": "training"
    }

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for key, value in configuration.items():
            file.write(
                f"{key}={value}\n"
            )

    print("Example 34:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 35: Save a Summary

    path = base / "example35.txt"

    event_counts = {
        "LOGIN_FAILED": 4,
        "LOGIN_SUCCESS": 2,
        "PORT_SCAN": 1
    }

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("SECURITY SUMMARY\n")

        for event, count in event_counts.items():
            file.write(
                f"{event}: {count}\n"
            )

    print("Example 35:", path.read_text(
        encoding="utf-8"
    ))


    # ======================================
    # SECTION 6 - FLOWER BUSINESS APPLICATIONS
    # ======================================

    # EXAMPLE 36: Save Flower Inventory

    path = base / "example36.txt"

    inventory = {
        "Roses": 25,
        "Tulips": 15,
        "Orchids": 10
    }

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for flower, quantity in inventory.items():
            file.write(
                f"{flower}: {quantity}\n"
            )

    print("Example 36:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 37: Append Inventory Activity

    path = base / "example37.log"

    path.write_text(
        "Inventory activity\n",
        encoding="utf-8"
    )

    with open(
        path,
        "a",
        encoding="utf-8"
    ) as file:
        file.write(
            "Added 10 roses\n"
        )

    print("Example 37:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 38: Save Order Summary

    path = base / "example38.txt"

    order = {
        "order_id": "TRAINING-001",
        "product": "Luxury Bouquet",
        "quantity": 2,
        "unit_price": 125.00
    }

    subtotal = (
        order["quantity"]
        * order["unit_price"]
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            f"Order: {order['order_id']}\n"
        )
        file.write(
            f"Product: {order['product']}\n"
        )
        file.write(
            f"Quantity: {order['quantity']}\n"
        )
        file.write(
            f"Subtotal: ${subtotal:.2f}\n"
        )

    print("Example 38:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 39: Save Multiple Orders

    path = base / "example39.json"

    orders = [
        {
            "order_id": "TRAINING-001",
            "total": 125.00
        },
        {
            "order_id": "TRAINING-002",
            "total": 75.00
        }
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            orders,
            file,
            indent=4
        )

    print(
        "Example 39:",
        len(orders),
        "orders saved."
    )


    # EXAMPLE 40: Generate Sales Report

    path = base / "example40.txt"

    sales = [
        125.00,
        75.00,
        150.00
    ]

    total_sales = sum(sales)

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            "GOLDEN AURA FLORALS\n"
        )
        file.write(
            "Training Sales Report\n"
        )
        file.write(
            f"Orders: {len(sales)}\n"
        )
        file.write(
            f"Total: ${total_sales:.2f}\n"
        )

    print("Example 40:", path.read_text(
        encoding="utf-8"
    ))


    # ======================================
    # SECTION 7 - CYBERSECURITY APPLICATIONS
    # ======================================

    # EXAMPLE 41: Save Security Event

    path = base / "example41.log"

    event = (
        "2026-11-11|192.0.2.10|"
        "LOGIN_FAILED|HIGH"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(event + "\n")

    print("Example 41:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 42: Append Security Events

    path = base / "example42.log"

    events = [
        "2026-11-11|192.0.2.10|LOGIN_FAILED|HIGH",
        "2026-11-11|198.51.100.20|LOGIN_SUCCESS|LOW",
        "2026-11-11|203.0.113.5|PORT_SCAN|MEDIUM"
    ]

    with open(
        path,
        "a",
        encoding="utf-8"
    ) as file:
        for event in events:
            file.write(event + "\n")

    print("Example 42:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 43: Write Filtered Events

    path = base / "example43.log"

    suspicious = [
        event
        for event in events
        if "LOGIN_FAILED" in event
        or "PORT_SCAN" in event
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for event in suspicious:
            file.write(event + "\n")

    print("Example 43:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 44: Save Event Counts

    path = base / "example44.txt"

    counts = Counter()

    for event in events:
        fields = event.split("|")

        if len(fields) == 4:
            counts[fields[2]] += 1

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for event_type, count in counts.items():
            file.write(
                f"{event_type}: {count}\n"
            )

    print("Example 44:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 45: Save Unique IPs

    path = base / "example45.txt"

    unique_ips = set()

    for event in events:
        fields = event.split("|")

        if len(fields) == 4:
            unique_ips.add(fields[1])

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for address in sorted(unique_ips):
            file.write(address + "\n")

    print("Example 45:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 46: Export Security JSON

    path = base / "example46.json"

    structured_events = []

    for event in events:
        fields = event.split("|")

        if len(fields) != 4:
            continue

        structured_events.append({
            "date": fields[0],
            "source_ip": fields[1],
            "event_type": fields[2],
            "severity": fields[3]
        })

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            structured_events,
            file,
            indent=4
        )

    print(
        "Example 46:",
        len(structured_events),
        "events exported."
    )


    # EXAMPLE 47: Save Rejected Records

    path = base / "example47.txt"

    rejected_records = [
        {
            "line": 4,
            "reason": "Missing fields"
        },
        {
            "line": 7,
            "reason": "Invalid severity"
        }
    ]

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        for record in rejected_records:
            file.write(
                f"Line {record['line']}: "
                f"{record['reason']}\n"
            )

    print("Example 47:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 48: Write Security Alert

    path = base / "example48.txt"

    failed_logins = 5
    threshold = 3

    if failed_logins >= threshold:
        message = (
            "ALERT: Failed login threshold exceeded."
        )
    else:
        message = (
            "No failed login alert."
        )

    path.write_text(
        message,
        encoding="utf-8"
    )

    print("Example 48:", path.read_text(
        encoding="utf-8"
    ))


    # EXAMPLE 49: Atomic File Replacement
    #
    # For important reports, writing
    # a complete temporary file and
    # replacing the destination can
    # reduce partial-file updates.
    #
    # os.replace() is atomic when
    # supported by the filesystem.
    #
    # This does not guarantee
    # crash durability or solve
    # concurrent-writer conflicts.

    destination = base / "example49.txt"
    temporary = base / "example49.tmp"

    destination.write_text(
        "Old report",
        encoding="utf-8"
    )

    temporary.write_text(
        "New completed report",
        encoding="utf-8"
    )

    os.replace(
        temporary,
        destination
    )

    print(
        "Example 49:",
        destination.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 50: COMPLETE SECURITY
    # REPORT WRITING SYSTEM
    #
    # Combines:
    #
    # File writing
    # File reading
    # Dictionaries
    # Lists
    # Loops
    # Functions
    # Validation
    # Counting
    # JSON output
    # Text reports
    # Error handling
    #
    # All events are synthetic.

    training_events = [
        {
            "date": "2026-11-11",
            "source_ip": "192.0.2.10",
            "event_type": "LOGIN_FAILED",
            "severity": "HIGH"
        },
        {
            "date": "2026-11-11",
            "source_ip": "192.0.2.10",
            "event_type": "LOGIN_FAILED",
            "severity": "HIGH"
        },
        {
            "date": "2026-11-11",
            "source_ip": "198.51.100.20",
            "event_type": "LOGIN_SUCCESS",
            "severity": "LOW"
        },
        {
            "date": "2026-11-11",
            "source_ip": "203.0.113.5",
            "event_type": "PORT_SCAN",
            "severity": "MEDIUM"
        },
        {
            "date": "2026-11-11",
            "source_ip": "198.51.100.30",
            "event_type": "FILE_ACCESS",
            "severity": "LOW"
        }
    ]


    def validate_event(event):
        required = {
            "date",
            "source_ip",
            "event_type",
            "severity"
        }

        if not isinstance(event, dict):
            return False

        return required.issubset(
            event.keys()
        )


    def analyze_events(records):
        accepted = []
        rejected = 0
        counts = Counter()
        unique_sources = set()

        for record in records:
            if not validate_event(record):
                rejected += 1
                continue

            accepted.append(record.copy())

            counts[
                record["event_type"]
            ] += 1

            unique_sources.add(
                record["source_ip"]
            )

        return {
            "total_received": len(records),
            "accepted_count": len(accepted),
            "rejected_count": rejected,
            "event_counts": dict(counts),
            "unique_sources": sorted(unique_sources),
            "accepted_events": accepted
        }


    def save_text_report(report, path):
        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(
                "SECURITY EVENT REPORT\n"
            )
            file.write(
                "=====================\n"
            )

            file.write(
                f"Total: {report['total_received']}\n"
            )

            file.write(
                f"Accepted: {report['accepted_count']}\n"
            )

            file.write(
                f"Rejected: {report['rejected_count']}\n"
            )

            file.write("\nEvent Counts:\n")

            for event, count in report[
                "event_counts"
            ].items():
                file.write(
                    f"{event}: {count}\n"
                )

            file.write("\nUnique Sources:\n")

            for address in report[
                "unique_sources"
            ]:
                file.write(address + "\n")


    def save_json_report(report, path):
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


    def display_saved_report(path):
        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                print(file.read())

        except (FileNotFoundError, PermissionError):
            print(
                "Unable to read saved report."
            )


    final_report = analyze_events(
        training_events
    )

    text_report_path = (
        reports / "security_report.txt"
    )

    json_report_path = (
        reports / "security_report.json"
    )

    save_text_report(
        final_report,
        text_report_path
    )

    save_json_report(
        final_report,
        json_report_path
    )

    print(
        "\nExample 50: Text report saved:",
        text_report_path.exists()
    )

    print(
        "Example 50: JSON report saved:",
        json_report_path.exists()
    )

    display_saved_report(
        text_report_path
    )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    with TemporaryDirectory(
        prefix="day28_training_"
    ) as training_folder:

        run_lesson(training_folder)


# ==========================================
# WHAT I LEARNED
# ==========================================
#
# 1. Writing files saves data.
# 2. "w" creates or overwrites files.
# 3. "a" appends to existing files.
# 4. "x" creates files exclusively.
# 5. "w+" supports writing and reading.
# 6. "a+" supports appending and reading.
# 7. "wb" writes binary data.
# 8. write() writes strings.
# 9. writelines() writes multiple strings.
# 10. writelines() adds no newlines.
# 11. Numbers require text conversion.
# 12. f-strings format file output.
# 13. Lists can be written line by line.
# 14. Dictionary values can be written.
# 15. enumerate() numbers output lines.
# 16. Reports can contain headers.
# 17. Timestamps can be saved.
# 18. UTF-8 supports Unicode text.
# 19. Empty files can be created.
# 20. join() combines strings.
# 21. Path.write_text() writes text.
# 22. Path.write_bytes() writes bytes.
# 23. mkdir() creates directories.
# 24. Files can be saved in subfolders.
# 25. Existence checks are not atomic.
# 26. seek() changes file position.
# 27. flush() flushes Python buffers.
# 28. Written files can be verified.
# 29. File writing may raise exceptions.
# 30. JSON can store dictionaries.
# 31. JSON can store lists.
# 32. JSON supports Unicode text.
# 33. Configuration files can be saved.
# 34. Summary reports can be generated.
# 35. Flower inventory can be saved.
# 36. Inventory changes can be appended.
# 37. Order summaries can be written.
# 38. Multiple orders can be exported.
# 39. Sales reports can be generated.
# 40. Security events can be logged.
# 41. Security logs can be appended.
# 42. Suspicious events can be filtered.
# 43. Event counts can be saved.
# 44. Unique IPs can be exported.
# 45. Structured events can be JSON.
# 46. Rejected records can be tracked.
# 47. Alerts can be saved.
# 48. os.replace() replaces files.
# 49. File writing needs safe design.
# 50. Report generation supports
#     business and cybersecurity work.
