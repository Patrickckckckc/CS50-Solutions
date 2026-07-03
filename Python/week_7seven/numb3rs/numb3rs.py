import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if match:
        # Just values between 0-256 and not "001"
        for i in match.groups():
            if not (0 <= int(i) <= 255):
                return False
            elif len(i) > 1 and i[0] == '0':
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
