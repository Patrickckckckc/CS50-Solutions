import re


def main():
    print(count(input("Text: ")))


def count(s):
    total = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(total)


if __name__ == "__main__":
    main()
