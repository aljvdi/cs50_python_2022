import sys
from os import path

def isFileAcceptable(file_name: str) -> tuple:
    # [is_python, is_exist]
    return (
        1 if file_name.endswith('.py') else 0,
        1 if path.exists(file_name) else 0
    )

def main(file_name: str) -> None:
    res_check: tuple = isFileAcceptable(file_name)
    if res_check[0]:
        try:
            with open(file_name, 'r') as f:
                lines = f.read().splitlines()
                c = len(lines)
                for line in lines:
                    for word in line.rstrip().strip().split('\n'):
                        if len(word) < 1:
                            c -= 1
                        elif len(word) > 0 and word.startswith("#"):
                            c -= 1
            print(c)
        except FileNotFoundError:
            sys.exit("File does not exist")

    else:
        sys.exit('Not a Python file')

if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        main(sys.argv[1])