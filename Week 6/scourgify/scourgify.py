from os import path
import csv, sys


def isFileAcceptable(file_name: str) -> tuple:
    # [is_csv, is_exist]
    return (
        1 if file_name.endswith('.csv') else 0,
        1 if path.exists(file_name) else 0
    )

def GetData(l: list) -> list:
    for d in l:
        name: tuple = d['name'].split(",")
        d['first'], d['last'] = name[1].strip(), name[0].strip()
        del d['name']
    return l

import csv

def GenerateNew(l: list, file_name: str) -> None:
    header = ['first', 'last', 'house']
    with open(file_name, 'w+', newline='') as new_file:
        w = csv.DictWriter(new_file, fieldnames=header)
        w.writeheader()
        w.writerows(l)



def main(file_name: str) -> None:
    res_check: tuple = isFileAcceptable(file_name)
    if res_check[0]:
        try:
            res_file: list = []
            with open(file_name, 'r') as f:
                res_file = [r for r in csv.DictReader(f)]
                GenerateNew(GetData(res_file), file_name=sys.argv[2])

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit('Not a CSV file')


if __name__ == "__main__":
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        main(sys.argv[1])