from board import Board
from board_filler import BoardFiller

class PuzzleCreator(object):
    def __init__(
            self,
            board=None
    ):
        self.board = board
        if not board:
            self.board = PuzzleCreator.random_board()

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

    # Note: this is dupe code from BoardFiller. might need move it
    def square_choices(self, square):
        taken = filter(lambda el: (el),
                map(lambda s: s.choice, self.board.game_set(square.coordinate)))
        choices = list(set(self.choices).difference(taken))
        return choices

    def create_puzzle(self, num_decisions, square_difficulty):
        """
        @param num_decisions: how many squares a player will need to fill
            before the board is "complete"
        @param square_difficulty: the maximum number of values the easiest square could
            possibly be
        """




print random_board()
