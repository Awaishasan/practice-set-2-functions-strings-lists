# Task 2: Shopping Bill Calculator
# Topics: Lists, Functions, String Manipulation and Input Validation

items = []
prices = []
quantities = []


def add_item(name, price, qty):
    """Add one item to the bill lists."""
    items.append(name)
    prices.append(price)
    quantities.append(qty)


def calculate_subtotal():
    """Return the subtotal: sum of (price x quantity) for all items."""
    subtotal = 0
    for price, qty in zip(prices, quantities):
        subtotal += price * qty
    return subtotal


def apply_discount(subtotal):
    """Return (discount_amount, discount_rate).

    10% discount if subtotal is above 5000, otherwise 5%.
    """
    if subtotal > 5000:
        rate = 10
    else:
        rate = 5
    discount = subtotal * rate / 100
    return discount, rate


def fmt(n):
    """Show whole numbers without '.0' (250 instead of 250.0)."""
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n


def print_bill():
    """Print a well-formatted bill with subtotal, discount, GST and total."""
    subtotal = calculate_subtotal()
    discount, rate = apply_discount(subtotal)
    discounted_amount = subtotal - discount
    gst_rate = 5
    gst = discounted_amount * gst_rate / 100
    grand_total = discounted_amount + gst

    print("----------------------------------------")
    print("            SHOPPING BILL")
    print("----------------------------------------")
    print(f"{'Item':<12} {'Price':<10} {'Qty':<8} {'Total':<10}")
    print("----------------------------------------")
    for name, price, qty in zip(items, prices, quantities):
        total = price * qty
        print(f"{name:<12} {fmt(price):<10} {qty:<8} {fmt(total):<10}")
    print("----------------------------------------")
    print(f"Subtotal: {fmt(subtotal)}")
    print(f"Discount ({rate}%) : {fmt(discount)}")
    print(f"GST ({gst_rate}%) : {gst:.2f}")
    print(f"Grand Total: {grand_total:.2f}")
    print("----------------------------------------")


def get_item_count():
    """Ask how many items to add. The bill must include at least 3 items."""
    while True:
        count = input("How many items do you want to add to the bill? ").strip()
        if not count.isdigit():
            print("Invalid input! Please enter a whole number.")
            continue
        count = int(count)
        if count < 3:
            print("Error! The bill must include at least 3 items. Please try again.")
            continue
        return count


def get_price():
    """Ask for a price. It must be a number greater than 0."""
    while True:
        price = input("Enter price: ").strip()
        try:
            price = float(price)
        except ValueError:
            print("Invalid input! Price must be a number.")
            continue
        if price <= 0:
            print("Invalid price! Price must be greater than 0.")
            continue
        return price


def get_quantity():
    """Ask for a quantity. It must be a whole number."""
    while True:
        qty = input("Enter quantity: ").strip()
        if not qty.isdigit():
            print("Invalid input! Quantity must be a whole number.")
            continue
        return int(qty)


def main():
    count = get_item_count()
    for i in range(count):
        print(f"\nItem {i + 1}:")
        while True:
            name = input("Enter item name: ").strip().title()
            if name:
                break
            print("Item name cannot be empty!")
        price = get_price()
        qty = get_quantity()
        add_item(name, price, qty)

    print()
    print_bill()


if __name__ == "__main__":
    main()
