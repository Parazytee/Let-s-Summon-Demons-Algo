

class Board:
    def __init__(self):
        self.cards = []
        self.demons = []

    def AddCards(self, card):
        self.cards.append(card)

    def AddDemons(self, demon):
        self.demons.append(demon)

    def print(self, obj=None):
        print("Souls: ", self.souls, "\n")
        print("Cards : ")
        for i in self.cards:
            i.print()
        print("Demons : ")
        for i in self.demons:
            i.print()
