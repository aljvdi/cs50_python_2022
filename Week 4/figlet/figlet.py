import sys
from pyfiglet import Figlet
from random import randint


fig = Figlet()

def isAnyArgExist() -> bool:
    return True if (len(sys.argv) - 1 ) > 0 else False

def getRequestedFont() -> tuple:
    if sys.argv[1] in ['-f', '--font']:
        if sys.argv[2] in fig.getFonts():
            return (True, sys.argv[2].strip())

    return (False, '')


def main():
    if isAnyArgExist():
         if (len(sys.argv) - 1 ) == 2:
            font = getRequestedFont()
            if not font[0]:
                sys.exit('Invalid usage')
            else:
                fig.setFont(font=font[1])
         else:
             sys.exit('Invalid usage')
    else:
        r: int = randint(0, len(fig.getFonts()))
        fig.setFont(font=fig.getFonts()[r])

    inp = input('Input: ')
    if len(inp) > 0:
        print(fig.renderText(inp))


if __name__ == "__main__":
    main()
