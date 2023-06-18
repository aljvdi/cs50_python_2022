
Grocery_Shopping_List: dict = {}
Grocery_Draft: list = []

# Yk, first, I want that user put it's grocery into the draft one, then I will transfer everything from draft
# to grocery shopping dict and show that to user

def DraftToList() -> None:
    for grocery in Grocery_Draft:
        if grocery not in Grocery_Shopping_List:
            Grocery_Shopping_List[grocery] = 1
        else:
            Grocery_Shopping_List[grocery] += 1

def SortGrocery() -> None:
    global Grocery_Shopping_List
    Grocery_Shopping_List = dict(sorted(Grocery_Shopping_List.items()))

def main():
    while True:
        try:
            inp: str = input('')
            if len(inp) > 0:
                Grocery_Draft.append(inp.upper())
        except EOFError:
            DraftToList()
            SortGrocery()
            for grocery in Grocery_Shopping_List:
                print(Grocery_Shopping_List[grocery], grocery)
            break


if __name__ == "__main__":
    main()