import sys

count = 0
# CLA Requesistes:
if len(sys.argv) != 2:
    sys.exit("Too few Command-Line Arguments")
if not sys.argv[1].endswith("py"):
    sys.exit("No a python FILE")

# Function that returns number of lines
name_file = sys.argv[1]
try:
    with open(name_file, "r") as file:
        for line in file:
            if not line.strip().startswith("#") and line.split() != []:
                count += 1
except FileNotFoundError:
    sys.exit("File doesn´t exists")

print(count)

