
def main():
    inp = input("Enter your text: ")
    if len(inp) > 0:
        print(inp.replace(' ', '...'))
    else:
        print("No input given. please try again.")

if __name__ == "__main__":
    main()