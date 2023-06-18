
def SolveMathproblem(x: int, y: str, z: int) -> float:
    res = 0
    match y:
        case '+':
            res = x + z
        case '-':
            res = x - z
        case '*':
            res = x * z
        case '/':
            res = x / z
        case _:
            res = 0

    return float(res)

def main():
    inp = input("Math problem (e.g, 2 + 2) -> ")
    if len(inp) > 0:
        x, y, z = inp.split(" ")
        print(SolveMathproblem(int(x),y,int(z)))
    else:
        print("Empty input")


if __name__ == "__main__":
    main()