from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)
yes = True


def ceaser(direction, text, shift):
    shift = shift % 26
    code = ''
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter) + shift
            if position >= 26:
                position -= 26
            elif position < 0:
                position += 26
            code += alphabet[position]
        else:
            code += letter
    print(f"The {direction}d text is {code}\n")


while yes:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if restart == "no":
        yes = False
