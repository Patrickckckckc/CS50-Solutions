import random

# Guessing Random Number
def main():
    # Ask indefine for a number
    while True:
        try:
            number = int(input("Level: "))
            if number > 0:
                break
        except ValueError:
            pass
        
    # Generate a Random Number
    random_number = random.randint(1, number)

    # Guess the Number
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
           pass

        if guess == random_number:
            print("Just Right!")
            return
        elif guess < random_number:
            print("Too Small!")
        else:
            print("Too Large!")



if __name__ == "__main__":
    main()
