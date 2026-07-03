from validator_collection import validators, errors


def main():
    print(validate(input("What is your email adress?")))


def validate(s):
    try:
        validators.email(s)
    except errors.InvalidEmailError:
        return "Invalid"
    else:
        return "Valid"


if __name__ == "__main__":
    main()
