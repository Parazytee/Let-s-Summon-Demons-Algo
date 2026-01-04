

import Board as bd
import Card
import Player as pl


def ActivateEffect(ID):
    match ID:
        case 1:
            SoulGen()


def SoulGen(soulsGained, target: pl.Player):
    target.souls += soulsGained
    return


def StealSouls(soulsStolen, targetGain: pl.Player, targetSteal: pl.Player):
    targetSteal.souls = max(targetSteal.souls-soulsStolen, 0)
    # will probably need to add a check for the demon that stops steals
    targetGain.souls += soulsStolen
    return


def ObtainCardBlock(card: Card, target: pl.Player):
    targetBoard: bd.Board = target.board
    targetBoard.AddCards(card)
    return
