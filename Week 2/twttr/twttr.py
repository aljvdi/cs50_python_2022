THE_VOWELS: list = ['a','e','i','o','u']

def remove_all_vowels(string: str) -> str:
    return ''.join([l if l.lower() not in THE_VOWELS else '' for l in [*string]])

def main():
    inp = input('-> ')
    if len(inp) > 0:
        print(remove_all_vowels(inp))

if __name__ == "__main__":
    main()