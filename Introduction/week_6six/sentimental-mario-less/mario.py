from cs50 import get_int

# Ask for INPUT
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
# Create the Piramds
for i in range(height):          #Rows
    for a in range(height-i-1):  #Spaces
        print(" ", end="")
    for b in range(i+1):         # Hashes
        print("#", end="")
    print("")
