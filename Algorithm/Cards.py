

class Card:
    def __init__(self, ID: int, name, type, subtype, number: int):
        self.ID = ID
        self.name = name
        self.type = type
        self.subtype = subtype
        self.number = number

    def remove(self):
        return

    def buy(self):  # might not be necessary
        return

    def obtain(self):
        return

    def effect(self, ID):  # assignate this one on creation for better perf

        return

    def EV(self, ID):  # assignate this one too
        return

    def print(self):
        print(self.ID, " - ", self.name, " - ", self.number,
              " - ", self.subtype, " ", self.type)
