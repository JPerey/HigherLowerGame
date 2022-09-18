from textwrap import fill
import art
import game_data
import os
import random

# global variables (if any)
player_score = 0

# function definitions


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def higher_lower():
    # local variables inits (if any)
    player_score = 0
    player_choice_correct = False
    who_has_more = ""
    winning = True
    winning_ticker = 0
    previous_champ = {}

    while winning == True:
        print(art.logo)
        pvp_list = fill_pvp(winning_ticker, previous_champ)
        previous_champ = pvp_list[1]
        display(pvp_list, player_score)
        who_has_more = more_followers(pvp_list)
        player_choice_correct = False

        while player_choice_correct != True:
            player_AB_choice = input(
                "Who has more followers? A or B: ").upper()
            if player_AB_choice == "A" or player_AB_choice == "B":
                player_choice_correct = True
            else:
                print("Invalid input. 'A' or 'B' only. ")

        if who_has_more == "A" and player_AB_choice == "A":
            player_score += 1
            winning_ticker += 1
        elif who_has_more == "B" and player_AB_choice == "B":
            player_score += 1
            winning_ticker += 1
        elif who_has_more == "Tie":
            winning_ticker += 1
        else:
            winning = False
    start(player_score)


def fill_pvp(winning_ticker, previous_champ):
    filled_pvp = ["", ""]
    if winning_ticker == 0:
        for i in range(0, 2):
            random_choice = random.choice(range(0, len(game_data.data)))
            #print(f"ranbdom choice: {random_choice}")
            filled_pvp[i] = game_data.data[random_choice]
            #print(f"filled pvp: {filled_pvp}")
    else:
        filled_pvp[0] = previous_champ
        random_choice = random.choice(range(0, len(game_data.data)))
        filled_pvp[1] = game_data.data[random_choice]

    return filled_pvp


def display(pvp_list, player_score):
    clear()
    print(art.logo)
    print(f"player score: {player_score}")
    print(
        f"{pvp_list[0]['name']}, a {pvp_list[0]['description']}, from {pvp_list[0]['country']}")
    print(f"amount of followers: {pvp_list[0]['follower_count']}")
    print(art.vs)
    print(
        f"{pvp_list[1]['name']}, a {pvp_list[1]['description']}, from {pvp_list[1]['country']}")
    print(f"amount of followers: {pvp_list[1]['follower_count']}")


def more_followers(pvp_list):
    if pvp_list[0]['follower_count'] > pvp_list[1]['follower_count']:
        return "A"
    elif pvp_list[0]['follower_count'] == pvp_list[1]['follower_count']:
        return "Tie"
    else:
        return "B"


def start(player_score):
    # local variables inits (if any)
    player_start_correct = False

    print(art.logo)
    if player_score != 0:
        print(f"final score: {player_score}")
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

start(player_score)
