
def getRewardForNotSayingHello(inp: str) -> str:
    reward = "$0"
    inp = inp.lower().strip()

    if inp.startswith('h'):
        if not inp.startswith('hello'):
            reward = "$20"
    else:
        reward = "$100"

    return reward


def main():
    inp = input("-> ")
    if len(inp) > 0:
        print(getRewardForNotSayingHello(inp))
    else:
        print("Empty input")


if __name__ == "__main__":
    main()