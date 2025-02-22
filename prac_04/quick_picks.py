"""
import random

function main

    get number_picks

    for i in range(num_picks):
        quick_pick = generate_quick_pick()
        display format_quick_pick


function generate_quick_pick()
    numbers = random.sample(range(1, 45 ), 6 )
    numbers.sort()
    return numbers

function format_quick_pick(pick)
    display " ".join(f"{num:2}" for num in pick)
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():

    number_picks = int(input("How many quick picks? "))

    for i in range(number_picks):
        quick_pick = generate_quick_pick()
        format_quick_pick(quick_pick)

def generate_quick_pick():
    numbers = random.sample(range(MIN_NUMBER, MAX_NUMBER), NUMBERS_PER_PICK)
    numbers.sort()
    return numbers

def format_quick_pick(pick):
    print(" ".join(f"{num:2}" for num in pick))

main()

