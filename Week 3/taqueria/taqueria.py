
menu: dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

TOTAL: float = 0

def main():
    while True:
        try:
            global TOTAL
            inp: str = input('Item: ')
            if len(inp) > 0:
                if inp.title() in menu:
                    TOTAL += menu[inp.title()]
                    print(f'Total: ${TOTAL:.2f}')
        except EOFError:
            print("")
            break


if __name__ == "__main__":
    main()