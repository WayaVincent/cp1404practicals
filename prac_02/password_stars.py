"""Password program"""
# Constants
PASS_LENGTH_MIN = 8


def main():

    password = get_password()
    verify = input("Please re-enter your password: ")
    if password == verify:
        print("Success")
        asterise(password)
    else:
        print("Password does not match")


def asterise(password: str):
    for i in range(1, len(password) + 1, 1):
        print("*", end="")


def get_password() -> str:
    password = input("Please enter your password: ")
    while len(password) < PASS_LENGTH_MIN:
        print("Password needs to have minimum 8 characters")
        password = input("Please enter your password: ")
    return password


main()