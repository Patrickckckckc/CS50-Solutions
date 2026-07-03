def main():
    text = input("Write:").lower()
    forty_two(text)

def forty_two(text):
    if '42'in text or 'forty-two' in text or 'forty two' in text :
        print("Yes")

main()
