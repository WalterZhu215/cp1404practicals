"""
import random

function main
    score = get_score()
    result = determine_result(score)
    display "Result: {result}"

    random_score = random.randint(0, 100)

    random_result = determine_result(random_score)
    display "Random score ({random_score}): {random_result}"

function determine_result(score)
    if 90 <= score <= 100:
        return "Excellent"
    else if 50 < score < 90:
        return "Passable"
    else if 0 <= score <= 50:
        return "Bad"
    else:
        return "Invalid score"

function get_score()
    while True:
        get score_input
        if score_input.replace('.', '', 1).isdigit() and score_input.count('.') < 2:
            return float(score_input)
        else:
            display "Invalid input. Please enter a numeric value."

"""
MIN_SCORE = 0
MAX_SCORE = 100
E_SCORE = 90
P_SCORE = 50

import random

def main():
    score = get_score()
    result = determine_result(score)
    print(f"Result: {result}")

    random_score = random.randint(0, 100)

    random_result = determine_result(random_score)
    print(f"Random score ({random_score}): {random_result}")

def determine_result(score):
    if E_SCORE <= score <= MAX_SCORE:
        return "Excellent"
    elif P_SCORE < score < E_SCORE:
        return "Passable"
    elif MIN_SCORE <= score <= P_SCORE:
        return "Bad"
    else:
        return "Invalid score"

def get_score():
    while True:
        score_input = input("Enter score: ")
        if score_input.replace('.', '', 1).isdigit() and score_input.count('.') < 2:
            return float(score_input)
        else:
            print("Invalid input. Please enter a numeric value.")

main()