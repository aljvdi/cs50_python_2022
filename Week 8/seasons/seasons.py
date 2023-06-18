import sys
from datetime import date
from inflect import engine

def ConvertToDate(DoB: str) -> str:
    try:
        date_diff = date.today() - date.fromisoformat(DoB)
        return f'{engine().number_to_words(date_diff.days * 24 * 60, andword="").capitalize()} minutes' if date_diff.days > 0 else ''
    except ValueError:
        sys.exit("Invalid date")

def main() -> None:
    print(ConvertToDate(input("DoB -> ")))

if __name__ == "__main__":
    main()