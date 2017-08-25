import random
import pdb
from board_filler import fill

class Board(object):

    def __init__(self, inner_square_dimension, board_dimension, seed=10):
        self.squares = []
        self.inner_square_dimension = inner_square_dimension
        self.board_dimension = board_dimension
        self.seed = seed
        self.random = random.Random(seed)

        for i in xrange(board_dimension):
            self.squares.append([None] * board_dimension)

    def inner_squares(self):
        for i in xrange(self.board_dimension/self.inner_square_dimension):
            for j in xrange(self.board_dimension/self.inner_square_dimension):
                yield (
                    i * self.inner_square_dimension,
                    j * self.inner_square_dimension,
                    self.inner_square_dimension
                )

    def __str__(self):
        b = ""
        for row in self.squares:
            for col in row:
                b = b + (" %s " % (col))
            b = b + "\n"
        return b
