from validators import email

def validate(e: str) -> True:
    return email(e)

def main():
    if validate(input("What's your email address? ")):
        print('Valid')
    else:
        print('Invalid')


if __name__ == "__main__":
    main()