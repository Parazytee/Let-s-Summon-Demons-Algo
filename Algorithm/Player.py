
class Player:
    def __init__(self, controller, controllerName, board: Board, demons: list[Demon]):
        self.controller = controller  # ai or human
        self.controllerName = controllerName
        self.board = board
        self.demons = demons
