import sys
import requests
import requests


# Get Actual Bitcoin Price
def main():
    if len(sys.argv) == 2:
        try:
            value = float(sys.argv[1])
        except:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=67600da6f1f8dc7fa49d3e03d2af28b3936a3fab26e83d349aba3cf2e61964d4")
        r.raise_for_status()
        data = r.json()
        bitcoin_price = float(data["data"]["priceUsd"])
        total_amount = bitcoin_price * value
        print(f"${total_amount:,.4f}")
    except requests.RequestException:
        print("Website Not Responding. Please Try Later")


if __name__ == "__main__":
    main()
