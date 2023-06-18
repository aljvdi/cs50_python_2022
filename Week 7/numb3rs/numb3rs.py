import re, sys

def validate(ip: str) -> bool:
    return True if re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip) else False


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()