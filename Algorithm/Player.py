import Board
import Demon
import projectVariables as const


class Player:
    def __init__(self, controller, controllerName, board: Board, demons: list = [], souls: int = const.INITIAL_SOULS):
        self.controller = controller  # ai or human
        self.controllerName = controllerName
        self.board = board
        self.demons = demons
        self.souls = souls

    def GetBoard(self) -> Board:
        return self.board
