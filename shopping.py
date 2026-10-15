from datetime import datetime

def get_number(prompt, minimum=0):
    while True:
        try:
            value = float(input(prompt))
            if value < minimum:
                print(f"Please enter a value >= {minimum}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def shopping_bill():
    items = []

    print("=" * 48)
    print("          SHOPPING BILL GENERATOR")
    print("=" * 48)

    customer = input("Enter customer name: ").strip() or "Customer"

    while True:
        name = input("\nEnter product name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            break

        if not name:
            print("Product name cannot be empty.")
            continue

        quantity = get_number("Enter quantity: ", 0.000001)
        price = get_number("Enter price per unit (Rs.): ")

        items.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        })

        print(f"Added {name} successfully!")

    if not items:
        print("\nNo products added. Bill cancelled.")
        return

    discount_rate = get_number("\nEnter discount (%): ")
    gst_rate = get_number("Enter GST (%): ")

    if discount_rate > 100:
        print("Discount cannot exceed 100%.")
        return

    subtotal = sum(item["total"] for item in items)
    discount = subtotal * discount_rate / 100
    taxable_amount = subtotal - discount
    gst = taxable_amount * gst_rate / 100
    grand_total = taxable_amount + gst

    now = datetime.now()

    # Generate the receipt
    bill = []
    bill.append("=" * 64)
    bill.append("                  SHOPPING BILL")
    bill.append("=" * 64)
    bill.append(f"Customer : {customer}")
    bill.append(f"Date     : {now.strftime('%d-%m-%Y %I:%M %p')}")
    bill.append("-" * 64)
    bill.append(
        f"{'Product':<18}{'Qty':>8}{'Price':>12}{'Amount':>14}"
    )
    bill.append("-" * 64)

    for item in items:
        bill.append(
            f"{item['name'][:18]:<18}"
            f"{item['quantity']:>8.2f}"
            f"{item['price']:>12.2f}"
            f"{item['total']:>14.2f}"
        )

    bill.append("-" * 64)
    bill.append(f"{'Subtotal:':>44} Rs. {subtotal:>10.2f}")
    bill.append(
        f"{'Discount (' + str(discount_rate) + '%):':>44}"
        f" Rs. {discount:>10.2f}"
    )
    bill.append(f"{'Taxable amount:':>44} Rs. {taxable_amount:>10.2f}")
    bill.append(
        f"{'GST (' + str(gst_rate) + '%):':>44} Rs. {gst:>10.2f}"
    )
    bill.append("=" * 64)
    bill.append(f"{'GRAND TOTAL:':>44} Rs. {grand_total:>10.2f}")
    bill.append("=" * 64)
    bill.append("             Thank you for shopping!")
    bill.append("=" * 64)

    receipt = "\n".join(bill)
    print("\n" + receipt)

    # Save receipt to a text file
    filename = f"bill_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(receipt)
        print(f"\nBill saved successfully as: {filename}")
    except OSError as error:
        print(f"\nCould not save bill: {error}")


if __name__ == "__main__":
    shopping_bill()
