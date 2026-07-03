def main():
    text = input("Write: ")
    file(text)

def file(text):
    if text.endswith(".gif"):
        print("image/gif")
    elif text.endswith(".jpg") or text.endswith(".jpeg"):
        print("image/jpeg")
    elif text.endswith(".png"):
        print("image/png")
    elif text.endswith(".pdf"):
        print("application/pdf")
    elif text.endswith(".txt"):
        print("text/plain")
    elif text.endswith(".zip"):
        print("application/zip")
    else:
        print("unknown")

main()

