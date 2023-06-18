def convert(f) -> None:
    try:
        values = f.split('/')
        x = int(values[0])
        y = int(values[1])
        frac = (x / y) * 100
        return int(frac)
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError

def gauge(percentage):
    if percentage == 75:
        return "75%"
    elif percentage >= 50 and percentage < 75:
        return "50%"
    elif percentage >= 25 and percentage < 50:
        return "25%"
    elif percentage >= 76 and percentage <= 100:
        return "F"
    elif percentage >= 0 and percentage < 25:
        return "E"

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    fuel = gauge(percentage)
    print(fuel)

if __name__ == "__main__":
    main()