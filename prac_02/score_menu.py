"""
function get_valid_score
    score = None
    while score is None:
        try:
            get score
            if score < 0 or score > 100
                display "Invalid input. Score must be between 0 and 100."
                score = None
        except ValueError:
            display "Invalid score. Please enter a score between 0 and 100."
    return score

function main
    score = get_valid_score()
    choice = ""

    while choice != 'q':
        display "(G)et score  (P)rint result  (S)how stars  (Q)uit"
        get choice

        if choice == 'g':
            score = get_valid_score()
        else if choice == 'p':
            display "Result: {determine_result(score)}"
        else if choice == 's':
            display "*" * score
        else if choice == 'q':
            display "See you again!"
        else:
            display "Invalid choice, try again."


function determine_result(score)
    if score >= 90:
        return "Excellent"
    else if score >= 50:
        return "Passable"
    else:
        return "bad"
"""

MIN_SCORE = 0
MAX_SCORE = 100
E_SCORE = 90
P_SCORE = 50

def get_valid_score():
    score = None
    while score is None:
        try:
            score = int(input("Enter a valid score: "))
            if score < MIN_SCORE or score > MAX_SCORE:
                print("Invalid input. Score must be between 0 and 100.")
                score = None
        except ValueError:
            print("Invalid score. Please enter a score between 0 and 100.")
    return score

def main():
    score = get_valid_score()
    choice = ""

    while choice != 'q':
        print("(G)et score  (P)rint result  (S)how stars  (Q)uit")
        choice = input("Enter your choice: ").lower()

        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            print(f"Result: {determine_result(score)}")
        elif choice == 's':
            print("*" * score)
        elif choice == 'q':
            print("See you again!")
        else:
            print("Invalid choice, try again.")


def determine_result(score):
    if score >= E_SCORE:
        return "Excellent"
    elif score >= P_SCORE:
        return "Passable"
    else:
        return "bad"

main()