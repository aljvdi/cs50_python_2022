import inflect

e = inflect.engine()

def main():
    names: list = []
    while True:
        try:
            n: str = input("Name: ")
            if len(n) > 0:
                n = n.title()
                names.append(n)
            else:
                exit(0)
        except EOFError:
            print(f"\nAdieu, adieu, to {e.join(names)}")
            break
        else:
            continue

if __name__ == "__main__":
    main()