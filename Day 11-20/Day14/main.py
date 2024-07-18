from art import logo , vs
import random
from game_data import data


def choice():
    """a random element from data list"""
    return random.choice(data)


def compare(a,b):
    global option_b
    """compares followers and outputs the highest"""
    if a == b:
        option_b = choice()    
    return max(a['follower_count'], b['follower_count'])


def answer(a,b,c):
    """checks value from 'compare' to give a choice answer"""
    if a['follower_count'] == c:
        return 'a'
    elif b['follower_count'] == c:
        return 'b'


print(logo)


score_count = 0
end_game = False

option_a = choice()

while not end_game:
    
    option_b = choice()

    check = compare(option_a, option_b)
    ans = answer(option_a, option_b, check)

    print(f"Compare A: {option_a['name']} a {option_a['description']} from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']} a {option_b['description']} from {option_b['country']}")

    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    while player_choice not in ['a', 'b']:
        player_choice = input("Wrong input, please type 'A' or 'B': ").lower()

    if player_choice == ans:
        score_count += 1
        option_a = option_b
        print(f"That is correct, Total score: {score_count}\n\n")

    else:
        end_game = True
        print(f"That's wrong\nYour Total score: {score_count}")







