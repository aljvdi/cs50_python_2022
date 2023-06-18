def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    d_without_sign : str = d.strip('$') if '$' in d else d
    return float(d_without_sign)


def percent_to_float(p: str) -> float:
    p_without_sign : str = p.strip('%') if '%' in p else p
    return float(p_without_sign)  / 100

if __name__ == "__main__":
    main()