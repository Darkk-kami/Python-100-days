import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


letter_pool = []
nr_letters_count = 0
while nr_letters_count < nr_letters:
    nr_letters_count += 1
    x = random.randint(0, len(letters)-1)
    letter_pool.append(letters[x])

symbol_pool = []
nr_symbols_count = 0
while nr_symbols_count < nr_symbols:
    nr_symbols_count += 1
    y = random.randint(0, len(symbols)-1)
    symbol_pool.append(symbols[y])

number_pool = []
nr_numbers_count = 0
while nr_numbers_count < nr_numbers:
    nr_numbers_count += 1
    z = random.randint(0, len(numbers)-1)
    number_pool.append(numbers[z])

password = letter_pool + symbol_pool + number_pool
# randomizer
random.shuffle(password)

random_password = ""
for n in password:
    random_password += n

print(f"Your password is: {random_password}")
