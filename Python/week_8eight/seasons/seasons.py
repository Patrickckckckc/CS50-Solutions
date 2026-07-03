from datetime import date
import inflect

def main():
    print(convert_minutes(input("Date of Birth: ")))

def convert_minutes(birth_date):
    # Parse birth date
    birth_date = valid(birth_date)
    current_date = date.today()
    # Calculate minutes lived
    time_delta = current_date - birth_date
    minutes = time_delta.days * 24 * 60
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"

def valid(d):
    try:
        return date.fromisoformat(d)
    except ValueError:
        raise ValueError("Invalid Date")

if __name__ == "__main__":
    main()
