import lists as lists
import random
import ascii as ascii

print(ascii.logo)
print("let's play hangman")

chosen_word = random.choice(lists.word_list)
display = []
lives = 6


for l in chosen_word:
    display.append("_")

while "_" in display and lives != 0:
    print(ascii.stages[lives])
    print(f"{' '.join(display)}")
    guess = input("\nGuess a letter:").lower()

    if guess in display:
        print(f"you have already picked: {guess}")

    if guess not in chosen_word:
        lives -= 1
        if lives > 1:
            print(f"\n{guess} is not in word\nYou have {lives} lives left")
        elif lives == 1:
            print(f"{guess} is not in word\nYou have {lives} life left!!")

    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess

if lives == 0:
    print(ascii.stages[0])
    print('you have lost')
else:
    print(ascii.stages[lives])
    print(f"{' '.join(display)}")
    print("you have won")


            