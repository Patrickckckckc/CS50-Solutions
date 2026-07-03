def count_letters(text: str) -> int:
    total = 0
    for char in text:
        if char.isalpha():
            total += 1
    return total


def count_words(text: str) -> int:
    total = 1
    for char in text:
        if char == " ":
            total += 1
    return total


def count_sentences(text: str) -> int:
    total = 0
    for char in text:
        if char in (".", "?", "!"):
            total += 1
    return total


def coleman_index(letters, words, sentences: int) -> int:
    L = (letters / words) * 100
    S = (sentences / words) * 100
    coleman_index = int(round(0.0588 * L - 0.296 * S - 15.8))
    return coleman_index


def print_grade_level(result: int):
    if result < 1:
        print("Before Grade 1")
        return
    elif result >= 16:
        print("Grade 16+")
        return
    else:
        print(f"Grade {result}")


def main():
    # ASK FOR INPUT
    text = input("Give me a text: ")

    # TAKE Letters, Words, Sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Coleman Index
    result = coleman_index(letters, words, sentences)

    # Print Grade
    print_grade_level(result)


if __name__ == "__main__":
    main()
