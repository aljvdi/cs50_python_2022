def is_valid(s: str) -> bool:
    each: list = [*s]
    if len(each) >= 2 and len(each) <= 6:
        if s.isalnum():
            if each[0] != '0':
                if each[0].isalpha() and each[1].isalpha():
                    found: bool = False
                    for i in range(2, len(s)):
                        if each[i] == '0':
                            if i < (len(s) - 1):
                                found = True
                    return not found

    return False

def main():
    plate = input("Plate: ")
    if is_valid(plate.upper()):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()