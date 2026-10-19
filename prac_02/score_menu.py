"""A simple menu function using the same process as score.py"""

MENU = """(G)et a valid score (from 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Score = {score}. Result is {result}")
        elif choice == "S":
            asterise(score)
            print()
        else:
            print("Invalid operation.")
        print(MENU)
        choice = input(">>>").upper()
    print("Exiting function. Farewell.")


def asterise(score: int):
    for i in range(1, score + 1, 1):
        print("*", end="")



def get_valid_score():
    score = int(input("Please enter a score between 0-100 inclusive: "))
    return score

def determine_result(score: int):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()