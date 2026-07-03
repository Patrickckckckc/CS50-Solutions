from cs50 import get_int

# ASKING FOR INPUT
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

# CREATE PYRAMIDS
for i in range(height):
    for a in range(height-1-i):
        print(" ", end="")
    for b in range(i + 1):
        print("#", end="")
    print("  ", end="")
    for c in range(i + 1):
        print("#", end="")
    print("")
