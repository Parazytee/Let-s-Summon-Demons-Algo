import projectVariables as const


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

    def effect(self):  # assignate this one on creation for better perf
        return

    def print(self):
        print(self.ID, " - ", self.name, " - ", self.number,
              " - ", self.subtype, " ", self.type)


class Demon:
    def __init__(self, ID: int, name, number: int):
        self.ID = ID
        self.name = name
        self.number = number

    def obtain(self):
        return

    def effect(self):
        return

    def remove(self):
        return

    def print(self):
        print(self.ID, " - ", self.name, " - ", self.number)


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


class Player:
    def __init__(self, controller, controllerName, board: Board, demons: list[Demon]):
        self.controller = controller  # ai or human
        self.controllerName = controllerName
        self.board = board
        self.demons = demons
