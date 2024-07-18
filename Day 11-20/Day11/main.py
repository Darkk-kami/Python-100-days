from art import logo
from func import ace_check, deal, black_jack, calc

print(logo)
user_name = input("What is your name?").title()
print("Game Start!")
# {} []
user = []
cpu = []

end_game = False

user.extend([deal(), deal()])
cpu.extend([deal(), deal()])


while not end_game:
    print(f"{user_name}:{user}\tcpu:{cpu}")

    user_total = calc(user)
    cpu_total = calc(cpu)

    if black_jack(user_total, user) == 0 and black_jack(cpu_total, cpu) == 0:
        print("Blackjack Draw!")
        end_game = True
        break
    elif black_jack(user_total, user) == 0:
        print(f"{user_name} has BlackjacK!\nYou win")
        end_game = True
        break
    elif black_jack(cpu_total, cpu) == 0:
        print(f"Computer has Blackjack!\n{user_name} Loses")
        end_game = True
        break

    ace_check(user)
    ace_check(cpu)

    if user_total > 21:
        end_game = True

    elif cpu_total > 21:
        end_game = True

    elif user_total < 21:
        choice = input("Do you want to pick another card?\nreply 'y' or 'n':").lower()

        while choice not in ['y', 'n']:
            choice = input("Invalid input. Please reply 'y' or 'n': ").lower()

        if choice == "y":
            user.append(deal())

        else:
            while cpu_total < 17:
                cpu.append(deal())
                cpu_total = calc(cpu)
                if cpu_total > 21:
                    ace_check(cpu)
            print(f"CPU: {cpu}")    
            end_game = True

if user_total > 21:
    print("CPU wins")
elif cpu_total > 21:
    print(f"{user_name} wins")

else:
    if user_total > cpu_total:
        print(f"{user_name} wins")
    elif user_total == cpu_total:
        print("Draw")
    else:
        print("CPU wins")

print(f"{user_name}:{user_total}\tCPU:{cpu_total}")

