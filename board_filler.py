from random import shuffle
import sys
from itertools import permutations
import time
import md5


class BoardFiller(object):
    i_try = 0
    best_none_count = 9999
    seen_hashes = set()

    def __init__(self, board):
        self.board = board

    def fill(self):
        """
        Pick inner square
            * calculate possible inner square permutations
            * iterate through perms and check for row col validitity
                * if valid choice is found, recurse into next inner square
        """
        coordinates = self.board.all_square_coordinates()
        shuffle(coordinates)
        self._fill_coords(coordinates)

    def _fill_coords(self, coordinates):
        # get coordinates
        if not coordinates:
            return True
        choices = list(xrange(1, self.board.dimension))
        shuffle(choices)
        for coord in coordinates:
            to_try = set(coordinates)
            to_try.remove(coord)
            for choice in choices:
                self.i_try = self.i_try + 1
                self.board.set(coord, choice)
                print "coord: " + str(coord)
                print "choice: " + str(choice)
                if self.board.is_valid() and not self.already_tried(coord, choice):
                    success = self._fill_coords(to_try)
                    if success:
                        return True

                # something didn't work out, undo the move and try the next coordinate
                # undo move
                self.board.set(coord, None)
                self.print_stats()
        return False

    def already_tried(self, coord, choice):
        board_hash = md5.md5(" ".join(self.board.map(lambda el: str(el)))).hexdigest()
        #board_hash = " ".join(self.board.map(lambda el: str(el)))
        if board_hash in self.seen_hashes:
            print "dupe!"
            return True
        self.seen_hashes.add(board_hash)
        return False


    def print_stats(self):
        if (self.i_try + 1) % 10000 == 0:
            print self.board
            none_count = len(filter(lambda el: (el), self.board.map(lambda el: (el))))
            self.best_none_count = min(
                    none_count,
                    self.best_none_count 
            )
            print "None count: " + str(none_count)
            print "Best none count: " + str(self.best_none_count)

    def valid_inner_state(self, inner_square, numbers):
        """
        See if numbers are valid in inner_sqare given board state `board`

        @param board: is the current state
        @param inner_square: is where we are looking to validate numbers
        @param numbers: the proposed new state to go into inner_square 
        """
        start_row, start_col, dim = inner_square
        for i, row_idx in enumerate(xrange(start_row, start_row + dim)):
            existing_row_set = self.board.row_set(row_idx)
            proposed_row_set = set()
            for i in xrange(i * dim, (i + 1) * dim):
                proposed_row_set.add(numbers[i])

            if len(existing_row_set.intersection(proposed_row_set)) != 0:
                return False

        for i, col_idx in enumerate(xrange(start_col, start_col + dim)):
            existing_col_set = self.board.col_set(col_idx)
            proposed_col_set = set()
            for i in xrange(i, len(numbers), dim):
                proposed_col_set.add(numbers[i])

            if len(existing_col_set.intersection(proposed_col_set)) != 0:
                return False

        return True

