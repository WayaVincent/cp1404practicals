"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    print(f"User score = {score}. Result is {determine_result(score)}")
    if determine_result(score) == "Excellent":
        print("You get a prize!")
    rand_score = randint(0,100)
    print(f"Random score = {rand_score}. Result is {determine_result(rand_score)}")




def determine_result(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()