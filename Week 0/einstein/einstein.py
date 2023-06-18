# E = m (c ^ c)
# inp = 1 (Perhaps will be the M)
# out = 90000000000000000ً

def calc(m: int) -> int:
    # I got timeout error; therefore, I decide to calculate the C, then I can use it :)
    c = 90000000000000000 # 300000000 * 300000000 or c ^ c
    e = m * c
    return e

def main():
    inp = input()
    if len(inp) > 0:
        print(calc(int(inp)))
    else:
        print("No input given. please try again.")

if __name__ == "__main__":
    main()