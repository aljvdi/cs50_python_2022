# Fuel Gauge
# Input -> x/y (each of them should be integer)
# x/y <= 1% -> E
# x/y >= 99% -> F
# x/y != integer || x > y || y == 0 -> request for re-enter the x/y

def GetFuelStatus(x: int, y:int) -> int:
    try:
        return (x / y) * 100
    except (ZeroDivisionError, ValueError):
        return -1


def main():
    a = input('x/y -> ')
    if len(a) >= 3:
        a = a.split('/')
        if a[0].isdigit() and a[1].isdigit():
            if int(a[0]) <= int(a[1]):
                res: int = GetFuelStatus(int(a[0]),int(a[1]))
                r: str = ""
                if res <= 1:
                    r = "E"
                elif res >= 99:
                    r = "F"
                else:
                    r = f'{round(res)}%'
                print(r)
                return True


if __name__ == "__main__":
    while True:
        try:
            if main():
                break
        except (ValueError, ZeroDivisionError):
            print('value must be an integer')