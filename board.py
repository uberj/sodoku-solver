import random
import pdb
from board_filler import fill
from coordinate import Coordinate
from itertools import permutations

class Board(object):

    def __init__(self,
            inner_square_dimension,
            dimension,
            seed=10,
            squares=[]
    ):
        self.inner_square_dimension = inner_square_dimension
        self.dimension = dimension
        self.seed = seed
        self.random = random.Random(seed)

        if not squares:
            self.squares = []
            # fill the board
            for i in xrange(dimension):
                self.squares.append([None] * dimension)
        else:
            self.squares = squares

    def set(self, coord, number):
        self.squares[coord.row][coord.col] = number

    def get(self, coord):
        return self.squares[coord.row][coord.col]

    def inner_squares(self):
        # return coordinates of inner squares in the board
        for i in xrange(self.dimension/self.inner_square_dimension):
            for j in xrange(self.dimension/self.inner_square_dimension):
                yield (
                    i * self.inner_square_dimension,
                    j * self.inner_square_dimension,
                    self.inner_square_dimension
                )

    def all_square_coordinates(self):
        return map(lambda c: Coordinate(*c), permutations(
            list(xrange(self.dimension)) +
            list(xrange(self.dimension)),
            2
        ))

    def col_set(self, col_idx):
        return set(
                filter(lambda el: (el),
                    list(row[col_idx] for row in self.squares)))

    def row_set(self, row_idx):
        return set(filter(lambda el: (el), self.squares[row_idx]))

    def is_valid(self):
        for col_idx, row in enumerate(self.squares):
            no_none_row = filter(lambda el: (el), row)
            if len(no_none_row) != len(set(no_none_row)):
                # there is something in the row more than once
                return False
            seen_col_values = set()
            for row in self.squares:
                if row[col_idx] is not None and row[col_idx] in seen_col_values:
                    return False
                seen_col_values.add(row[col_idx])

        for col_idx, row_idx, dim in self.inner_squares():
            numbers = []
            for row in self.squares[row_idx:row_idx+dim]:
                for col in row[col_idx:col_idx+dim]:
                    numbers.append(col)

            no_nones = filter(lambda el: (el), numbers)

            if len(set(no_nones)) != len(no_nones):
                return False

        return True

    def map(self, l):
        result = []
        for row in self.squares:
            for col in row:
                result.append(l(col))
        return result

    def __str__(self):
        b = ""
        for row in self.squares:
            for col in row:
                b = b + (" %s " % (col or 0))
            b = b + "\n"
        return b
