
# ==========================================
# DAY 29 - CSV FILES
# Topic: Structured Data with Python
# ==========================================

# LESSON NOTES
#
# CSV stands for:
# Comma-Separated Values
#
# CSV files store tabular data.
#
# Example:
#
# product,quantity,price
# Roses,10,75.00
# Tulips,5,55.00
#
# Each row represents a record.
# Each column represents a field.
#
# Python includes the csv module.
#
# IMPORTANT TOOLS:
#
# csv.reader()
# csv.writer()
# csv.DictReader()
# csv.DictWriter()
# writerow()
# writerows()
# writeheader()
#
# FILE HANDLING:
#
# Use with open().
# Specify encoding="utf-8".
# Use newline="" for CSV files.
#
# IMPORTANT CONCEPTS:
#
# CSV values are generally strings.
# Convert numeric fields carefully.
# Validate column names.
# Handle missing values.
# Handle malformed rows.
# Avoid overwriting important files.
#
# SECURITY NOTES:
#
# Treat imported CSV as untrusted.
# Validate all fields.
# Do not execute CSV contents.
# Avoid storing credentials.
# Protect sensitive business data.
#
# CSV formula injection:
#
# Spreadsheet programs may interpret
# values beginning with characters
# such as =, +, -, or @ as formulas.
#
# Do not assume CSV quoting alone
# prevents spreadsheet execution.
#
# Exporting untrusted text to
# spreadsheet applications requires
# appropriate safety controls.
#
# All datasets below are fictional.


# ==========================================
# SECTION 1 - IMPORTS AND SETUP
# ==========================================

import csv
import io

from pathlib import Path
from tempfile import TemporaryDirectory
from collections import Counter
from decimal import Decimal, InvalidOperation
from ipaddress import ip_address
from datetime import datetime


def run_lesson(folder):

    base = Path(folder)

    inventory_path = base / "inventory.csv"
    security_path = base / "security_events.csv"

    # Create sample inventory data.

    with open(
        inventory_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "product",
            "quantity",
            "price"
        ])

        writer.writerows([
            ["Rose Bouquet", 10, "75.00"],
            ["Tulip Arrangement", 5, "55.00"],
            ["Luxury Bouquet", 3, "125.00"],
            ["Orchid Arrangement", 7, "95.00"]
        ])

    # Create synthetic security data.

    security_records = [
        [
            "2026-11-11T08:00:00",
            "192.0.2.10",
            "LOGIN_FAILED",
            "HIGH"
        ],
        [
            "2026-11-11T08:05:00",
            "198.51.100.20",
            "LOGIN_SUCCESS",
            "LOW"
        ],
        [
            "2026-11-11T08:10:00",
            "203.0.113.5",
            "PORT_SCAN",
            "MEDIUM"
        ],
        [
            "2026-11-11T08:15:00",
            "192.0.2.10",
            "LOGIN_FAILED",
            "HIGH"
        ],
        [
            "2026-11-11T08:20:00",
            "198.51.100.30",
            "FILE_ACCESS",
            "LOW"
        ]
    ]

    with open(
        security_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "source_ip",
            "event_type",
            "severity"
        ])

        writer.writerows(security_records)

    # ======================================
    # SECTION 2 - BASIC CSV READING
    # ======================================

    # EXAMPLE 1: Read a CSV File

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        for row in reader:
            print("Example 1:", row)


    # EXAMPLE 2: Read CSV Headers

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        headers = next(reader)

    print("Example 2:", headers)


    # EXAMPLE 3: Read First Data Row

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        next(reader)

        first_row = next(reader)

    print("Example 3:", first_row)


    # EXAMPLE 4: Convert Rows to a List

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        rows = list(csv.reader(file))

    print("Example 4:", rows)


    # EXAMPLE 5: Count Data Rows

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        next(reader)

        count = sum(1 for row in reader)

    print("Example 5:", count)


    # EXAMPLE 6: Access CSV Columns

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:
            print(
                "Example 6:",
                row[0],
                row[1],
                row[2]
            )


    # EXAMPLE 7: CSV Values Are Strings

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        first = next(reader)

    print(
        "Example 7:",
        type(first["quantity"])
    )


    # EXAMPLE 8: Convert Quantity

    quantity = int(first["quantity"])

    print("Example 8:", quantity)


    # EXAMPLE 9: Convert Price

    price = Decimal(first["price"])

    print("Example 9:", price)


    # EXAMPLE 10: Calculate Row Total

    total = quantity * price

    print("Example 10:", total)


    # ======================================
    # SECTION 3 - DICTIONARY READING
    # ======================================

    # EXAMPLE 11: DictReader

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            print("Example 11:", row)


    # EXAMPLE 12: Access Named Fields

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(
                "Example 12:",
                row["product"]
            )


    # EXAMPLE 13: Read All Dictionaries

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        records = list(
            csv.DictReader(file)
        )

    print("Example 13:", records)


    # EXAMPLE 14: Filter CSV Rows

    expensive = [
        row
        for row in records
        if Decimal(row["price"]) >= 90
    ]

    print("Example 14:", expensive)


    # EXAMPLE 15: Sum Quantities

    total_quantity = sum(
        int(row["quantity"])
        for row in records
    )

    print("Example 15:", total_quantity)


    # EXAMPLE 16: Total Inventory Value

    inventory_value = sum(
        (
            int(row["quantity"])
            * Decimal(row["price"])
            for row in records
        ),
        Decimal("0")
    )

    print(
        "Example 16:",
        inventory_value
    )


    # EXAMPLE 17: Find Highest Price

    highest = max(
        records,
        key=lambda row: Decimal(
            row["price"]
        )
    )

    print(
        "Example 17:",
        highest["product"]
    )


    # EXAMPLE 18: Sort by Product

    sorted_records = sorted(
        records,
        key=lambda row: row[
            "product"
        ].casefold()
    )

    print(
        "Example 18:",
        [
            row["product"]
            for row in sorted_records
        ]
    )


    # EXAMPLE 19: Search Product Name

    matches = [
        row
        for row in records
        if "bouquet" in row[
            "product"
        ].casefold()
    ]

    print("Example 19:", matches)


    # EXAMPLE 20: Extract One Column

    names = [
        row["product"]
        for row in records
    ]

    print("Example 20:", names)


    # ======================================
    # SECTION 4 - CSV WRITING
    # ======================================

    # EXAMPLE 21: Create CSV File

    path = base / "example21.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "name",
            "score"
        ])

    print("Example 21:", path.exists())


    # EXAMPLE 22: Write One Data Row

    path = base / "example22.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "product",
            "quantity"
        ])

        writer.writerow([
            "Rose Bouquet",
            10
        ])

    print(
        "Example 22:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 23: writerows()

    path = base / "example23.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerows([
            ["name", "quantity"],
            ["Roses", 10],
            ["Tulips", 5],
            ["Orchids", 8]
        ])

    print(
        "Example 23:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 24: DictWriter

    path = base / "example24.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "product",
                "price"
            ]
        )

        writer.writeheader()

        writer.writerow({
            "product": "Luxury Bouquet",
            "price": "125.00"
        })

    print(
        "Example 24:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 25: Write Dictionaries

    path = base / "example25.csv"

    products = [
        {
            "product": "Rose Bouquet",
            "price": "75.00"
        },
        {
            "product": "Tulip Arrangement",
            "price": "55.00"
        }
    ]

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "product",
                "price"
            ]
        )

        writer.writeheader()

        writer.writerows(products)

    print(
        "Example 25:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 26: Append CSV Row

    with open(
        path,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Orchid Arrangement",
            "95.00"
        ])

    print(
        "Example 26:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 27: Custom Delimiter

    path = base / "example27.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(
            file,
            delimiter=";"
        )

        writer.writerow([
            "product",
            "price"
        ])

        writer.writerow([
            "Rose Bouquet",
            "75.00"
        ])

    print(
        "Example 27:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 28: Read Custom Delimiter

    with open(
        path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(
            file,
            delimiter=";"
        )

        custom_rows = list(reader)

    print("Example 28:", custom_rows)


    # EXAMPLE 29: Quoted Fields

    path = base / "example29.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "product",
            "description"
        ])

        writer.writerow([
            "Rose Bouquet",
            "Red, pink, and white roses"
        ])

    print(
        "Example 29:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # EXAMPLE 30: Quote All Fields

    path = base / "example30.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(
            file,
            quoting=csv.QUOTE_ALL
        )

        writer.writerow([
            "product",
            "quantity"
        ])

        writer.writerow([
            "Rose Bouquet",
            10
        ])

    print(
        "Example 30:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # ======================================
    # SECTION 5 - VALIDATION AND ERRORS
    # ======================================

    # EXAMPLE 31: Validate Headers

    required_headers = {
        "product",
        "quantity",
        "price"
    }

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        actual_headers = set(
            reader.fieldnames or []
        )

    print(
        "Example 31:",
        required_headers.issubset(
            actual_headers
        )
    )


    # EXAMPLE 32: Detect Missing Fields

    incomplete = {
        "product": "Roses",
        "quantity": ""
    }

    missing = [
        key
        for key, value in incomplete.items()
        if not str(value).strip()
    ]

    print("Example 32:", missing)


    # EXAMPLE 33: Handle Invalid Integer

    raw_quantity = "not_a_number"

    try:
        converted = int(raw_quantity)

    except ValueError:
        converted = None

    print("Example 33:", converted)


    # EXAMPLE 34: Handle Invalid Price

    raw_price = "invalid"

    try:
        converted_price = Decimal(
            raw_price
        )

    except InvalidOperation:
        converted_price = None

    print(
        "Example 34:",
        converted_price
    )


    # EXAMPLE 35: Validate Positive Quantity

    def valid_quantity(value):
        try:
            number = int(value)

        except (ValueError, TypeError):
            return False

        return number >= 0

    print(
        "Example 35:",
        valid_quantity("10")
    )


    # EXAMPLE 36: Validate Price

    def valid_price(value):
        try:
            amount = Decimal(
                str(value)
            )

        except (
            InvalidOperation,
            TypeError,
            ValueError
        ):
            return False

        return (
            amount.is_finite()
            and amount >= 0
        )

    print(
        "Example 36:",
        valid_price("75.00")
    )


    # EXAMPLE 37: Handle Empty CSV

    path = base / "example37.csv"

    path.write_text(
        "",
        encoding="utf-8"
    )

    with open(
        path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        rows = list(
            csv.reader(file)
        )

    print("Example 37:", rows)


    # EXAMPLE 38: Handle Missing File

    missing_path = base / "missing.csv"

    try:
        with open(
            missing_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            rows = list(
                csv.reader(file)
            )

    except FileNotFoundError:
        rows = []

    print("Example 38:", rows)


    # EXAMPLE 39: Detect Extra Columns

    path = base / "example39.csv"

    path.write_text(
        "name,quantity\n"
        "Roses,10,EXTRA\n",
        encoding="utf-8"
    )

    with open(
        path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        extra_records = [
            row
            for row in reader
            if None in row
        ]

    print(
        "Example 39:",
        extra_records
    )


    # EXAMPLE 40: Detect Missing Columns

    path = base / "example40.csv"

    path.write_text(
        "name,quantity,price\n"
        "Roses,10\n",
        encoding="utf-8"
    )

    with open(
        path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        incomplete_records = [
            row
            for row in reader
            if any(
                value is None
                for value in row.values()
            )
        ]

    print(
        "Example 40:",
        incomplete_records
    )


    # ======================================
    # SECTION 6 - ADVANCED CSV FEATURES
    # ======================================

    # EXAMPLE 41: Detect CSV Delimiter
    #
    # Sniffer makes a best-effort
    # guess. It is not guaranteed
    # to identify every file.

    sample = (
        "name;quantity\n"
        "Roses;10\n"
        "Tulips;5\n"
    )

    dialect = csv.Sniffer().sniff(
        sample,
        delimiters=",;\t"
    )

    print(
        "Example 41:",
        repr(dialect.delimiter)
    )


    # EXAMPLE 42: Read CSV from String

    sample = (
        "name,quantity\n"
        "Roses,10\n"
        "Tulips,5\n"
    )

    reader = csv.DictReader(
        io.StringIO(sample)
    )

    print(
        "Example 42:",
        list(reader)
    )


    # EXAMPLE 43: Write CSV to String

    buffer = io.StringIO(
        newline=""
    )

    writer = csv.writer(buffer)

    writer.writerow([
        "name",
        "quantity"
    ])

    writer.writerow([
        "Roses",
        10
    ])

    print(
        "Example 43:",
        buffer.getvalue()
    )


    # EXAMPLE 44: Read UTF-8 CSV

    path = base / "example44.csv"

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "product",
            "description"
        ])

        writer.writerow([
            "Rosé Bouquet",
            "Luxury flowers 🌸"
        ])

    with open(
        path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        unicode_rows = list(
            csv.reader(file)
        )

    print(
        "Example 44:",
        unicode_rows
    )


    # EXAMPLE 45: Sort CSV Data

    with open(
        inventory_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        inventory = list(
            csv.DictReader(file)
        )

    inventory.sort(
        key=lambda row: Decimal(
            row["price"]
        ),
        reverse=True
    )

    print(
        "Example 45:",
        [
            row["product"]
            for row in inventory
        ]
    )


    # ======================================
    # SECTION 7 - CYBERSECURITY CSV DATA
    # ======================================

    # EXAMPLE 46: Read Security CSV

    with open(
        security_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        security_events = list(
            csv.DictReader(file)
        )

    print(
        "Example 46:",
        security_events
    )


    # EXAMPLE 47: Count Event Types

    event_counts = Counter(
        row["event_type"]
        for row in security_events
    )

    print(
        "Example 47:",
        dict(event_counts)
    )


    # EXAMPLE 48: Filter High Severity

    high_severity = [
        row
        for row in security_events
        if row["severity"] == "HIGH"
    ]

    print(
        "Example 48:",
        high_severity
    )


    # EXAMPLE 49: Export Filtered Events

    path = base / "example49.csv"

    fieldnames = [
        "timestamp",
        "source_ip",
        "event_type",
        "severity"
    ]

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            high_severity
        )

    print(
        "Example 49:",
        path.read_text(
            encoding="utf-8"
        )
    )


    # ======================================
    # EXAMPLE 50 - COMPLETE CSV
    # SECURITY EVENT ANALYZER
    # ======================================

    # This example combines:
    #
    # Reading CSV
    # Writing CSV
    # DictReader
    # DictWriter
    # Validation
    # Error handling
    # Event filtering
    # Event counting
    # Unique IP addresses
    # Report generation
    #
    # All data is synthetic.

    allowed_events = {
        "LOGIN_FAILED",
        "LOGIN_SUCCESS",
        "PORT_SCAN",
        "FILE_ACCESS"
    }

    allowed_severities = {
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    }

    expected_fields = [
        "timestamp",
        "source_ip",
        "event_type",
        "severity"
    ]

    def validate_security_row(row):
        errors = []

        if None in row:
            errors.append(
                "Extra CSV columns"
            )

        for field in expected_fields:
            value = row.get(field)

            if not isinstance(value, str):
                errors.append(
                    f"Missing {field}"
                )

            elif not value.strip():
                errors.append(
                    f"Blank {field}"
                )

        if errors:
            return errors

        try:
            datetime.fromisoformat(
                row["timestamp"]
            )

        except ValueError:
            errors.append(
                "Invalid timestamp"
            )

        try:
            ip_address(
                row["source_ip"]
            )

        except ValueError:
            errors.append(
                "Invalid IP address"
            )

        if row["event_type"] not in allowed_events:
            errors.append(
                "Invalid event type"
            )

        if row["severity"] not in allowed_severities:
            errors.append(
                "Invalid severity"
            )

        return errors


    def analyze_security_csv(path):
        report = {
            "total_rows": 0,
            "valid_events": [],
            "invalid_records": [],
            "event_counts": {},
            "severity_counts": {},
            "unique_ips": []
        }

        event_counter = Counter()
        severity_counter = Counter()
        source_ips = set()

        try:
            with open(
                path,
                "r",
                newline="",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                if reader.fieldnames != expected_fields:
                    report["file_error"] = (
                        "Unexpected CSV headers"
                    )
                    return report

                for line_number, row in enumerate(
                    reader,
                    start=2
                ):
                    report["total_rows"] += 1

                    errors = validate_security_row(
                        row
                    )

                    if errors:
                        report[
                            "invalid_records"
                        ].append({
                            "line": line_number,
                            "errors": errors
                        })

                        continue

                    cleaned = {
                        field: row[field].strip()
                        for field in expected_fields
                    }

                    report[
                        "valid_events"
                    ].append(cleaned)

                    event_counter[
                        cleaned["event_type"]
                    ] += 1

                    severity_counter[
                        cleaned["severity"]
                    ] += 1

                    source_ips.add(
                        cleaned["source_ip"]
                    )

        except (
            FileNotFoundError,
            PermissionError,
            UnicodeError,
            csv.Error
        ) as error:

            report["file_error"] = (
                type(error).__name__
            )

            return report

        report["event_counts"] = dict(
            event_counter
        )

        report["severity_counts"] = dict(
            severity_counter
        )

        report["unique_ips"] = sorted(
            source_ips
        )

        return report


    def export_valid_events(report, path):
        with open(
            path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=expected_fields
            )

            writer.writeheader()

            writer.writerows(
                report["valid_events"]
            )


    def export_summary(report, path):
        with open(
            path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "metric",
                "value"
            ])

            writer.writerow([
                "total_rows",
                report["total_rows"]
            ])

            writer.writerow([
                "valid_rows",
                len(report["valid_events"])
            ])

            writer.writerow([
                "invalid_rows",
                len(report["invalid_records"])
            ])

            writer.writerow([
                "unique_source_ips",
                len(report["unique_ips"])
            ])


    # Add malformed training records.

    challenge_path = (
        base / "security_challenge.csv"
    )

    with open(
        challenge_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            expected_fields
        )

        writer.writerows(
            security_records
        )

        writer.writerow([
            "2026-11-11T09:00:00",
            "invalid-ip",
            "LOGIN_FAILED",
            "HIGH"
        ])

        writer.writerow([
            "2026-11-11T09:05:00",
            "192.0.2.50",
            "UNKNOWN_EVENT",
            "LOW"
        ])

        writer.writerow([
            "2026-11-11T09:10:00",
            "203.0.113.10"
        ])


    final_report = analyze_security_csv(
        challenge_path
    )

    if "file_error" not in final_report:

        valid_output = (
            base / "valid_events.csv"
        )

        summary_output = (
            base / "security_summary.csv"
        )

        export_valid_events(
            final_report,
            valid_output
        )

        export_summary(
            final_report,
            summary_output
        )

        print(
            "\n===== CSV SECURITY REPORT ====="
        )

        print(
            "Total rows:",
            final_report["total_rows"]
        )

        print(
            "Valid events:",
            len(final_report["valid_events"])
        )

        print(
            "Invalid records:",
            len(final_report["invalid_records"])
        )

        print(
            "Event counts:",
            final_report["event_counts"]
        )

        print(
            "Severity counts:",
            final_report["severity_counts"]
        )

        print(
            "Unique source IPs:",
            final_report["unique_ips"]
        )

        print(
            "Valid CSV exported:",
            valid_output.exists()
        )

        print(
            "Summary CSV exported:",
            summary_output.exists()
        )

    else:
        print(
            "CSV analysis failed:",
            final_report["file_error"]
        )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    with TemporaryDirectory(
        prefix="day29_csv_training_"
    ) as training_folder:

        run_lesson(training_folder)


# ==========================================
# WHAT I LEARNED
# ==========================================
#
# 1. CSV stores tabular data.
# 2. csv.reader() reads rows as lists.
# 3. csv.writer() writes CSV rows.
# 4. DictReader reads dictionaries.
# 5. DictWriter writes dictionaries.
# 6. writerow() writes one row.
# 7. writerows() writes multiple rows.
# 8. writeheader() writes headers.
# 9. CSV values are usually strings.
# 10. Numeric conversion is necessary.
# 11. Decimal supports exact money values.
# 12. CSV rows can be counted.
# 13. CSV data can be filtered.
# 14. CSV data can be sorted.
# 15. CSV values can be searched.
# 16. Columns can be extracted.
# 17. CSV data can be appended.
# 18. Custom delimiters are supported.
# 19. CSV handles quoted fields.
# 20. QUOTE_ALL quotes every field.
# 21. CSV headers should be validated.
# 22. Missing fields should be checked.
# 23. Invalid numbers need handling.
# 24. Empty CSV files can be handled.
# 25. Missing files raise exceptions.
# 26. Extra columns can be detected.
# 27. Missing columns can be detected.
# 28. Sniffer guesses CSV dialects.
# 29. StringIO supports in-memory CSV.
# 30. UTF-8 supports Unicode data.
# 31. Inventory data can be analyzed.
# 32. Inventory totals can be calculated.
# 33. Security events can be stored.
# 34. Security events can be filtered.
# 35. Event types can be counted.
# 36. Severity levels can be counted.
# 37. Unique source IPs can be found.
# 38. Invalid records can be separated.
# 39. Timestamps can be validated.
# 40. IP addresses can be validated.
# 41. Allowed event types can be checked.
# 42. CSV reports can be exported.
# 43. CSV data is untrusted input.
# 44. Spreadsheet formula injection
#     requires attention.
# 45. Quoting does not prevent formulas.
# 46. Context managers close files.
# 47. newline="" supports CSV handling.
# 48. Encoding should be specified.
# 49. CSV supports business analytics.
# 50. CSV supports cybersecurity analysis.
