"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    lines = receipt_string.split("\n")
    invoice = "VAT RECEIPT\n\n"
    net_total = 0
    vat_total = 0

    for line in lines:
        if "Total" in line:
            continue
        name_qty, price = line.split(" - ")
        name, qty = name_qty.split(" x ")
        qty = int(qty)
        gross_total = float(price.replace("£", ""))
        net = gross_total * 0.8
        vat = gross_total - net
        net_total += net
        vat_total += vat

        invoice += f"{name} x {qty} - £{net:.2f}\n"

    total_with_vat = net_total + vat_total
    invoice += f"\nTotal: £{net_total:.2f}\n"
    invoice += f"VAT: £{vat_total:.2f}\n"
    invoice += f"Total inc VAT: £{total_with_vat:.2f}"
    return invoice  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
