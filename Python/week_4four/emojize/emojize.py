from emoji import emojize


def main():
    text = input("Input: ")
    print(f"Output: {emojize(text, language='alias')}")


if __name__ == "__main__":
    main()
