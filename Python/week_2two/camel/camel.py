def main():
    text = input("camelCase: ")
    new_text = snake_converter(text)
    print(new_text)


def snake_converter(text):
    return ''.join(["_" + c.lower() if c.isupper() else c for c in text])


main()
