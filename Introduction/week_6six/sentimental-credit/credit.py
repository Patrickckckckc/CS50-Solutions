# INPUT
def create_list_digits(credit_card: str) -> list:
    list_digits = []
    for i in range(len(credit_card)):
        list_digits.append(int(credit_card[i]))
    return list_digits

# CHECKSUM


def luhn_function(list_digits: list) -> bool:
    track = 0
    for i in range(len(list_digits) - 2, -1, -2):
        track += list_digits[i] * 2
        if (list_digits[i] * 2) > 9:
            track -= 9
    for i in range(len(list_digits) - 1, -1, -2):
        track += list_digits[i]
    if track % 10 == 0:
        return True
    else:
        return False


def check_validation_card(valid: bool, digits, list):
    # VALIDATION
    if valid == True:
        if digits == 15 and list[0] == 3 and (list[1] in {4, 7}):
            print("AMEX")
        elif digits in {13, 16} and list[0] == 4:
            print("VISA")
        elif digits == 16 and list[0] == 5 and (list[1] in {1, 2, 3, 4, 5}):
            print("MASTERCARD")
        else:
            print("CHECKSUM VALID")

    else:
        print("INVALID")


def main():
    # FUNCTION INPUT
    credit_card = input("Creditcard: ")
    list = create_list_digits(credit_card)
    # FUNCTION LUHN
    valid = luhn_function(list)
    # FUNCTION CHECK
    check_validation_card(valid, len(list), list)


if __name__ == "__main__":
    main()
