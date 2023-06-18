from random import randint

USER_META = {
    'number_to_guess': 0,
    'guesses': 0
}


def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Invalid level. Please select more than 0")
        except ValueError:
            print("Invalid level. Please select more than 0")

def generate_number(level: get_level) -> int:
    return randint(1,level)

def main_game(level):
    USER_META["number_to_guess"] = generate_number(level)
    while True:
        try:
            user_guess = int(input('Guess: '))
            USER_META['guesses'] += 1
            if USER_META['number_to_guess'] < user_guess:
                print('Too large!')
            elif USER_META['number_to_guess'] > user_guess:
                print('Too small!')
            else:
                print('Just right!')
                break
        except ValueError:
            pass

def main():
    level: int = get_level()
    main_game(level)

if __name__ == "__main__":
    main()
