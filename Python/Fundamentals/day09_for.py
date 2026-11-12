
# ==========================================
# DAY 09 - FOR LOOPS AND ITERATION
# Topic: Repeating Code with for
# ==========================================

# LESSON NOTES
#
# A for loop repeats instructions by
# iterating over a sequence of values.
#
# A sequence can contain numbers,
# characters, or other data.
#
# Each repetition is called an iteration.
#
# Python uses the for keyword to create
# a for loop.
#
# The in keyword identifies the values
# the loop will iterate through.
#
# The range() function generates a
# sequence of integers.
#
# A for loop is useful when processing
# a known collection of values.
#
# Unlike many while loops, a for loop
# does not require manually updating
# a counter to advance through its sequence.


# EXAMPLE 1: Basic For Loop

for number in range(5):
    print("Number:", number)


# EXAMPLE 2: Counting from 1 to 10

for number in range(1, 11):
    print("Count:", number)


# EXAMPLE 3: Understanding range()
#
# range(stop) starts at zero.
#
# range(start, stop) starts at start.
#
# The stop value is not included.

for number in range(1, 6):
    print(number)


# EXAMPLE 4: Using a Step Value
#
# range(start, stop, step)
#
# The step determines how much
# the number changes each iteration.

for number in range(0, 11, 2):
    print("Even number:", number)


# EXAMPLE 5: Counting Backward

for number in range(10, 0, -1):
    print("Countdown:", number)

print("Countdown completed.")


# EXAMPLE 6: Repeating a Message

for repetition in range(3):
    print("Welcome to my coding camp!")


# EXAMPLE 7: Iterating Through a String
#
# Strings contain sequences of characters.
#
# A for loop can process each character.

name = "Python"

for letter in name:
    print("Letter:", letter)


# EXAMPLE 8: Iterating Through a List
#
# A list stores multiple values.
#
# Lists will be covered in more
# detail later in the curriculum.

programming_languages = ["Python", "C", "C++"]

for language in programming_languages:
    print("Language:", language)


# EXAMPLE 9: Adding Numbers with a For Loop

total = 0

for number in range(1, 6):
    total += number

print("Total:", total)


# EXAMPLE 10: Multiplication Table

number = 5

for multiplier in range(1, 11):
    result = number * multiplier

    print(number, "x", multiplier, "=", result)


# EXAMPLE 11: Using if Inside a For Loop

for number in range(1, 11):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")


# EXAMPLE 12: Using break
#
# break exits the loop immediately.

for number in range(1, 11):
    if number == 6:
        break

    print("Number:", number)

print("Loop stopped.")


# EXAMPLE 13: Using continue
#
# continue skips the remaining code
# in the current iteration.

for number in range(1, 11):
    if number == 5:
        continue

    print("Number:", number)


# EXAMPLE 14: Nested For Loops
#
# A nested loop is a loop inside
# another loop.
#
# The inner loop runs for each
# iteration of the outer loop.

for row in range(1, 4):
    for column in range(1, 4):
        print("Row:", row, "Column:", column)


# EXAMPLE 15: Flower Inventory
#
# Simulate preparing five bouquets.

for bouquet in range(1, 6):
    print("Preparing bouquet:", bouquet)

print("All bouquets prepared.")


# EXAMPLE 16: Flower Sales Revenue

bouquet_prices = [65, 75, 85, 95]

revenue = 0

for price in bouquet_prices:
    revenue += price

print("Total revenue: $", revenue)


# EXAMPLE 17: Student Grades

grades = [85, 92, 78, 95, 88]

total = 0

for grade in grades:
    total += grade

average = total / len(grades)

print("Average grade:", average)


# EXAMPLE 18: Security Event Processing
#
# Simulate processing five events.

for event in range(1, 6):
    print("Processing security event:", event)

print("Security event processing completed.")


# EXAMPLE 19: Checking Network Ports
#
# This example processes a predefined
# list of port numbers.
#
# It does not perform a network scan.

ports = [22, 80, 443, 3389]

for port in ports:
    print("Reviewing port:", port)


# EXAMPLE 20: Counting Failed Login Events

login_events = [
    "success",
    "failed",
    "failed",
    "success",
    "failed"
]

failed_count = 0

for event in login_events:
    if event == "failed":
        failed_count += 1

print("Failed login events:", failed_count)


# EXAMPLE 21: Using enumerate()
#
# enumerate() provides an index
# alongside each item in a sequence.

tools = ["Python", "Linux", "Wireshark"]

for index, tool in enumerate(tools, start=1):
    print(index, tool)


# EXAMPLE 22: Using For Loops in Functions

def display_numbers(start, stop):
    for number in range(start, stop + 1):
        print(number)


display_numbers(1, 5)


# EXAMPLE 23: For Loop with User Input

number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)


# EXAMPLE 24: For Loop with else
#
# The else block executes when the
# loop finishes without encountering break.

for number in range(1, 4):
    print("Iteration:", number)
else:
    print("Loop completed normally.")


# EXAMPLE 25: Comparing For and While Loops
#
# Both examples display numbers 1 through 5.

print("Using a for loop:")

for number in range(1, 6):
    print(number)


print("Using a while loop:")

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# WHAT I LEARNED
#
# 1. for loops iterate through sequences.
# 2. range() generates integer sequences.
# 3. range() excludes the stop value.
# 4. A step controls how values change.
# 5. Strings can be iterated character by character.
# 6. Lists can be processed using loops.
# 7. for loops can perform calculations.
# 8. break exits a loop.
# 9. continue skips an iteration.
# 10. Nested loops repeat within other loops.
# 11. enumerate() provides item indexes.
# 12. Functions can contain for loops.
# 13. for and while loops serve different needs.
