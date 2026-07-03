def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(text):
    vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
    shortened_word = ""
    for c in text:
        if c not in vowels:
            shortened_word = shortened_word + c
    return shortened_word

if __name__ == "__main__":
    main()
