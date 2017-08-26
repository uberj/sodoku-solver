import random
import pdb
from board_filler import fill

class Board(object):

    def __init__(self,
            inner_square_dimension,
            board_dimension,
            seed=10,
            squares=[]
    ):
        self.inner_square_dimension = inner_square_dimension
        self.board_dimension = board_dimension
        self.seed = seed
        self.random = random.Random(seed)

        if not squares:
            self.squares = []
            # fill the board
            for i in xrange(board_dimension):
                self.squares.append([None] * board_dimension)
        else:
            self.squares = squares


    def inner_squares(self):
        for i in xrange(self.board_dimension/self.inner_square_dimension):
            for j in xrange(self.board_dimension/self.inner_square_dimension):
                yield (
                    i * self.inner_square_dimension,
                    j * self.inner_square_dimension,
                    self.inner_square_dimension
                )

    def col_set(self, col_idx):
        return set(
                filter(lambda el: (el),
                    list(row[col_idx] for row in self.squares)))

    def row_set(self, row_idx):
        return set(filter(lambda el: (el), self.squares[row_idx]))

    def __str__(self):
        b = ""
        for row in self.squares:
            for col in row:
                b = b + (" %s " % (col))
            b = b + "\n"
        return b
