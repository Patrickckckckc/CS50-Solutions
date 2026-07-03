def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    elif len(s) > 6 or len(s) < 2:
        return False
    # Needs to end in numbers
    for i, char in enumerate(s):
        if char.isnumeric():
            # First Number cannot be 0
            if char == "0":
                return False
            elif not s[i:].isdigit():
                return False
            else:
                return True
    return True


main()
