import Day07.ascii as ascii
import random
import time

random_no = random.randint(0, 2)
set = [ascii.rock, ascii.paper, ascii.scissors]

print("Lets play Rock, Paper, Scissors!!!")
user_choice = input("Choose").lower()

print(f"You picked {user_choice}:")

if user_choice == "rock":
    choice = 0
    print(set[0])
elif user_choice == "paper":
    choice = 1
    print(set[1])
elif user_choice == "scissors":
    choice = 2
    print(set[2])

time.sleep(3)

# cpu choice
if random_no == 0:
    r = "rock"
    cpu_choice = 0
    print(f"Your opponent picks {r}:")
    print(set[0])
elif random_no == 1:
    p = "paper"
    cpu_choice = 1
    print(f"Your opponent picks {p}:")
    print(set[1])
elif random_no == 2:
    cpu_choice = 2
    s = "scissors"
    print(f"Your opponent picks {s}:")
    print(set[2])

if choice == cpu_choice:
    print("It's a tie!\nPlay again")
elif choice == 0 and cpu_choice == 2:
    print("You won!!!\nPlay again")
elif choice == 1 and cpu_choice == 0:
    print("You won!!!\nPlay again")
elif choice == 2 and cpu_choice == 1:
    print("You won!!!\nPlay again")
else:
    print("You lost.\nTry again?")