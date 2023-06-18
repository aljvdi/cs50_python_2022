MONTHS: list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def ChangeDateAndTimeToIso8601(DD: int, MM: int, YYYY:int) -> str:
    return f'{YYYY}-{MM:02}-{DD:02}'

def GetMonthBasedOnName(month_name: str) -> int:
    return MONTHS.index(month_name.title()) + 1

def main():
    try:
        inp = input('MM/DD/YYYY or MONTH DD, YYYY -> ')
        splited: list = []
        if len(inp) > 0:

            if ',' in inp:
                s = inp.split(',')
                splited = [int(x) if x.isdigit() else x for x in s[0].split(' ')] + [int(s[1].strip())]
            elif '/' in inp:
                splited = [int(x) for x in inp.split('/')]

            if isinstance(splited[0], str) and splited[0].title() in MONTHS:
                splited[0] = int(GetMonthBasedOnName(splited[0]))

            if splited[1] <= 31 and splited[0] <= 12:
                print(ChangeDateAndTimeToIso8601(DD=splited[1],MM=splited[0],YYYY=splited[2]))
                return True
    except (ValueError, IndexError, TypeError):
        pass



if __name__ == "__main__":
    while True:
        if main():
            break