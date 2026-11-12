
# ==========================================
# DAY 27 - READING FILES
# Topic: File Input and Text Processing
# ==========================================

# LESSON NOTES
#
# Files allow information to exist
# outside the running Python program.
#
# Python can read:
#
# Text files
# Log files
# Configuration files
# CSV files
# JSON files
# Binary files
#
# Today focuses on reading text files.
#
# Basic syntax:
#
# with open("example.txt", "r") as file:
#     content = file.read()
#
# File modes:
#
# "r"  = read text
# "rb" = read binary data
#
# Important methods:
#
# read()
# readline()
# readlines()
# seek()
# tell()
#
# Important concepts:
#
# Absolute paths
# Relative paths
# File encodings
# UTF-8
# Newline characters
# Context managers
# Exception handling
# File existence checks
# Log processing
#
# SECURITY NOTES:
#
# Treat file contents as untrusted input.
# Validate records before using them.
# Avoid displaying secrets in logs.
# Limit file access to authorized paths.
# Do not execute text read from files.
# Avoid reading unbounded files
# entirely into memory.
#
# All security data is synthetic.


# ==========================================
# SECTION 1 - IMPORTS AND TEST FILES
# ==========================================

from pathlib import Path
from tempfile import TemporaryDirectory
from collections import Counter
import json


# TemporaryDirectory creates a
# disposable folder for examples.
#
# The folder is automatically removed
# after the lesson finishes.
#
# Day 28 will cover writing files
# in greater detail.


def run_lesson(folder):
    base = Path(folder)

    text_path = base / "message.txt"
    lines_path = base / "flowers.txt"
    log_path = base / "security.log"
    config_path = base / "settings.txt"
    json_path = base / "events.json"
    unicode_path = base / "unicode.txt"
    empty_path = base / "empty.txt"
    numbers_path = base / "numbers.txt"

    # Create fictional training data.

    text_path.write_text(
        "Welcome to Golden Aura Florals.\n"
        "This is a Python reading lesson.\n",
        encoding="utf-8"
    )

    lines_path.write_text(
        "Rose Bouquet\n"
        "Tulip Arrangement\n"
        "Mixed Floral Bouquet\n"
        "Luxury Arrangement\n",
        encoding="utf-8"
    )

    log_path.write_text(
        "2026-11-01|192.0.2.10|LOGIN_FAILED|HIGH\n"
        "2026-11-01|198.51.100.20|LOGIN_SUCCESS|LOW\n"
        "2026-11-02|203.0.113.5|PORT_SCAN|MEDIUM\n"
        "2026-11-02|192.0.2.10|LOGIN_FAILED|HIGH\n"
        "2026-11-03|198.51.100.30|FILE_ACCESS|LOW\n"
        "MALFORMED_RECORD\n",
        encoding="utf-8"
    )

    config_path.write_text(
        "# Training configuration\n"
        "application=security_monitor\n"
        "environment=lab\n"
        "logging=enabled\n"
        "\n"
        "# End of configuration\n",
        encoding="utf-8"
    )

    json_path.write_text(
        json.dumps([
            {
                "event": "LOGIN_FAILED",
                "source_ip": "192.0.2.10"
            },
            {
                "event": "PORT_SCAN",
                "source_ip": "203.0.113.5"
            }
        ]),
        encoding="utf-8"
    )

    unicode_path.write_text(
        "Flowers: Rosé, Tulip, Orchid 🌸\n",
        encoding="utf-8"
    )

    empty_path.write_text(
        "",
        encoding="utf-8"
    )

    numbers_path.write_text(
        "10\n20\ninvalid\n30\n",
        encoding="utf-8"
    )

    # ======================================
    # SECTION 2 - BASIC FILE READING
    # ======================================

    # EXAMPLE 1: Open a Text File

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    print("Example 1:", content)


    # EXAMPLE 2: Read Entire File

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        flowers = file.read()

    print("Example 2:", flowers)


    # EXAMPLE 3: Read First Line

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        first_line = file.readline()

    print("Example 3:", first_line.strip())


    # EXAMPLE 4: Read Two Lines

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        first = file.readline()
        second = file.readline()

    print("Example 4:", first.strip())
    print("Example 4:", second.strip())


    # EXAMPLE 5: readlines()

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        all_lines = file.readlines()

    print("Example 5:", all_lines)


    # EXAMPLE 6: Loop Through a File

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        for line in file:
            print("Example 6:", line.strip())


    # EXAMPLE 7: Read a Fixed Number
    # of Characters

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        portion = file.read(10)

    print("Example 7:", portion)


    # EXAMPLE 8: Multiple Small Reads

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        part_one = file.read(7)
        part_two = file.read(8)

    print("Example 8:", part_one)
    print("Example 8:", part_two)


    # EXAMPLE 9: File Closed Automatically

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    print("Example 9:", file.closed)


    # EXAMPLE 10: Empty File

    with open(
        empty_path,
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    print("Example 10:", repr(content))


    # ======================================
    # SECTION 3 - STRING PROCESSING
    # ======================================

    # EXAMPLE 11: Remove Newlines

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        cleaned = [
            line.strip()
            for line in file
        ]

    print("Example 11:", cleaned)


    # EXAMPLE 12: Remove Only
    # Line Ending Characters

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        cleaned = [
            line.rstrip("\r\n")
            for line in file
        ]

    print("Example 12:", cleaned)


    # EXAMPLE 13: Count Lines

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        count = sum(1 for line in file)

    print("Example 13:", count)


    # EXAMPLE 14: Count Nonempty Lines

    with open(
        config_path,
        "r",
        encoding="utf-8"
    ) as file:
        count = sum(
            1 for line in file
            if line.strip()
        )

    print("Example 14:", count)


    # EXAMPLE 15: Search for Text

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        found = any(
            "Tulip" in line
            for line in file
        )

    print("Example 15:", found)


    # EXAMPLE 16: Case-Insensitive Search

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        matches = [
            line.strip()
            for line in file
            if "rose" in line.casefold()
        ]

    print("Example 16:", matches)


    # EXAMPLE 17: Split Words

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        words = file.read().split()

    print("Example 17:", words)


    # EXAMPLE 18: Count Words

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        word_count = len(
            file.read().split()
        )

    print("Example 18:", word_count)


    # EXAMPLE 19: Find Longest Line

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        longest = max(
            (line.strip() for line in file),
            key=len,
            default=""
        )

    print("Example 19:", longest)


    # EXAMPLE 20: Enumerate Lines

    with open(
        lines_path,
        "r",
        encoding="utf-8"
    ) as file:
        for number, line in enumerate(
            file,
            start=1
        ):
            print(
                "Example 20:",
                number,
                line.strip()
            )


    # ======================================
    # SECTION 4 - FILE POSITION
    # ======================================

    # EXAMPLE 21: tell()

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        position = file.tell()

    print("Example 21:", position)


    # EXAMPLE 22: Position After Reading

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        file.read(5)
        position = file.tell()

    print("Example 22:", position)


    # EXAMPLE 23: seek(0)

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        first = file.read(7)

        file.seek(0)

        second = file.read(7)

    print("Example 23:", first, second)


    # EXAMPLE 24: Read Again

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        first_read = file.read()

        file.seek(0)

        second_read = file.read()

    print(
        "Example 24:",
        first_read == second_read
    )


    # EXAMPLE 25: Read Binary Data
    #
    # rb returns bytes.
    #
    # Binary data differs
    # from decoded text.

    with open(
        text_path,
        "rb"
    ) as file:
        raw_data = file.read(12)

    print("Example 25:", raw_data)


    # ======================================
    # SECTION 5 - PATHS AND ENCODING
    # ======================================

    # EXAMPLE 26: pathlib Path

    path = Path(text_path)

    print("Example 26:", path.name)


    # EXAMPLE 27: Check File Existence

    exists = text_path.is_file()

    print("Example 27:", exists)


    # EXAMPLE 28: Check Missing File

    missing_path = base / "missing.txt"

    print(
        "Example 28:",
        missing_path.exists()
    )


    # EXAMPLE 29: File Suffix

    print(
        "Example 29:",
        log_path.suffix
    )


    # EXAMPLE 30: File Stem

    print(
        "Example 30:",
        log_path.stem
    )


    # EXAMPLE 31: Parent Directory

    print(
        "Example 31:",
        log_path.parent.name
    )


    # EXAMPLE 32: UTF-8 Text

    with open(
        unicode_path,
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    print("Example 32:", content.strip())


    # EXAMPLE 33: Handle Missing File

    try:
        with open(
            missing_path,
            "r",
            encoding="utf-8"
        ) as file:
            content = file.read()

    except FileNotFoundError:
        content = None

    print("Example 33:", content)


    # EXAMPLE 34: Safe Reading Function

    def safe_read(path):
        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                return file.read()

        except (FileNotFoundError, PermissionError):
            return None

    print(
        "Example 34:",
        safe_read(text_path) is not None
    )


    # EXAMPLE 35: Read a Limited Amount
    #
    # Reading a fixed amount can
    # help avoid loading a large
    # file entirely into memory.

    with open(
        text_path,
        "r",
        encoding="utf-8"
    ) as file:
        preview = file.read(20)

    print("Example 35:", preview)


    # ======================================
    # SECTION 6 - CONFIGURATION FILES
    # ======================================

    # EXAMPLE 36: Skip Comments

    with open(
        config_path,
        "r",
        encoding="utf-8"
    ) as file:
        settings = [
            line.strip()
            for line in file
            if line.strip()
            and not line.lstrip().startswith("#")
        ]

    print("Example 36:", settings)


    # EXAMPLE 37: Parse Key-Value Lines

    configuration = {}

    with open(
        config_path,
        "r",
        encoding="utf-8"
    ) as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            configuration[key.strip()] = value.strip()

    print("Example 37:", configuration)


    # EXAMPLE 38: Read One Setting

    print(
        "Example 38:",
        configuration.get(
            "environment",
            "unknown"
        )
    )


    # EXAMPLE 39: Read JSON Data
    #
    # JSON is a structured
    # data format.
    #
    # JSON files are covered
    # in more depth later.

    with open(
        json_path,
        "r",
        encoding="utf-8"
    ) as file:
        events = json.load(file)

    print("Example 39:", events)


    # EXAMPLE 40: Handle Invalid JSON

    try:
        json.loads("{invalid json}")

    except json.JSONDecodeError:
        print(
            "Example 40: Invalid JSON data."
        )


    # ======================================
    # SECTION 7 - SECURITY LOG READING
    # ======================================

    # EXAMPLE 41: Read Security Log

    with open(
        log_path,
        "r",
        encoding="utf-8"
    ) as file:
        log_content = file.read()

    print("Example 41:\n", log_content)


    # EXAMPLE 42: Count Log Records

    with open(
        log_path,
        "r",
        encoding="utf-8"
    ) as file:
        record_count = sum(
            1 for line in file
            if line.strip()
        )

    print("Example 42:", record_count)


    # EXAMPLE 43: Find Failed Logins

    with open(
        log_path,
        "r",
        encoding="utf-8"
    ) as file:
        failed_logins = [
            line.strip()
            for line in file
            if "|LOGIN_FAILED|" in line
        ]

    print("Example 43:", failed_logins)


    # EXAMPLE 44: Count Failed Logins

    print(
        "Example 44:",
        len(failed_logins)
    )


    # EXAMPLE 45: Parse a Log Line

    sample_line = (
        "2026-11-01|192.0.2.10|LOGIN_FAILED|HIGH"
    )

    fields = sample_line.split("|")

    print("Example 45:", fields)


    # EXAMPLE 46: Validate Log Fields

    def parse_log_line(line):
        fields = line.strip().split("|")

        if len(fields) != 4:
            return None

        date, source_ip, event_type, severity = fields

        return {
            "date": date,
            "source_ip": source_ip,
            "event_type": event_type,
            "severity": severity
        }

    parsed = parse_log_line(sample_line)

    print("Example 46:", parsed)


    # EXAMPLE 47: Separate Malformed Lines

    valid_records = []
    invalid_lines = []

    with open(
        log_path,
        "r",
        encoding="utf-8"
    ) as file:
        for line_number, line in enumerate(
            file,
            start=1
        ):
            record = parse_log_line(line)

            if record is None:
                invalid_lines.append(line_number)

            else:
                valid_records.append(record)

    print(
        "Example 47: Valid:",
        len(valid_records)
    )

    print(
        "Example 47: Invalid lines:",
        invalid_lines
    )


    # EXAMPLE 48: Count Event Types

    event_counts = Counter(
        record["event_type"]
        for record in valid_records
    )

    print("Example 48:", dict(event_counts))


    # EXAMPLE 49: Unique Source IPs

    unique_ips = {
        record["source_ip"]
        for record in valid_records
    }

    print(
        "Example 49:",
        sorted(unique_ips)
    )


    # EXAMPLE 50: COMPLETE LOG READING REPORT
    #
    # Combines:
    #
    # File reading
    # Context managers
    # Line iteration
    # String splitting
    # Record validation
    # Dictionaries
    # Sets
    # Counting
    # Error handling
    # Functions
    # Return values
    #
    # All log entries are synthetic.

    def analyze_log_file(path):
        report = {
            "total_lines": 0,
            "valid_records": 0,
            "invalid_records": 0,
            "failed_logins": 0,
            "event_counts": {},
            "source_ips": set(),
            "invalid_line_numbers": []
        }

        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                for line_number, line in enumerate(
                    file,
                    start=1
                ):
                    report["total_lines"] += 1

                    record = parse_log_line(line)

                    if record is None:
                        report["invalid_records"] += 1

                        report[
                            "invalid_line_numbers"
                        ].append(line_number)

                        continue

                    report["valid_records"] += 1

                    event_type = record["event_type"]

                    report["event_counts"][event_type] = (
                        report["event_counts"].get(
                            event_type,
                            0
                        ) + 1
                    )

                    report["source_ips"].add(
                        record["source_ip"]
                    )

                    if event_type == "LOGIN_FAILED":
                        report["failed_logins"] += 1

        except (FileNotFoundError, PermissionError):
            return None

        return report


    def display_log_report(report):
        if report is None:
            print("Unable to read log file.")
            return

        print("\n===== SECURITY LOG REPORT =====")

        print(
            "Total lines:",
            report["total_lines"]
        )

        print(
            "Valid records:",
            report["valid_records"]
        )

        print(
            "Invalid records:",
            report["invalid_records"]
        )

        print(
            "Failed logins:",
            report["failed_logins"]
        )

        print(
            "Event counts:",
            report["event_counts"]
        )

        print(
            "Unique source IPs:",
            sorted(report["source_ips"])
        )

        print(
            "Invalid line numbers:",
            report["invalid_line_numbers"]
        )


    final_report = analyze_log_file(log_path)

    display_log_report(final_report)


# ==========================================
# SECTION 8 - PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    with TemporaryDirectory(
        prefix="day27_training_"
    ) as training_folder:
        run_lesson(training_folder)


# ==========================================
# WHAT I LEARNED
# ==========================================
#
# 1. Files store data outside Python.
# 2. open() opens a file.
# 3. "r" opens text for reading.
# 4. "rb" opens binary data.
# 5. read() returns file contents.
# 6. readline() reads one line.
# 7. readlines() returns a list of lines.
# 8. Files can be iterated line by line.
# 9. with closes files automatically.
# 10. Empty files return empty text.
# 11. strip() removes whitespace.
# 12. rstrip() can remove line endings.
# 13. Lines can be counted.
# 14. Nonempty lines can be counted.
# 15. Files can be searched for text.
# 16. casefold() supports text matching.
# 17. split() separates text.
# 18. Word counts can be calculated.
# 19. Longest lines can be identified.
# 20. enumerate() adds line numbers.
# 21. tell() reports file position.
# 22. seek() changes file position.
# 23. Files can be reread after seek(0).
# 24. Binary reads return bytes.
# 25. pathlib works with paths.
# 26. is_file() checks for regular files.
# 27. exists() checks path existence.
# 28. suffix returns file extensions.
# 29. stem returns filenames without suffix.
# 30. parent identifies parent directories.
# 31. UTF-8 supports Unicode text.
# 32. Missing files raise exceptions.
# 33. Safe reading functions can return None.
# 34. Large files should be read carefully.
# 35. Configuration comments can be skipped.
# 36. Key-value settings can be parsed.
# 37. JSON can be loaded from files.
# 38. Invalid JSON raises decode errors.
# 39. Security logs contain event records.
# 40. Log records can be counted.
# 41. Failed logins can be filtered.
# 42. Delimited lines can be split.
# 43. Malformed lines can be identified.
# 44. Event types can be counted.
# 45. Unique source IPs can be collected.
# 46. Reports can summarize log data.
# 47. File contents must be treated
#     as untrusted input.
# 48. Reading files supports automation.
# 49. Log analysis supports cybersecurity.
# 50. File handling is foundational
#     for future Python projects.
