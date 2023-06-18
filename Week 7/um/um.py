import re, sys

# Let we don't use regex, Shall we?
def count(string: str) -> int:
    acceptable_words: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for word in string.split():
        for l in word:
            if l not in acceptable_words:
                string = string.replace(l, ' ')
                break

    return string.lower().split().count('um')


def main():
    print(count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?'))

if __name__ == "__main__":
    main()