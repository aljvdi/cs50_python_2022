# TODO: We will get a camelCase type input, and we'll show output with the sanke_case

def ConvertCameltoSnakeCase(string: str) -> str:
    letter_list : list = [*string]
    serialise: list = [f'_{l.lower()}' if l.isupper() and letter_list.index(l) > 0 else l for l in letter_list]
    return ''.join(serialise)

def main():
    inp = input('-> ')
    if len(inp) > 0:
        print(ConvertCameltoSnakeCase(inp))
    else:
        print("No input given. please try again.")

if __name__ == "__main__":
    main()