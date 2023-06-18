import csv, sys
from os import path
from tabulate import tabulate

def isFileAcceptable(file_name: str) -> tuple:
    # [is_csv, is_exist]
    return (
        1 if file_name.endswith('.csv') else 0,
        1 if path.exists(file_name) else 0
    )

def main(file_name: str) -> None:
    res_check: tuple = isFileAcceptable(file_name)
    if res_check[0]:
        try:
            res_file: list = []
            with open(file_name, 'r') as f:
                res_file = [r for r in csv.DictReader(f)]

            print(tabulate(res_file, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit('Not a CSV file')

if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        main(sys.argv[1])