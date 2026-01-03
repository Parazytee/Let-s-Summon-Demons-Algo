import projectVariables as const


class Board:
    def __init__(self,  souls=const.INITIAL_SOULS):
        self.cards = []
        self.demons = []
        self.souls = souls

    def addCards(self, card):
        self.cards.append(card)

    def addDemons(self, demon):
        self.demons.append(demon)

    def print(self, obj=None):
        print("Souls: ", self.souls, "\n")
        print("Cards : ")
        for i in self.cards:
            i.print()
        print("Demons : ")
        for i in self.demons:
            i.print()
