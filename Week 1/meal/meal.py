# Challenge, accept time in 12-hour format

def convert(time: str) -> float:
    time = time.lower()

    if 'a.m.' in time or 'p.m.' in time:
        # remove p.m. or a.m.
        hours, minutes = map(int, time[:-5].split(':'))

        if 'p.m.' in time and hours != 12:
            hours += 12
    else:
        hours, minutes = map(int, time.split(":"))

    return hours + (minutes / 60)


def getCurrentMeal(time: str) -> str:
    time = convert(time)
    current_meal = ""

    if time >= 7.0 and time <= 8.0:
        current_meal = "breakfast time"

    elif time >= 12.0 and time <= 13.0:
        current_meal = "lunch time"

    elif time >= 18.0 and time <= 19.0:
        current_meal = "dinner time"

    return current_meal


def main():
    inp = input("What time is it? -> ")

    if len(inp) > 0:
        print(getCurrentMeal(inp))
    else:
        print("Empty input")



if __name__ == "__main__":
    main()