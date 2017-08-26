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
        for coord in coordinates:
            to_try = set(coordinates)
            to_try.remove(coord)
            taken = self.board.col_set(coord.col).union(
                    self.board.row_set(coord.row)
            )

            for choice in set(choices).difference(taken):
                self.i_try = self.i_try + 1
                self.board.set(coord, choice)
                # print "coord: " + str(coord)
                # print "choice: " + str(choice)
                if self.board.is_valid() and not self.already_tried(coord, choice):
                    return self._fill_coords(to_try)
                    # if success:
                        # return True

                # something didn't work out, undo the move and try the next coordinate
                # undo move
                self.board.set(coord, None)
                self.print_stats()

        return False

    def already_tried(self, coord, choice):
        board_hash = md5.md5(" ".join(self.board.map(lambda el: str(el)))).hexdigest()
        #board_hash = " ".join(self.board.map(lambda el: str(el)))
        if board_hash in self.seen_hashes:
            # print " ".join(self.board.map(lambda el: str(el)))
            # print "dupe!"
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
