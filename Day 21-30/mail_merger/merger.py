
class Merger:
    def __init__(self):

        self.name_list =  []
        

        with open(r"Input/Names/invited_names.txt") as file:
            names_raw = file.readlines()

        for names in names_raw:
            formatted_name = names.strip("\n'")
            self.name_list.append(formatted_name)


    def letter_body(self):
        with open("Input\Letters\starting_letter.txt") as file:
            return file.read()

    def new_letter(self, name, letter):
        with open(f"Output\ReadyToSend\letter_for_{name}.txt", mode='w') as file:
            file.write(letter)
    



