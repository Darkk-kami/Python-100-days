from art import logo
import random

print(logo)

def lives(choice):
    if choice == 'e':
        return 10
    elif choice == 'm':
        return 7
    else:
        return 5

def strike():
    """strikes a life"""
    global no_of_lives
    no_of_lives -= 1
    if no_of_lives > 1:
        print(f"You have {no_of_lives} lives left\n")
    else:
        print(f"You have {no_of_lives} life left\n")

print("Can you guess the number?\n")

print("""Difficulty level
-----------------
Easy: 10 lives
Medium: 7 lives
Hard: 5 lives\n
""")

difficulty = input("Pick 'E' for Easy, 'M' for Medium or 'H' Hard").lower()
while difficulty not in ['e', 'm' ,'h']:
    difficulty = input("invalid input, pick 'E', 'M' or 'H'")

ans = random.randint(1,100) # picks a random number
print(f"Pssst. It's a number between 1 and 100")


no_of_lives = lives(difficulty)


while no_of_lives > 0:
    number = input("Pick a number:")
    while not number.isdigit():
        number = input("That is not a number\nPick a number:")

    number = int(number)
         
    if number > ans:
        print(f"The answer is less than {number}")
        strike()
    elif number < ans:
        print(f"The answer is higher than {number}")
        strike()
    else:
        print(f"You have won!\nThe correct number was {ans}\nPlay Again?")
        break
    


if no_of_lives == 0:
    print(f"You have lost, the correct answer was\n{ans}\nTry again?")
