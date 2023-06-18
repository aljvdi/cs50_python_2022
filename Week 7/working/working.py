# input: 3 PM
# output: 15:00
import re, sys

# The first solution: using re
# NOTE: NGL, I used Chat GPT for finding the right Regex ;)
import re

def convert(time: str) -> str:
    rgx = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", time)
    if rgx:
        sp: tuple = rgx.groups()

        # I don't have any idea to fix 12 AM to 12 PM, 12:00 AM to 12:00 PM :/
        if sp[0] in ['12', '12:00'] and sp[4] in ['12', '12:00']:
            return f'00:00 to 12:00'

        hours: list = [1 if int(x) < 12 else 0 for x in [sp[5], sp[1]]]
        if 0 not in hours:
            return f'{time_convert(int(sp[1]), sp[2], sp[3].upper())} to {time_convert(int(sp[5]), sp[6], sp[7].upper())}'

    raise ValueError

def time_convert(h: int, mi: int, me: str) -> str:
    return f"{(0 if (me == 'AM' and h == 12) else (12 if (me != 'AM' and h == 12) else (h if me == 'AM' else h + 12))):02}:{'00' if mi is None else mi}"


def main():
    print(convert(input('-> ')))

if __name__ == "__main__":
    main()