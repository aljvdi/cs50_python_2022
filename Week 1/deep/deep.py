
def isInputEqualToFortyTwo(inp: str) -> bool:
    inp = inp.lower().strip(" ")
    return True if inp == "42" or inp == "forty-two" or inp == "forty two" else False


def main():
    inp = input("Prompt Me -> ")
    if len(inp) > 0:
        print("Yes" if isInputEqualToFortyTwo(inp) else "No")
    else:
        print("Empty input")


if __name__ == "__main__":
    main()