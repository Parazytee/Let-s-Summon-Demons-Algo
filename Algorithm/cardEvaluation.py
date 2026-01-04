import projectVariables as const
import Utility as U


def EffectEV(ID):
    match ID:
        case 1:
            SoulGenEV()


def SoulGenEV(soulsGained, number):
    return soulsGained*U.D_DiceTotal(const.NUMBER_OF_DICE, const.NUMBER_OF_FACES, number)


def StealSoulsEV():
    # for all players in the game
    return
