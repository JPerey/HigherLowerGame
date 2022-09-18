from textwrap import fill
import art
import game_data
import os
import random

# global variables (if any)


# function definitions

def higher_lower():
    # local variables inits (if any)
    player_score = 0
    player_choice_correct = False
    who_has_more = ""

    print(art.logo)
    pvp_list = fill_pvp()
    display(pvp_list, player_score)
    who_has_more = more_followers(pvp_list)

    while player_choice_correct != True:
        player_AB_choice = input("Who has more followers? A or B: ").upper()
        if player_AB_choice == "A" or player_AB_choice == "B":
            player_choice_correct = True
        else:
            print("Invalid input. 'A' or 'B' only. ")

    if who_has_more == "A" and player_AB_choice == "A":
        player_score += 1
        print(f"correct.")
    elif who_has_more == "B" and player_AB_choice == "B":
        player_score += 1
        print(f"correct.")
    else:
        print(f"incorrect. game over. final score: {player_score}")
    start()


def fill_pvp():
    filled_pvp = ["", ""]
    for i in range(0, 2):
        random_choice = random.choice(range(0, len(game_data.data)))
        #print(f"ranbdom choice: {random_choice}")
        filled_pvp[i] = game_data.data[random_choice]
        #print(f"filled pvp: {filled_pvp}")
    return filled_pvp


def display(pvp_list, player_score):
    print(f"player score: {player_score}")
    print(
        f"{pvp_list[0]['name']}, a {pvp_list[0]['description']}, from {pvp_list[0]['country']}")
    print(art.vs)
    print(
        f"{pvp_list[1]['name']}, a {pvp_list[1]['description']}, from {pvp_list[1]['country']}")


def more_followers(pvp_list):
    if pvp_list[0]['follower_count'] > pvp_list[1]['follower_count']:
        return "A"
    else:
        return "B"


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def start():
    # local variables inits (if any)
    player_start_correct = False

    print(art.logo)
    while player_start_correct != True:
        player_choice = input("Would you like to play? yes or no: ").lower()
        if player_choice == "yes" or player_choice == "no":
            player_start_correct = True
        else:
            print("invalid input. 'yes' or 'no' only.")
    if player_choice == "yes":
        clear()
        higher_lower()
    else:
        print("goodbye.")
        exit()


# timeline

start()
