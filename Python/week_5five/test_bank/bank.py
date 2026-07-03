def main():
    text = input("Write: ")
    money = value(text)
    print(f"${money}")


def value(greeting):
    greeting = greeting.upper()
    if greeting.startswith("HELLO"):
        return 0
    elif greeting.startswith("H"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
