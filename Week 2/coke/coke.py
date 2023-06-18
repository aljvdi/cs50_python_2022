

inserted_amount : int = 0
EACH_COKE_PRICE : int = 50
ACCEPTED_COINS : list = [5,10,25]

def main():
    global inserted_amount
    inp = input('Insert Coin: ')
    if inp.isdigit():
        inp = int(inp)
        if inp in ACCEPTED_COINS:
            inserted_amount += inp

    if inserted_amount >= EACH_COKE_PRICE:
        print(f'Change Owed: {inserted_amount - EACH_COKE_PRICE}')
        exit(1)
    else:
        print(f'Amount Due: {EACH_COKE_PRICE - inserted_amount}')

if __name__ == "__main__":
    while True:
        main()