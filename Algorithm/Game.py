import Board as bd
import Card
import numpy as np
import Player as pl
import projectVariables as const


class Game:
    def __init__(self, players: list = [], turn=0, block: list = [], discard: list = [], deck: list = [], demonDiscard: list = [], demonDeck: list = []):
        self.players = players
        self.turn = turn
        self.playerIndex = 0
        self.block = block
        self.discard = discard
        self.deck = deck
        self.demonDiscard = demonDiscard
        self.demonDeck = demonDeck
        self.active = True

    def NextTurn(self, skipTime=False):
        # when skip

        self.turn += 1
        self.FillBlock()
        if skipTime:
            # target to self
            return

        self.playerIndex = (self.playerIndex + 1) % len(self.players)
        # need to do something about active players
        return

    def InitializeDeck(self):
        # prend un json maybe?
        self.ShuffleDeck(self.deck)
        return

    def ShuffleDeck(self, deck):
        np.random.shuffle(deck)
        return

    def GetTopCard(self):
        return self.deck.pop()

    def FillBlock(self):
        while len(self.block) < const.MAX_CARDS_IN_BLOCK:
            self.block.append(self.deck.pop())

    def InitializeDemons(self):
        self.ShuffleDeck(self.demonDeck)
        return

    def DrawDemons(self):
        return self.demonDeck.pop()

    def AssignDemons(self):
        for i in self.players:
            for j in range(0, const.NUMBER_OF_DEMONS_TO_WIN):
                i.demons.append(self.DrawDemons())
        return

    def CheckIfWin(self):
        # idk how i'll manage this as it could be at any point.
        return

    def Roll(self):
        result = 0
        for i in range(0, const.NUMBER_OF_DICE):
            result += np.random.randint(1, const.NUMBER_OF_FACES)
        return result

    def PlayGame(self):
        self.players.append(pl.Player("Human", "Nora", bd.Board()))

        self.InitializeDeck()
        self.InitializeDemons()
        self.AssignDemons()
        self.FillBlock()

        while self.active:
            # do stuff here
            self.Roll()
            # Decision Aglo or player action here
            self.NextTurn()

        return
