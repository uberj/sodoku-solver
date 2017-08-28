import random
import pdb
from coordinate import Coordinate
from itertools import permutations, chain
from square import Square

class Board(object):

    def __init__(self,
            inner_square_dimension,
            dimension,
            seed=10,
            squares=[],
            choices=None
    ):
        self.inner_square_dimension = inner_square_dimension
        self.dimension = dimension
        self.seed = seed
        self.random = random.Random(seed)
        self.choices=choices or list(xrange(1, dimension + 1))

        if not squares:
            self.squares = []
            # fill the board
            for i in xrange(dimension):
                self.squares.append([None] * dimension)
            coordinates = sorted(list(set(self.all_square_coordinates())))
            choices = list(xrange(1, self.dimension + 1))
            for coord in coordinates:
                self.squares[coord.row][coord.col] = Square(
                        choice=None,
                        coordinate=coord
                )
        else:
            self.squares = squares

    def square_choices(self, square):
        taken = filter(lambda el: (el),
                map(lambda s: s.choice, self.game_set(square.coordinate)))
        return set(self.choices).difference(taken)

    def set(self, coord, number, choices):
        self.squares[coord.row][coord.col].choice = number
        self.squares[coord.row][coord.col].choices = choices

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
        cords = reversed(sorted(list(xrange(self.dimension)) + list(xrange(self.dimension))))
        return map(lambda c: Coordinate(*c), permutations(
            cords,
            2
        ))

    def col_set(self, col_idx):
        for row in self.squares:
            yield row[col_idx]

    def row_set(self, row_idx):
        return self.squares[row_idx]

    def game_set(self, coord):
        return chain(
                self.col_set(coord.col),
                self.row_set(coord.row),
                self.inner_square_set(coord))

    def inner_square_set(self, coord):
        for col_idx, row_idx, dim in self.inner_squares():
            if (coord.row >= row_idx and coord.row < row_idx + dim
                    and
                coord.col >= col_idx and coord.col < col_idx + dim
            ):
                squares = []
                for row in self.squares[row_idx:row_idx+dim]:
                    for col in row[col_idx:col_idx+dim]:
                        squares.append(col)
                return squares

        raise Exception("no inner square found for coord " + str(coord))

    def is_valid(self):
        for row_idx, row in enumerate(self.squares):
            no_none_row = filter(lambda el: (el), map(lambda el: el.choice, row))
            if len(no_none_row) != len(set(no_none_row)):
                # there is something in the row more than once
                return False
            seen_col_values = set()
            for row in self.squares:
                if row[row_idx].choice is not None and row[row_idx].choice in seen_col_values:
                    return False
                seen_col_values.add(row[row_idx].choice)

        for col_idx, row_idx, dim in self.inner_squares():
            numbers = []
            for row in self.squares[row_idx:row_idx+dim]:
                for col in row[col_idx:col_idx+dim]:
                    numbers.append(col.choice)

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
