def main():
    text = input("Text: ")
    print(convert(text))

def convert(text):
    text = text.replace(':)', '🙂').replace (':(', '🙁')
    return text

if __name__ == "__main__":
    main()

