def main():
    text = input("Input: ")
    text_no_vowels = eliminate_vowels(text)
    print("Output: " + text_no_vowels)


def eliminate_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return ''.join(["" if c.lower() in vowels else c for c in text])


main()
