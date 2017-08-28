from random import shuffle
import pdb
import sys
from itertools import permutations
import time
import md5


class BoardFiller(object):
    i_try = 0
    best_none_count = 9999
    seen_hashes = set()
    choice_board = {}

    def __init__(self, board):
        self.board = board
        coordinates = sorted(list(set(self.board.all_square_coordinates())))
        choices = list(xrange(1, self.board.dimension + 1))
        for coord in coordinates:
            choice_board.put(coord, choices)

    def fill(self):
        """
        Pick inner square
            * calculate possible inner square permutations
            * iterate through perms and check for row col validitity
                * if valid choice is found, recurse into next inner square
        """
        #shuffle(coordinates)
        squares = self.all_squares()
        self._fill_squares(squares)

    def all_squares(self):
        for row in self.squares:
            for square in row:
                yield square

    def _fill_squares(self, squares):
        square = squares.pop()
        choices = square['choices']
        # for choice in choices:
            # square['choice'] = choice
            # for s in self.row_set(square['coord'].row):
                # s['choices'].remove(choice)
            # for square in self.
            # for col_idx, row_id, dim in self.inner_squares():
                # if square['col']

            # self.col_set(square['coord'].col)
            # square['choices'] = []
            # self._fill_squares(squares)
        return False

    def already_tried(self, coord, choice):
        board_hash = md5.md5(" ".join(self.board.map(lambda el: str(el['choice'])))).hexdigest()
        #board_hash = " ".join(self.board.map(lambda el: str(el)))
        if board_hash in self.seen_hashes:
            # print " ".join(self.board.map(lambda el: str(el)))
            return True
        self.seen_hashes.add(board_hash)
        return False


    def print_stats(self):
        # if (self.i_try + 1) % 100 == 0:
        if True:
            print self.board
            none_count = len(filter(lambda el: (el['choice']), self.board.map(lambda el: (el))))
            self.best_none_count = min(
                    none_count,
                    self.best_none_count 
            )
            print "None count: " + str(none_count)
            print "Best none count: " + str(self.best_none_count)
