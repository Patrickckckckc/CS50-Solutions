def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO $50.00
    return float(d.replace('$', ''))


def percent_to_float(p):
    # TODO 15%
    return (float(p.replace('%', ''))/ 100.0)

main()
