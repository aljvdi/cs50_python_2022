# https://en.wikipedia.org/wiki/List_of_emoticons
# inp: hello :)
# out: Hello 🙂

def convert(str: str) -> str:
    t1 = str.replace(':(','🙁') if ':(' in str else str
    return t1.replace(':)', '🙂') if ':)' in t1 else t1

def main():
    inp = input()
    if len(inp) > 0:
        print(convert(inp))
    else:
        print("No input given. please try again.")

if __name__ == "__main__":
    main()