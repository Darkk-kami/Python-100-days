import pandas


class DataManager:

    def __init__(self, file):
        self.file = pandas.read_csv(f"data/{file}.csv")
        self.cards = [(row.Japanese, row.Kanji, row.English) for index, row in self.file.iterrows()]
