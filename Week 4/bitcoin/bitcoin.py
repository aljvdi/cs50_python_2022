import sys
from requests import get, RequestException

def get_request(amount):
    try:
        r = get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        rate = r['bpi']['USD']['rate_float']
        result = rate * amount
        print(f"${result:,.4f}")
    except RequestException:
        sys.exit("RequestException")

def main():
    try:
        n: float = float(sys.argv[1])
        get_request(n)
    except ValueError:
        sys.exit("argument is not a number")
    except IndexError:
        sys.exit("Missing argument")

if __name__ == "__main__":
    main()