"""Script to drill binary to decimal or decimal to binary conversion."""

import random
import pyinputplus as pyip


def generate_and_output_a_random_binary_number():
    random_decimal_number = random.randint(0, 256)
    binary = format(random_decimal_number, "08b")
    print(f"\nconvert {binary} to decimal")
    return binary


def test_user_answer(test_value):
    if user_answer == test_value:
        print("correct")
        correct_answers.append(user_answer)
    else:
        print("incorrect")
        incorrect_answers.append(user_answer)


def try_another():
    return pyip.inputYesNo("\nwould you like to try another (y or n)? ")


def generate_a_random_integer():
    number = random.randint(1, 256)
    print(f"\nconvert {number} to binary")

    return number


def calculate_percentage_correct():
    attempts = correct_answers + incorrect_answers
    corrects = len(correct_answers)
    total = len(attempts)
    percentage = \
    round(corrects / total * 100)

    return total, corrects, percentage


def output_summary():
    print("\nsummary")
    print(f"number of attempts: {number_of_attempts}")
    print(f"number correct: {number_of_correct_answers}")
    print(f"percentage correct: {percentage_correct}%\n")


binary_or_decimal_switcher = {
    1: "binary to decimal",
    2: "decimal to binary"
    }

print("\nwould you like to convert")
for number, direction in binary_or_decimal_switcher.items():
    print(f"{number}. {direction}")

while True:
    direction = int(input("> "))
    if direction not in list(binary_or_decimal_switcher.keys()):
        print("please select one of the options above")
    else:
        break

binary_or_decimal = binary_or_decimal_switcher[direction]
correct_answers = []
incorrect_answers = []
while True:
    if binary_or_decimal == "binary":
        binary_value = generate_and_output_a_random_binary_number()
        answer = int(binary_value, 2)
        user_answer = int(input("> "))
    else:
        decimal_value = generate_a_random_integer()
        answer = format(decimal_value, "08b")
        user_answer = input("> ")
    test_user_answer(answer)
    user_choice = try_another()
    if user_choice != "yes":
        number_of_attempts, number_of_correct_answers, \
        percentage_correct = calculate_percentage_correct()
        output_summary()
        break
