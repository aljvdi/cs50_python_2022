
def getFileMimebasedOnExtension(inp: str) -> str:
    type = ""

    match inp.lower().strip().split(".")[-1]:
        case 'gif':
            type = 'image/gif'
        case 'jpg':
            type = 'image/jpeg'
        case 'jpeg':
            type = 'image/jpeg'
        case 'png':
            type = 'image/png'
        case 'txt':
            type = 'text/plain'
        case 'pdf':
            type = 'application/pdf'
        case 'zip':
            type = 'application/zip'
        case _:
            type = 'application/octet-stream'
    return type


def main():
    inp = input("Enter your file name -> ")
    if len(inp) > 0:
        print(getFileMimebasedOnExtension(inp))
    else:
        print("Empty input")


if __name__ == "__main__":
    main()