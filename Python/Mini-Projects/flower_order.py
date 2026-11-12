
# ==========================================
# DAY 25 - FLOWER ORDERING MINI-PROJECT
# ==========================================
#
# Project: Golden Aura Florals
# Application: Flower Ordering System
# Language: Python
# Status: Reference project - Review pending
#
# ==========================================
# PROJECT OVERVIEW
# ==========================================
#
# This project combines concepts
# from Days 1 through 24.
#
# Concepts practiced:
#
# Printing and formatting
# Variables and data types
# Arithmetic operators
# User input
# Conditional statements
# Boolean logic
# While loops
# For loops
# Functions
# Parameters and return values
# Variable scope
# Strings and string methods
# Lists and dictionaries
# Nested data structures
# Input validation
# Error messages
# Inventory management
# Order processing
# Reporting
#
# IMPORTANT:
#
# This is a training application.
#
# It does not connect to Shopify.
# It does not process real payments.
# It does not store customer data
# in a database.
#
# Prices and inventory values
# are fictional examples.
#
# The demonstration runs without
# interactive input.
#
# Interactive mode is optional.


# ==========================================
# SECTION 1 - APPLICATION SETTINGS
# ==========================================

STORE_NAME = "Golden Aura Florals"

CURRENCY_SYMBOL = "$"

MAX_ORDER_QUANTITY = 25

SUPPORTED_DELIVERY_CITIES = {
    "las cruces",
    "el paso"
}

# A fixed training tax rate.
#
# This is not a representation
# of actual local tax rules.

TRAINING_TAX_RATE = 0.00

# Example delivery fees only.

DELIVERY_FEES = {
    "las cruces": 10.00,
    "el paso": 20.00
}


# ==========================================
# SECTION 2 - PRODUCT CATALOG
# ==========================================

# Each product has:
#
# ID
# Name
# Category
# Price
# Available stock
#
# Product prices are fictional.

PRODUCT_CATALOG = {
    "F001": {
        "name": "Classic Rose Bouquet",
        "category": "Roses",
        "price": 75.00,
        "stock": 20
    },
    "F002": {
        "name": "Luxury Rose Bouquet",
        "category": "Roses",
        "price": 125.00,
        "stock": 15
    },
    "F003": {
        "name": "Tulip Arrangement",
        "category": "Tulips",
        "price": 65.00,
        "stock": 18
    },
    "F004": {
        "name": "Mixed Floral Bouquet",
        "category": "Mixed Flowers",
        "price": 85.00,
        "stock": 25
    },
    "F005": {
        "name": "Premium Floral Arrangement",
        "category": "Luxury",
        "price": 175.00,
        "stock": 10
    }
}


# ==========================================
# SECTION 3 - APPLICATION DATA
# ==========================================

# Completed training orders
# are stored in this list.

ORDER_HISTORY = []

# Order numbers start at 1001.

NEXT_ORDER_NUMBER = 1001


# ==========================================
# SECTION 4 - DISPLAY FUNCTIONS
# ==========================================

def display_header():
    print("=" * 50)
    print(STORE_NAME.upper())
    print("FLOWER ORDERING SYSTEM")
    print("=" * 50)


def display_separator():
    print("-" * 50)


def format_money(amount):
    return f"{CURRENCY_SYMBOL}{amount:.2f}"


def display_welcome():
    display_header()

    print("Welcome to our flower ordering system.")
    print("Browse bouquets and create sample orders.")

    display_separator()


# ==========================================
# SECTION 5 - PRODUCT FUNCTIONS
# ==========================================

def display_catalog(catalog):
    print("\nAVAILABLE FLOWER PRODUCTS")

    display_separator()

    for product_id, product in catalog.items():
        print("Product ID:", product_id)
        print("Name:", product["name"])
        print("Category:", product["category"])

        print(
            "Price:",
            format_money(product["price"])
        )

        print("Stock:", product["stock"])

        display_separator()


def product_exists(catalog, product_id):
    return product_id in catalog


def get_product(catalog, product_id):
    return catalog.get(product_id)


def get_product_price(catalog, product_id):
    product = get_product(catalog, product_id)

    if product is None:
        return None

    return product["price"]


def get_product_stock(catalog, product_id):
    product = get_product(catalog, product_id)

    if product is None:
        return None

    return product["stock"]


# ==========================================
# SECTION 6 - VALIDATION FUNCTIONS
# ==========================================

def validate_customer_name(name):
    if not isinstance(name, str):
        return False

    cleaned = name.strip()

    return 2 <= len(cleaned) <= 60


def validate_product_id(catalog, product_id):
    if not isinstance(product_id, str):
        return False

    return product_id in catalog


def validate_quantity(quantity):
    if isinstance(quantity, bool):
        return False

    if not isinstance(quantity, int):
        return False

    return 1 <= quantity <= MAX_ORDER_QUANTITY


def normalize_delivery_city(city):
    if not isinstance(city, str):
        return None

    return city.strip().casefold()


def validate_delivery_city(city):
    normalized = normalize_delivery_city(city)

    return normalized in SUPPORTED_DELIVERY_CITIES


def validate_order_items(catalog, items):
    errors = []

    if not isinstance(items, list) or not items:
        return False, ["Order must contain items."]

    requested_quantities = {}

    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            errors.append(
                f"Item {index} must be a dictionary."
            )
            continue

        product_id = item.get("product_id")
        quantity = item.get("quantity")

        if not validate_product_id(catalog, product_id):
            errors.append(
                f"Item {index}: Invalid product ID."
            )
            continue

        if not validate_quantity(quantity):
            errors.append(
                f"Item {index}: Invalid quantity."
            )
            continue

        requested_quantities[product_id] = (
            requested_quantities.get(product_id, 0)
            + quantity
        )

    for product_id, requested in requested_quantities.items():
        available = catalog[product_id]["stock"]

        if requested > available:
            errors.append(
                f"{product_id}: Requested {requested}, "
                f"but only {available} available."
            )

    return len(errors) == 0, errors


def validate_order(catalog, order):
    errors = []

    if not isinstance(order, dict):
        return False, ["Order must be a dictionary."]

    customer = order.get("customer")
    delivery_city = order.get("delivery_city")
    items = order.get("items")

    if not validate_customer_name(customer):
        errors.append("Invalid customer name.")

    if not validate_delivery_city(delivery_city):
        errors.append("Unsupported delivery city.")

    items_valid, item_errors = validate_order_items(
        catalog,
        items
    )

    if not items_valid:
        errors.extend(item_errors)

    return len(errors) == 0, errors


# ==========================================
# SECTION 7 - CALCULATION FUNCTIONS
# ==========================================

def calculate_line_total(price, quantity):
    return round(price * quantity, 2)


def calculate_subtotal(catalog, items):
    subtotal = 0.00

    for item in items:
        product_id = item["product_id"]
        quantity = item["quantity"]

        price = catalog[product_id]["price"]

        subtotal += calculate_line_total(
            price,
            quantity
        )

    return round(subtotal, 2)


def calculate_delivery_fee(city):
    normalized = normalize_delivery_city(city)

    return DELIVERY_FEES.get(normalized)


def calculate_tax(subtotal):
    return round(
        subtotal * TRAINING_TAX_RATE,
        2
    )


def calculate_order_total(
    subtotal,
    delivery_fee,
    tax
):
    return round(
        subtotal + delivery_fee + tax,
        2
    )


# ==========================================
# SECTION 8 - INVENTORY FUNCTIONS
# ==========================================

def has_sufficient_stock(
    catalog,
    product_id,
    quantity
):
    if not validate_product_id(catalog, product_id):
        return False

    if not validate_quantity(quantity):
        return False

    return catalog[product_id]["stock"] >= quantity


def reduce_stock(catalog, product_id, quantity):
    if not has_sufficient_stock(
        catalog,
        product_id,
        quantity
    ):
        return False

    catalog[product_id]["stock"] -= quantity

    return True


def display_inventory(catalog):
    print("\nCURRENT INVENTORY")

    display_separator()

    for product_id, product in catalog.items():
        print(
            product_id,
            "-",
            product["name"],
            "- Stock:",
            product["stock"]
        )


def get_low_stock_products(catalog, threshold=5):
    low_stock = []

    for product_id, product in catalog.items():
        if product["stock"] <= threshold:
            low_stock.append({
                "product_id": product_id,
                "name": product["name"],
                "stock": product["stock"]
            })

    return low_stock


# ==========================================
# SECTION 9 - ORDER PROCESSING
# ==========================================

def create_order_record(
    order_number,
    customer,
    delivery_city,
    items,
    subtotal,
    delivery_fee,
    tax,
    total
):
    return {
        "order_number": order_number,
        "customer": customer,
        "delivery_city": delivery_city,
        "items": items,
        "subtotal": subtotal,
        "delivery_fee": delivery_fee,
        "tax": tax,
        "total": total,
        "status": "Accepted - Training"
    }


def process_order(catalog, order, history):
    global NEXT_ORDER_NUMBER

    valid, errors = validate_order(
        catalog,
        order
    )

    if not valid:
        return {
            "accepted": False,
            "errors": errors
        }

    customer = order["customer"].strip()

    delivery_city = normalize_delivery_city(
        order["delivery_city"]
    )

    items = []

    for item in order["items"]:
        product_id = item["product_id"]
        quantity = item["quantity"]

        product = catalog[product_id]

        items.append({
            "product_id": product_id,
            "product_name": product["name"],
            "quantity": quantity,
            "unit_price": product["price"],
            "line_total": calculate_line_total(
                product["price"],
                quantity
            )
        })

    subtotal = calculate_subtotal(
        catalog,
        order["items"]
    )

    delivery_fee = calculate_delivery_fee(
        delivery_city
    )

    tax = calculate_tax(subtotal)

    total = calculate_order_total(
        subtotal,
        delivery_fee,
        tax
    )

    # Validation has checked aggregate
    # quantities for each product ID.
    #
    # This training program runs
    # sequentially in one process.
    #
    # Real multi-user systems need
    # transactional inventory updates.

    for item in order["items"]:
        reduce_stock(
            catalog,
            item["product_id"],
            item["quantity"]
        )

    order_record = create_order_record(
        NEXT_ORDER_NUMBER,
        customer,
        delivery_city,
        items,
        subtotal,
        delivery_fee,
        tax,
        total
    )

    history.append(order_record)

    NEXT_ORDER_NUMBER += 1

    return {
        "accepted": True,
        "order": order_record
    }


# ==========================================
# SECTION 10 - RECEIPT FUNCTIONS
# ==========================================

def display_receipt(order):
    print("\n" + "=" * 50)

    print(STORE_NAME.upper())
    print("CUSTOMER ORDER RECEIPT")

    display_separator()

    print("Order Number:", order["order_number"])
    print("Customer:", order["customer"])
    print("Delivery City:", order["delivery_city"])
    print("Status:", order["status"])

    display_separator()

    for item in order["items"]:
        print("Product:", item["product_name"])
        print("Quantity:", item["quantity"])

        print(
            "Unit Price:",
            format_money(item["unit_price"])
        )

        print(
            "Line Total:",
            format_money(item["line_total"])
        )

        display_separator()

    print(
        "Subtotal:",
        format_money(order["subtotal"])
    )

    print(
        "Delivery Fee:",
        format_money(order["delivery_fee"])
    )

    print(
        "Training Tax:",
        format_money(order["tax"])
    )

    print(
        "TOTAL:",
        format_money(order["total"])
    )

    print("=" * 50)


def display_order_result(result):
    if not result["accepted"]:
        print("\nORDER REJECTED")

        for error in result["errors"]:
            print("Error:", error)

        return

    display_receipt(result["order"])


# ==========================================
# SECTION 11 - ORDER HISTORY
# ==========================================

def display_order_history(history):
    print("\nORDER HISTORY")

    display_separator()

    if not history:
        print("No accepted orders recorded.")
        return

    for order in history:
        print("Order:", order["order_number"])
        print("Customer:", order["customer"])

        print(
            "Total:",
            format_money(order["total"])
        )

        print("Status:", order["status"])

        display_separator()


def find_order(history, order_number):
    for order in history:
        if order["order_number"] == order_number:
            return order

    return None


def count_accepted_orders(history):
    return len(history)


# ==========================================
# SECTION 12 - SALES REPORTING
# ==========================================

def calculate_total_sales(history):
    total = 0.00

    for order in history:
        total += order["total"]

    return round(total, 2)


def calculate_average_order_value(history):
    if not history:
        return 0.00

    return round(
        calculate_total_sales(history) / len(history),
        2
    )


def count_products_sold(history):
    product_counts = {}

    for order in history:
        for item in order["items"]:
            product_id = item["product_id"]

            product_counts[product_id] = (
                product_counts.get(product_id, 0)
                + item["quantity"]
            )

    return product_counts


def display_sales_report(history):
    print("\nSALES REPORT")

    display_separator()

    print(
        "Accepted Orders:",
        count_accepted_orders(history)
    )

    print(
        "Total Order Value:",
        format_money(calculate_total_sales(history))
    )

    print(
        "Average Order Value:",
        format_money(
            calculate_average_order_value(history)
        )
    )

    print("Products Sold:")

    product_counts = count_products_sold(history)

    if not product_counts:
        print("No products sold.")

    for product_id, quantity in product_counts.items():
        print(product_id, "-", quantity)


# ==========================================
# SECTION 13 - SAMPLE ORDER DATA
# ==========================================

# All customer names are fictional.
#
# These orders do not represent
# real business transactions.

SAMPLE_ORDERS = [
    {
        "customer": "Alex Morgan",
        "delivery_city": "Las Cruces",
        "items": [
            {
                "product_id": "F001",
                "quantity": 2
            },
            {
                "product_id": "F003",
                "quantity": 1
            }
        ]
    },
    {
        "customer": "Taylor Jordan",
        "delivery_city": "El Paso",
        "items": [
            {
                "product_id": "F005",
                "quantity": 1
            }
        ]
    },
    {
        "customer": "Casey Rivera",
        "delivery_city": "Las Cruces",
        "items": [
            {
                "product_id": "F002",
                "quantity": 3
            }
        ]
    },
    {
        "customer": "Invalid Example",
        "delivery_city": "Phoenix",
        "items": [
            {
                "product_id": "F999",
                "quantity": -2
            }
        ]
    }
]


# ==========================================
# SECTION 14 - DEMONSTRATION
# ==========================================

def run_demonstration():
    display_welcome()

    display_catalog(PRODUCT_CATALOG)

    print("\nPROCESSING SAMPLE ORDERS")

    for sample_order in SAMPLE_ORDERS:
        result = process_order(
            PRODUCT_CATALOG,
            sample_order,
            ORDER_HISTORY
        )

        display_order_result(result)

    display_inventory(PRODUCT_CATALOG)

    display_order_history(ORDER_HISTORY)

    display_sales_report(ORDER_HISTORY)

    low_stock = get_low_stock_products(
        PRODUCT_CATALOG
    )

    print("\nLOW STOCK PRODUCTS")

    if not low_stock:
        print("No products below the threshold.")

    for product in low_stock:
        print(
            product["name"],
            "-",
            product["stock"]
        )


# ==========================================
# SECTION 15 - OPTIONAL INTERACTIVE INPUT
# ==========================================

# This section uses input().
#
# It runs only if interactive mode
# is selected at the bottom
# of this file.


def request_customer_name():
    while True:
        name = input(
            "Enter customer name: "
        ).strip()

        if validate_customer_name(name):
            return name

        print("Invalid customer name.")


def request_delivery_city():
    while True:
        city = input(
            "Enter delivery city: "
        )

        if validate_delivery_city(city):
            return city

        print("Unsupported delivery city.")


def request_product_id(catalog):
    while True:
        product_id = input(
            "Enter product ID: "
        ).strip().upper()

        if validate_product_id(catalog, product_id):
            return product_id

        print("Invalid product ID.")


def request_quantity():
    while True:
        quantity_text = input(
            "Enter quantity: "
        ).strip()

        if not quantity_text.isascii():
            print("Enter ASCII digits only.")
            continue

        if not quantity_text.isdecimal():
            print("Enter a whole number.")
            continue

        quantity = int(quantity_text)

        if validate_quantity(quantity):
            return quantity

        print("Quantity is outside the allowed range.")


def request_order_items(catalog):
    items = []

    while True:
        display_catalog(catalog)

        product_id = request_product_id(catalog)
        quantity = request_quantity()

        items.append({
            "product_id": product_id,
            "quantity": quantity
        })

        response = input(
            "Add another product? (yes/no): "
        ).strip().casefold()

        if response != "yes":
            break

    return items


def create_interactive_order(catalog):
    customer = request_customer_name()

    delivery_city = request_delivery_city()

    items = request_order_items(catalog)

    return {
        "customer": customer,
        "delivery_city": delivery_city,
        "items": items
    }


# ==========================================
# SECTION 16 - INTERACTIVE MENU
# ==========================================

def display_menu():
    print("\nMAIN MENU")
    print("1. View Product Catalog")
    print("2. Create Flower Order")
    print("3. View Inventory")
    print("4. View Order History")
    print("5. View Sales Report")
    print("6. Exit")


def run_interactive_menu():
    display_welcome()

    while True:
        display_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            display_catalog(PRODUCT_CATALOG)

        elif choice == "2":
            order = create_interactive_order(
                PRODUCT_CATALOG
            )

            result = process_order(
                PRODUCT_CATALOG,
                order,
                ORDER_HISTORY
            )

            display_order_result(result)

        elif choice == "3":
            display_inventory(PRODUCT_CATALOG)

        elif choice == "4":
            display_order_history(ORDER_HISTORY)

        elif choice == "5":
            display_sales_report(ORDER_HISTORY)

        elif choice == "6":
            print("Thank you for visiting!")
            break

        else:
            print("Invalid menu selection.")


# ==========================================
# SECTION 17 - PROGRAM ENTRY POINT
# ==========================================

# The demonstration is the default.
#
# Change RUN_INTERACTIVE_MODE to True
# when you are ready to practice
# entering orders manually.

RUN_INTERACTIVE_MODE = False


if __name__ == "__main__":
    if RUN_INTERACTIVE_MODE:
        run_interactive_menu()
    else:
        run_demonstration()


# ==========================================
# PROJECT REVIEW NOTES
# ==========================================
#
# 1. Dictionaries store product data.
# 2. Lists store orders and order items.
# 3. Functions organize application logic.
# 4. Parameters pass information.
# 5. Return values communicate results.
# 6. Validation checks order information.
# 7. Loops process multiple products.
# 8. Conditionals handle decisions.
# 9. Boolean values represent outcomes.
# 10. Inventory is checked before sale.
# 11. Order totals are calculated.
# 12. Receipts display purchase details.
# 13. Accepted orders enter order history.
# 14. Invalid orders are rejected.
# 15. Sales reports summarize orders.
# 16. The menu supports user interaction.
# 17. The demo runs without user input.
# 18. The program uses synthetic records.
# 19. Prices and fees are examples only.
# 20. The project is not production-ready.
#
# FUTURE IMPROVEMENTS:
#
# Save orders to files.
# Load inventory from CSV.
# Use Decimal for monetary values.
# Add order cancellation.
# Add inventory restocking.
# Add customer order lookup.
# Improve input handling.
# Add automated tests.
# Add database storage.
# Add a graphical interface.
# Add secure authentication.
# Add transactional inventory updates.
#
# Future lessons will introduce
# several of these concepts.
