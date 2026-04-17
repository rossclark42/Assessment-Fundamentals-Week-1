"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list:
    for product in basket:
        if product["name"] == item["name"] and product["price"] == item["price"]:
            product["quantity"] += 1
            return basket
    else:
        basket.append(
            {"name": item["name"], "price": item["price"], "quantity": 1})
    return basket


def generate_receipt(basket: list) -> str:
    receipt = ""
    grand_total = 0
    if len(basket) == 0:
        receipt = "Basket is empty"
        return receipt
    else:
        for item in basket:
            total = item["price"] * item["quantity"]
            total_str = "Free" if total == 0 else f"£{total:.2f}"
            grand_total += total

            receipt += f"{item["name"]} x {item["quantity"]} - {total_str}\n"
    receipt += f"Total: £{grand_total:.2f}"
    return receipt  # return the receipt string

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
