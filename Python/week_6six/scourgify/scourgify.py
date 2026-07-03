import sys
import csv


def main():
    # CLA Requesistes:
    if len(sys.argv) != 3:
        sys.exit("Too few Command-Line Arguments")
    if not sys.argv[1].endswith("csv") or not sys.argv[2].endswith("csv"):
        sys.exit("The file(s) is not a csv FILE")
    # Read and Write a new FIlE
    with open(sys.argv[1], "r") as input:
        reader = csv.DictReader(input)
        headers = ["name", "last_name", "house"]
        with open(sys.argv[2], "w", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=headers)
            writer.writeheader()
            for row in reader:
                writer.writerow({
                    "name": row["name"].split(",")[0],
                    "last_name": row["name"].split(",")[1],
                    "house": row["house"]
                })

    # Print Out the RESULTS
    with open(sys.argv[2], "r") as output:
        reader = csv.DictReader(output)
        for row in reader:
            print(f"Dear {row['name']}{row['last_name']}")


if __name__ == "__main__":
    main()
