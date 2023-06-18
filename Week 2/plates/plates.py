def main():
    plate = input("Plate: ")
    if is_valid(plate.upper()):
        print("Valid")
    else:
        print("Invalid")

"""
[X] Each plate should be start with at least 2 chars
[X] Each plate should have maximum of 6 chars
[-] Numbers can't be in the middle of the plate, just at the end
[X] The first char can't be a zero (0)
[X] No space, dot or non alpha numeric
"""

def isChar(s: str) -> bool:
    return s.isalpha()


def is_valid(s: str) -> bool:
    each: list = [*s]
    if len(each) >= 2 and len(each) <= 6:
        if s.isalnum():
            if each[0] != '0':
                if isChar(each[0]) and isChar(each[1]):
                    found: bool = False
                    for i in range(2, len(s)):
                        if each[i] == '0':
                            if i < (len(s) - 1):
                                found = True
                    return not found

    return False





if __name__ == "__main__":
    main()