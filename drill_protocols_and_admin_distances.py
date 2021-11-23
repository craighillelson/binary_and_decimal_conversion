"""
Script to drill protocols and their associated administrative distances in
preparation for the CCNA 200-301 exam
"""

import random
import pyinputplus as pyip


def build_menu():
    dct = {}
    options = [
        'protocols',
        'administrative distances'
    ]
    for number, option in enumerate(options, 1):
        dct[number] = option

    return dct


def present_menu():
    for number, category in menu.items():
        print(f"{number}. {category}")


def prompt_user():
    while True:
        print("\nselect one of the following")
        present_menu()
        user_choice = pyip.inputInt("> ", blank=False)
        if user_choice not in menu.keys():
            print("not in the list")
        else:
            break

    return menu[user_choice]


def populate_list():
    lst = [
        ("Connected", 0),
        ("Static", 1),
        ("eBGP", 20),
        ("EIGRP", 90),
        ("OSPF", 110),
        ("IS-IS", 115),
        ("RIP", 120),
        ("External EIGRP", 170),
        ("iBGP", 200)
    ]

    return lst


def determine_number_of_items(lst):
    return len(lst)


def create_list_of_random_numbers():
    return random.sample(range(NUMBER_OF_ITEMS_TO_QUIZ),
                         NUMBER_OF_ITEMS_TO_QUIZ)


def quiz_user(prompt):
    print(f"\n{prompt}")
    return pyip.inputStr("> ", blank=False)


def track_answers(answer, prompt):
    if USER_ANSWER == answer:
        print("correct")
        correct_answers.append(prompt)
    else:
        print("incorrect")
        print(f"the correct answer is {answer}")
        incorrect_answers.append(prompt)

    return correct_answers, incorrect_answers


def output_results(results, headline):
    if results:
        print(headline)
        print(*results, sep=", ")
    else:
        pass


def count_answers(answers):
    return len(answers)


def summary():
    print("\nsummary")
    number_of_correct_answers = count_answers(correct_answers)
    number_of_incorrect_answers = count_answers(incorrect_answers)
    print(f"number correct: {number_of_correct_answers}")
    print(f"number incorrect: {number_of_incorrect_answers}")
    output_results(correct_answers, "\nyou answered the following correctly")
    output_results(incorrect_answers, "\nyou should work on the following")


menu = build_menu()
protocols_or_administrative_distances = prompt_user()
print(f"you selected {protocols_or_administrative_distances}")
protocols_and_administrative_distances = populate_list()
NUMBER_OF_ITEMS_TO_QUIZ = \
determine_number_of_items(protocols_and_administrative_distances)
list_of_random_numbers = create_list_of_random_numbers()

correct_answers = []
incorrect_answers = []

for i in list_of_random_numbers:
    PROTOCOL = protocols_and_administrative_distances[int(i)][0]
    ADMINISTRATIVE_DISTANCE = protocols_and_administrative_distances[int(i)][1]
    if protocols_or_administrative_distances == "protocols":
        response = quiz_user(PROTOCOL)
        USER_ANSWER = int(response)
        track_answers(ADMINISTRATIVE_DISTANCE, PROTOCOL)
    else:
        USER_ANSWER = quiz_user(ADMINISTRATIVE_DISTANCE)
        track_answers(PROTOCOL, ADMINISTRATIVE_DISTANCE)

summary()
