"""

Question:


"""

import argparse
import sys

import requests


def get_api_key():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", required=True, help="CoinCap API key")
    parser.add_argument("amount", type=float, help="Number of Bitcoins")
    args = parser.parse_args()

    return args.key, args.amount


def get_current_price(API_KEY):
    url = f"https://api.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises an error if status is not 200
        data = response.json()
        price = float(data["data"]["priceUsd"])
        return price
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        sys.exit(1)


def main():
    API_KEY, n = get_api_key()
    # print(API_KEY, n)
    price = n * get_current_price(API_KEY)

    print(f"${price:,.4f}")


main()
