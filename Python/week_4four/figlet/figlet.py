import sys
from pyfiglet import Figlet
import random

# Function transform normaltext -> figlettext
def main():
    # Create Figlet
    figlet = Figlet()
    font_list = figlet.getFonts()

    # Check correct Arguments
    # For 1 Argument
    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=random.choice(font_list))
        print(figlet.renderText(text))

    # For 3 Arguments
    elif len(sys.argv) == 3 and sys.argv[1] in ('-f', '--font') and sys.argv[2] in font_list:
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))

    else:
        print("Invalid usage")
        sys.exit(1)


if __name__ == "__main__":
    main()
