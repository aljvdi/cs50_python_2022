# level (n) == (1,2,3)
# random math n > -1
# 4 + 1 = n if n true then 4+1 = 5 else three times EEE after that show correct answer
from random import randint

USER_META = {
    'requested_level': 0,
    'current_score': 0
}


def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid level. Please select 1, 2, or 3.")

def generate_questions(level: get_level, count: int = 10) -> list:
    res: list = []
    level_ranges: dict = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    for _ in range(count):
        selected_level: tuple = level_ranges[level]
        get_question: list = [randint(selected_level[0],selected_level[1]) for _ in range(2)]
        answer : int  = get_question[0] + get_question[1]
        res.append({
            'question': f'{get_question[0]} + {get_question[1]} = ',
            'answer': {
                'numeric': answer,
                'string': f'{get_question[0]} + {get_question[1]} = {answer}'
            }
        })

    return res

def generate_integer(level):
    for q in generate_questions(level):
        GUESSES: int = 0
        while GUESSES < 3:
            user_res = input(q['question'])
            if user_res.isnumeric():
                user_res: int = int(user_res)
                if user_res == q['answer']['numeric']:
                    USER_META['current_score'] += 1
                    break
                elif user_res != q['answer']['numeric']:
                    GUESSES += 1
                    print("EEE")
            else:
                GUESSES += 1
                print("EEE")

            if GUESSES == 3:
                print(q['answer']['string'])

    print(f"Score: {USER_META['current_score']}")

def main():
    level: int = get_level()
    generate_integer(level)

if __name__ == "__main__":
    main()
