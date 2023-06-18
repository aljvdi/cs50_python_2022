from emoji import emojize

def getEmoji(data: str) -> str:
    return emojize(data)

if __name__ == "__main__":
    print(getEmoji(input("-> ").strip().lower()))