# mes, dia, año -> año, mes, día
def main():
    date = converter_iso8601()
    print(f"{date[0]}-{str(date[1]).zfill(2)}-{str(date[2]).zfill(2)}")


def converter_iso8601():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # Months = 12 MAX
    # Days = 31 MAX
    while True:
        date = input("Date: ")
        if "/" in date:  # Input in CASE 9/8/1636
            month, day, year = date.split("/")
            try:
                if int(month) > 12 or int(day) > 31:
                    continue
                year = int(year)
                return [year, month, day]
            except ValueError:
                pass
        else:              # Input in CASE September 8, 1636
            month, day, year = date.split()
            if month in months:
                try:
                    month = months.index(month) + 1
                    day = day.replace(',', '')
                    if int(month) > 12 or int(day) > 31:
                        continue
                    year = int(year)
                    return [year, month, day]
                except ValueError:
                    pass

main()
