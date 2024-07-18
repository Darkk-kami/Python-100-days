import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print(nato_dict)


while True:
    user_input = input("What is your name?: ").upper()
    try:
        nato_code_name = [nato_dict[letter] for letter in user_input]
        break
    except KeyError:
        print('Only Alphabets are allowed here')

print(nato_code_name)


