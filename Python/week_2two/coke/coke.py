def main():
    due = 50
    coins_available = (5, 10, 25)
    while due > 0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert a Coin: "))
        if coin in coins_available:
            due = due - coin
    print(f"Changed Owed: {abs(due)}")

main()
