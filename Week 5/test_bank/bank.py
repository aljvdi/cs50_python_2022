def value(greeting: str) -> int:
    greeting = greeting.lower()
    r: int = -1
    if greeting.startswith('hello'):
        r = 0
    elif greeting.startswith('h'):
        r = 20
    else:
        r = 100
    return r
