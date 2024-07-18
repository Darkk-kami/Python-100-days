import time
pause = time.sleep(3)

print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Do you have what it takes to find the treasure?.")
ans = input("A dark path lies ahead of you. Enter? Y or N:")

while ans != "y":
    print("You have entered the kingdom of myr, peril awaits!!!")
    pause
    print("You look around and you see are trapped in a maze!\nThere are only two paths!!")
    pause
    ans = input("Go left or right?")
    if ans == "left":
        input ("hmmm.... you are met with two more paths, left or right?")
    else:
        print("You see a dragon and it burns you alive! oof!")
        pause
        print("Try again!!!")

else:
    print(f"You are a failure....")
    pause
    print("Come back when you grow some balls")
