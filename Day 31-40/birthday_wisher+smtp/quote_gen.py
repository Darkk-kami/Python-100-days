def random_quote():
    from random import choice
    with open('quotes.txt', 'r') as file:
        data = file.readlines()
        return choice(data)


class Quote:
    def __init__(self):
        self.quote = random_quote()
