import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?P<first_hour>\d{1,2}):?(?P<first_minutes>\d{2})? (?P<first_noon>AM|PM) to (?P<second_hour>\d{1,2}):?(?P<second_minutes>\d{2})? (?P<second_noon>AM|PM)$"
    match = re.search(pattern, s)

    if match:
        # Get Valid Hours
        hour = int(match.group("first_hour"))
        minute = int(match.group("first_minutes") or 0)
        second_hour = int(match.group("second_hour"))
        second_minute = int(match.group("second_minutes") or 0)
        if not (
            1 <= hour <= 12
            and 0 <= minute <= 59
            and 1 <= second_hour <= 12
            and 0 <= second_minute <= 59
        ):
            raise ValueError("Invalid Time")
        # Change Values
        first = to_24h(hour, minute, match.group("first_noon"))
        second = to_24h(second_hour, second_minute, match.group("second_noon"))
        return f"{first} to {second}"

    else:
        raise ValueError("Invalid input")

def to_24h(hour, minute, noon):
    hour = int(hour)
    minute = int(minute)
    if noon == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
