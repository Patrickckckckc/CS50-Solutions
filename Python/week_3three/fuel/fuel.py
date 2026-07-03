def main():
    percentage = get_percentage_fuel()
    print(percentage)


def get_percentage_fuel():
    # Convert STR into a Fraction
    while True:
        fuel = input("Fraction: ")

        try:
            X,Y = fuel.split("/")
            X = int(X)
            Y = int(Y)
            if X < 0 or Y < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            # X cannot be greater than Y and divided by zero Errors
            if X <= Y:
                try:
                    result = X/Y
                    result = round(result * 100)
                except ZeroDivisionError:
                    pass
                else:
                    if result <= 1:
                        return "E"
                    elif result >= 99:
                        return "F"
                    else:
                        return f"{result}%"
if __name__ == "__main__":
    main()
