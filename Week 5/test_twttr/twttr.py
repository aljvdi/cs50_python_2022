THE_VOWELS: list = ['a','e','i','o','u','A','E','I','O','U']

def shorten(word: str) -> str:
    return ''.join([l if l not in THE_VOWELS else '' for l in [*word]])

def main() -> str:
    inp = input('-> ')
    if len(inp) > 0:
        print(shorten(inp))

if __name__ == "__main__":
    main()