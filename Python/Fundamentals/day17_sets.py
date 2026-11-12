
# ==========================================
# DAY 17 - SETS AND UNIQUE DATA
# Topic: Working with Sets in Python
# ==========================================

# LESSON NOTES
#
# A set is a collection of unique values.
#
# Sets are useful when duplicate
# elements are not needed.
#
# Sets are:
#
# 1. Unordered
# 2. Mutable
# 3. Unable to contain duplicate elements
# 4. Able to contain hashable values
#
# Sets do not support indexing
# or slicing.
#
# A set can contain strings, numbers,
# and tuples of hashable values.
#
# Lists and dictionaries cannot
# be elements of a regular set.
#
# Sets are useful for:
#
# Removing duplicate data
# Comparing collections
# Tracking unique IP addresses
# Finding shared permissions
# Managing unique inventory items
# Analyzing security records


# EXAMPLE 1: Creating a Set

languages = {"Python", "C", "C++"}

print("Languages:", languages)


# EXAMPLE 2: Checking the Data Type

tools = {"Wireshark", "Nmap", "Python"}

print("Data type:", type(tools))


# EXAMPLE 3: Creating an Empty Set
#
# {} creates an empty dictionary.
#
# set() creates an empty set.

empty_set = set()

print("Empty set:", empty_set)
print("Type:", type(empty_set))


# EXAMPLE 4: Removing Duplicate Values
#
# Sets automatically remove duplicates.

numbers = {10, 20, 20, 30, 30, 40}

print("Unique numbers:", numbers)


# EXAMPLE 5: Converting a List to a Set
#
# set() creates a set from an iterable.

languages = [
    "Python",
    "C",
    "Python",
    "C++",
    "C"
]

unique_languages = set(languages)

print("Unique languages:", unique_languages)


# EXAMPLE 6: Converting a Set to a List
#
# list() converts a set into a list.
#
# The resulting order is not guaranteed.

tools = {"Wireshark", "Nmap", "Python"}

tools_list = list(tools)

print("Tools list:", tools_list)


# EXAMPLE 7: Set Length
#
# len() counts unique elements.

numbers = {10, 20, 30, 40}

print("Number of elements:", len(numbers))


# EXAMPLE 8: Set Membership
#
# in checks whether an element
# belongs to a set.

tools = {"Wireshark", "Nmap", "Python"}

print("Python" in tools)
print("Java" in tools)


# EXAMPLE 9: Using not in

authorized_roles = {
    "admin",
    "analyst",
    "employee"
}

role = "guest"

if role not in authorized_roles:
    print("Role is not in the approved set.")
else:
    print("Role is in the approved set.")


# EXAMPLE 10: Iterating Through a Set
#
# Sets have no guaranteed order.
#
# A for loop can process each element.

languages = {"Python", "C", "C++"}

for language in languages:
    print("Language:", language)


# EXAMPLE 11: Adding an Element
#
# add() inserts one element.

tools = {"Wireshark", "Nmap"}

tools.add("Python")

print("Updated tools:", tools)


# EXAMPLE 12: Adding a Duplicate
#
# Adding an existing element
# does not create a duplicate.

tools = {"Wireshark", "Nmap"}

tools.add("Nmap")

print("Tools:", tools)


# EXAMPLE 13: Adding Multiple Elements
#
# update() adds elements from
# one or more iterables.

tools = {"Wireshark", "Nmap"}

tools.update(["Python", "Linux", "Git"])

print("Updated tools:", tools)


# EXAMPLE 14: Removing an Element
#
# remove() deletes an element.
#
# It raises KeyError if the
# element does not exist.

tools = {"Wireshark", "Nmap", "Python"}

tools.remove("Nmap")

print("Updated tools:", tools)


# EXAMPLE 15: Using discard()
#
# discard() removes an element
# if it exists.
#
# It does not raise an error
# if the element is absent.

tools = {"Wireshark", "Nmap", "Python"}

tools.discard("Java")

print("Tools:", tools)


# EXAMPLE 16: Using pop()
#
# pop() removes and returns
# an arbitrary element.
#
# It does not necessarily remove
# the first or last element.
#
# Calling pop() on an empty set
# raises KeyError.

numbers = {10, 20, 30}

removed = numbers.pop()

print("Removed:", removed)
print("Remaining:", numbers)


# EXAMPLE 17: Using clear()
#
# clear() removes every element.

numbers = {10, 20, 30}

numbers.clear()

print("Cleared set:", numbers)


# EXAMPLE 18: Copying a Set
#
# copy() creates a shallow copy.

original = {"Python", "C", "C++"}

copied = original.copy()

copied.add("Java")

print("Original:", original)
print("Copied:", copied)


# EXAMPLE 19: Set References
#
# Assignment creates another
# reference to the same set.

original = {"Python", "C"}

reference = original

reference.add("C++")

print("Original:", original)
print("Reference:", reference)


# EXAMPLE 20: Set Union
#
# union() combines unique values
# from both sets.
#
# The | operator also performs union.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

combined = set_a.union(set_b)

print("Union:", combined)
print("Union operator:", set_a | set_b)


# EXAMPLE 21: Set Intersection
#
# intersection() finds values
# present in both sets.
#
# The & operator also works.

set_a = {1, 2, 3}
set_b = {2, 3, 4}

shared = set_a.intersection(set_b)

print("Intersection:", shared)
print("Intersection operator:", set_a & set_b)


# EXAMPLE 22: Set Difference
#
# difference() finds elements
# in the first set but not
# in the second.
#
# The - operator also works.

set_a = {1, 2, 3}
set_b = {2, 3, 4}

difference = set_a.difference(set_b)

print("A minus B:", difference)
print("Difference operator:", set_a - set_b)


# EXAMPLE 23: Symmetric Difference
#
# symmetric_difference() finds
# elements present in exactly
# one of the two sets.
#
# The ^ operator also works.

set_a = {1, 2, 3}
set_b = {2, 3, 4}

unique_to_one = set_a.symmetric_difference(set_b)

print("Symmetric difference:", unique_to_one)
print("Operator:", set_a ^ set_b)


# EXAMPLE 24: Checking Subsets
#
# issubset() checks whether
# every element of one set
# appears in another set.

required = {"read", "write"}

permissions = {"read", "write", "execute"}

print("Subset:", required.issubset(permissions))


# EXAMPLE 25: Checking Supersets
#
# issuperset() checks whether
# a set contains every element
# of another set.

permissions = {"read", "write", "execute"}

required = {"read", "write"}

print("Superset:", permissions.issuperset(required))


# EXAMPLE 26: Checking Disjoint Sets
#
# isdisjoint() returns True when
# two sets share no elements.

set_a = {1, 2, 3}
set_b = {4, 5, 6}

print("Disjoint:", set_a.isdisjoint(set_b))


# EXAMPLE 27: Updating with Union
#
# update() changes the original set.

set_a = {1, 2}
set_b = {2, 3, 4}

set_a.update(set_b)

print("Updated set:", set_a)


# EXAMPLE 28: Intersection Update
#
# intersection_update() keeps only
# elements shared by both sets.

set_a = {1, 2, 3, 4}
set_b = {2, 4, 6}

set_a.intersection_update(set_b)

print("Shared values:", set_a)


# EXAMPLE 29: Difference Update
#
# difference_update() removes
# elements found in another set.

set_a = {1, 2, 3, 4}
set_b = {2, 4}

set_a.difference_update(set_b)

print("Remaining:", set_a)


# EXAMPLE 30: Symmetric Difference Update
#
# symmetric_difference_update()
# keeps elements belonging to
# exactly one of the sets.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

set_a.symmetric_difference_update(set_b)

print("Updated set:", set_a)


# EXAMPLE 31: Sorting Set Values
#
# Sets themselves are unordered.
#
# sorted() returns a sorted list.

numbers = {50, 10, 40, 20, 30}

sorted_numbers = sorted(numbers)

print("Sorted values:", sorted_numbers)


# EXAMPLE 32: Set Comprehension
#
# A set comprehension creates
# a set from an expression.

squares = {
    number ** 2
    for number in range(1, 6)
}

print("Squares:", squares)


# EXAMPLE 33: Filtering with Set Comprehension

numbers = {1, 2, 3, 4, 5, 6, 7, 8}

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print("Even numbers:", even_numbers)


# EXAMPLE 34: Immutable Set with frozenset()
#
# frozenset is an immutable
# set-like collection.
#
# Elements cannot be added
# or removed after creation.

fixed_permissions = frozenset({
    "read",
    "write"
})

print("Fixed permissions:", fixed_permissions)


# EXAMPLE 35: Flower Inventory Varieties

flowers = {
    "Roses",
    "Tulips",
    "Lilies",
    "Orchids"
}

for flower in sorted(flowers):
    print("Available flower:", flower)


# EXAMPLE 36: Removing Duplicate Orders
#
# A set can identify unique
# order IDs from repeated values.
#
# In a real system, duplicate
# records should be investigated
# rather than automatically deleted.

order_ids = [
    "001",
    "002",
    "003",
    "002",
    "004",
    "001"
]

unique_order_ids = set(order_ids)

print("Unique order IDs:", sorted(unique_order_ids))


# EXAMPLE 37: Comparing Flower Inventory

store_a = {"Roses", "Tulips", "Lilies"}
store_b = {"Roses", "Orchids", "Lilies"}

shared_flowers = store_a & store_b

print("Shared flowers:", sorted(shared_flowers))


# EXAMPLE 38: Unique Security IP Addresses
#
# These are documentation IP addresses.
#
# This example does not connect
# to any external system.

source_ips = [
    "192.0.2.10",
    "192.0.2.20",
    "192.0.2.10",
    "198.51.100.5",
    "192.0.2.20"
]

unique_ips = set(source_ips)

print("Unique IPs:", sorted(unique_ips))
print("Unique count:", len(unique_ips))


# EXAMPLE 39: Comparing Security Event Sources

server_a_ips = {
    "192.0.2.10",
    "192.0.2.20",
    "198.51.100.5"
}

server_b_ips = {
    "192.0.2.20",
    "198.51.100.5",
    "203.0.113.7"
}

shared_ips = server_a_ips & server_b_ips

print("Shared IPs:", sorted(shared_ips))


# EXAMPLE 40: Finding New IP Addresses

known_ips = {
    "192.0.2.10",
    "192.0.2.20"
}

observed_ips = {
    "192.0.2.10",
    "203.0.113.7"
}

new_ips = observed_ips - known_ips

print("Previously unseen IPs:", sorted(new_ips))


# EXAMPLE 41: Comparing User Permissions
#
# This example compares stored
# permission labels.
#
# It does not grant access.

user_permissions = {
    "read",
    "write"
}

required_permissions = {
    "read",
    "write",
    "execute"
}

missing_permissions = (
    required_permissions - user_permissions
)

print("Missing permissions:", missing_permissions)


# EXAMPLE 42: Finding Shared Security Tools

team_a_tools = {
    "Wireshark",
    "Nmap",
    "Python"
}

team_b_tools = {
    "Python",
    "Linux",
    "Wireshark"
}

shared_tools = team_a_tools.intersection(
    team_b_tools
)

print("Shared tools:", sorted(shared_tools))


# EXAMPLE 43: Unique Security Event Categories

events = [
    "login_success",
    "login_failed",
    "port_scan",
    "login_failed",
    "file_access",
    "port_scan"
]

unique_categories = set(events)

print("Event categories:", sorted(unique_categories))


# EXAMPLE 44: Using Sets in Functions

def find_shared_items(first_set, second_set):
    return first_set.intersection(second_set)


tools_a = {"Python", "Nmap", "Wireshark"}
tools_b = {"Python", "Linux", "Wireshark"}

result = find_shared_items(tools_a, tools_b)

print("Shared items:", sorted(result))


# EXAMPLE 45: Returning Unique Values

def remove_duplicates(items):
    return set(items)


events = [
    "failed",
    "success",
    "failed",
    "port_scan"
]

unique_events = remove_duplicates(events)

print("Unique events:", sorted(unique_events))


# EXAMPLE 46: Basic Security IP Report

source_ips = [
    "192.0.2.10",
    "192.0.2.20",
    "192.0.2.10",
    "203.0.113.7",
    "198.51.100.5",
    "203.0.113.7"
]

unique_ips = set(source_ips)

print("===== SECURITY IP REPORT =====")
print("Total IP observations:", len(source_ips))
print("Unique IP addresses:", len(unique_ips))

for ip in sorted(unique_ips):
    print("Observed IP:", ip)


# WHAT I LEARNED
#
# 1. Sets store unique elements.
# 2. Sets are unordered.
# 3. Sets are mutable.
# 4. Sets do not support indexing.
# 5. set() creates an empty set.
# 6. Duplicate elements are removed.
# 7. add() inserts one element.
# 8. update() adds iterable elements.
# 9. remove() deletes an element.
# 10. discard() removes safely.
# 11. pop() removes an arbitrary element.
# 12. clear() empties a set.
# 13. copy() creates a shallow copy.
# 14. union() combines unique values.
# 15. intersection() finds shared values.
# 16. difference() finds unmatched values.
# 17. symmetric_difference() finds
#     values belonging to one set only.
# 18. issubset() checks containment.
# 19. issuperset() checks containment.
# 20. isdisjoint() checks for no overlap.
# 21. Set comprehensions create sets.
# 22. frozenset creates immutable sets.
# 23. Sets help remove duplicates.
# 24. Sets help compare security records.
