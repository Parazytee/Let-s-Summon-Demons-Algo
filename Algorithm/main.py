
import classes as cl


def main():
    board1 = cl.Board(10)
    demon1 = cl.Demon(1, "TEST.D", 7)
    player1 = cl.Player("player", "Nora", board1, [demon1])

    print(board1.souls)
    player1.board.addDemons(demon1)
    player1.board.addCards(cl.Card(123, "Adam", "Child", "Normal", 8))
    player1.board.print()


main()
