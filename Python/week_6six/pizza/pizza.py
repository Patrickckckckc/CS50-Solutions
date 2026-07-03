import sys
import csv
from tabulate import tabulate


def main():
    # CLA Requesistes:
    if len(sys.argv) != 2:
        sys.exit("Too few Command-Line Arguments")
    if not sys.argv[1].endswith("csv"):
        sys.exit("This file is not a csv FILE")

    # Try to open the file:
    try:
        with open(sys.argv[1], "r") as file:
            menu_table(file)
    except FileNotFoundError:
        sys.exit("This file doesn´t exist")


def menu_table(file):
    reader = csv.DictReader(file)
    print(tabulate(reader, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
