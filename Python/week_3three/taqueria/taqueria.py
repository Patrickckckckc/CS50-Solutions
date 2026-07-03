def main():
    total = float(order())
    print(f"\nTotal: ${total:.2f}")


def order():
    taqueria_menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Take Order until Control D is press
    total = 0.00
    while True:
        try:
            item = input("Item: ")
            if item.title() in taqueria_menu.keys():
                total = total + taqueria_menu[item.title()]
                print(f"${total:.2f}")
        except EOFError:
            return total


main()
