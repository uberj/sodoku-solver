from random import shuffle
from board import Board
from board_filler import BoardFiller

class PuzzleCreator(object):
    def __init__(
            self,
            board=None
    ):
        self.board = board

    @staticmethod
    def random_board():
        board = Board(3, 9)
        board_filler = BoardFiller(
                board,
                shuffle_choices=True,
                shuffle_squares=True
        )
        assert board_filler.fill()
        assert board.is_valid()
        return board

    def create_puzzle(self, num_decisions, square_difficulty):
        if not self.board:
            board = PuzzleCreator.random_board()
        else:
            board = self.board
        """
        @param num_decisions: how many squares a player will need to fill
            before the board is "complete"
        @param square_difficulty: the maximum number of values the easiest square could
            possibly be
        """
        squares = list(board.all_squares())
        shuffle(squares)

        while True:
            if num_decisions == 0:
                break

            for square in squares:
                square.choice = None
                num_decisions -= 1
                if num_decisions == 0:
                    break
        return board

if __name__ == "__main__":
    for i in xrange(5, 60, 7):
        print PuzzleCreator().create_puzzle(i, 2).ascii()
