
# ==========================================
# DAY 08 - WHILE LOOPS AND REPETITION
# Topic: Repeating Code with while
# ==========================================

# LESSON NOTES
#
# A loop allows a program to repeat
# instructions without rewriting them.
#
# A while loop repeats code as long as
# its condition evaluates to True.
#
# Python checks the condition before
# each repetition.
#
# Each repetition is called an iteration.
#
# The loop stops when the condition
# becomes False.
#
# A counter can track the number
# of iterations.
#
# IMPORTANT:
# If the condition never becomes False,
# the loop may continue indefinitely.
#
# This is called an infinite loop.


# EXAMPLE 1: Basic While Loop

count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print("Loop completed.")


# EXAMPLE 2: Counting Backward

count = 5

while count >= 1:
    print("Countdown:", count)
    count -= 1

print("Countdown finished.")


# EXAMPLE 3: Repeating a Message

repetitions = 0

while repetitions < 3:
    print("Welcome to my coding camp!")
    repetitions += 1


# EXAMPLE 4: Understanding Loop Conditions
#
# The condition is checked before
# the loop body executes.
#
# If the condition starts as False,
# the loop body will not run.

number = 10

while number < 5:
    print("This message will not appear.")

print("The condition was False.")


# EXAMPLE 5: Incrementing a Counter
#
# += increases the value of a variable.

counter = 0

while counter < 10:
    counter += 1
    print("Counter:", counter)


# EXAMPLE 6: Decrementing a Counter
#
# -= decreases the value of a variable.

remaining = 5

while remaining > 0:
    print("Remaining:", remaining)
    remaining -= 1


# EXAMPLE 7: Adding Numbers with a Loop

number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Sum of numbers 1 through 5:", total)


# EXAMPLE 8: Multiplication Table

number = 3
multiplier = 1

while multiplier <= 10:
    result = number * multiplier
    print(number, "x", multiplier, "=", result)
    multiplier += 1


# EXAMPLE 9: While Loop with User Input
#
# The program repeats until the user
# enters the expected response.

answer = ""

while answer != "yes":
    answer = input("Type yes to continue: ")
    answer = answer.strip().lower()

print("Thank you for continuing.")


# EXAMPLE 10: Using break
#
# break immediately exits the loop,
# even if its condition is still True.

counter = 1

while counter <= 10:
    if counter == 5:
        break

    print("Counter:", counter)
    counter += 1

print("Loop stopped using break.")


# EXAMPLE 11: Using continue
#
# continue skips the remaining statements
# in the current iteration.
#
# The loop then checks its condition again.

number = 0

while number < 10:
    number += 1

    if number == 5:
        continue

    print("Number:", number)


# EXAMPLE 12: While Loop with if and else

number = 1

while number <= 5:
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

    number += 1


# EXAMPLE 13: Flower Inventory Counter
#
# Simulate preparing five bouquets.

bouquets_prepared = 0
bouquets_needed = 5

while bouquets_prepared < bouquets_needed:
    bouquets_prepared += 1
    print("Bouquet prepared:", bouquets_prepared)

print("All bouquets are ready.")


# EXAMPLE 14: Tracking Remaining Inventory

roses = 50

while roses >= 10:
    roses -= 10
    print("Roses remaining:", roses)

print("Not enough roses for another group of 10.")


# EXAMPLE 15: Login Attempt Limit
#
# This is a simplified learning example.
# Real authentication systems require
# additional security protections.

correct_pin = "1234"
attempts = 0
max_attempts = 3
authenticated = False

while attempts < max_attempts:
    entered_pin = input("Enter demo PIN: ")
    attempts += 1

    if entered_pin == correct_pin:
        authenticated = True
        break
    else:
        print("Incorrect PIN.")

if authenticated:
    print("Demo login successful.")
else:
    print("Maximum attempts reached.")


# EXAMPLE 16: Menu with a While Loop
#
# The menu repeats until the user
# chooses to exit.

choice = ""

while choice != "3":
    print()
    print("===== MAIN MENU =====")
    print("1. View Account")
    print("2. Security Settings")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("Opening account.")
    elif choice == "2":
        print("Opening security settings.")
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid selection.")


# EXAMPLE 17: While True
#
# while True creates a loop that continues
# until a break statement stops it.
#
# Make sure there is a clear exit condition.

while True:
    response = input("Type quit to exit: ")

    if response.strip().lower() == "quit":
        print("Exiting loop.")
        break

    print("You entered:", response)


# EXAMPLE 18: Using a Boolean Flag
#
# A Boolean variable can control
# whether a loop continues.

running = True
counter = 0

while running:
    counter += 1
    print("Iteration:", counter)

    if counter == 5:
        running = False

print("Program stopped.")


# EXAMPLE 19: Nested While Loops
#
# A nested loop is a loop inside
# another loop.
#
# The inner loop completes its repetitions
# for each iteration of the outer loop.

row = 1

while row <= 3:
    column = 1

    while column <= 3:
        print("Row:", row, "Column:", column)
        column += 1

    row += 1


# EXAMPLE 20: Security Event Counter
#
# Simulate processing a fixed number
# of security events.

event_number = 1
total_events = 5

while event_number <= total_events:
    print("Processing security event:", event_number)
    event_number += 1

print("All events processed.")


# EXAMPLE 21: While Loop with a Function

def countdown(start):
    while start > 0:
        print(start)
        start -= 1

    print("Countdown complete.")


countdown(5)


# EXAMPLE 22: While Loop with else
#
# A while loop can have an else block.
#
# The else block runs when the loop
# finishes normally without break.

counter = 1

while counter <= 3:
    print("Iteration:", counter)
    counter += 1
else:
    print("Loop finished normally.")


# EXAMPLE 23: Avoiding Infinite Loops
#
# The following code is intentionally
# commented out because it would
# continue forever.
#
# counter = 1
#
# while counter <= 5:
#     print(counter)
#
# The problem is that counter never changes.
#
# Correct approach:

counter = 1

while counter <= 5:
    print("Safe counter:", counter)
    counter += 1


# WHAT I LEARNED
#
# 1. while loops repeat code conditionally.
# 2. Each repetition is an iteration.
# 3. Conditions are checked before execution.
# 4. Counters track repetitions.
# 5. += increments a variable.
# 6. -= decrements a variable.
# 7. break exits a loop immediately.
# 8. continue skips the current iteration.
# 9. Boolean flags can control loops.
# 10. Nested loops repeat within other loops.
# 11. while True requires a clear exit.
# 12. A while loop can have an else block.
# 13. Infinite loops occur when loops
#     never reach a stopping condition.
