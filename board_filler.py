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
        self._fill_coords(coordinates)

    def work(self, coord):
        choices = list(xrange(1, self.board.dimension + 1))
        while True:
            shuffle(choices)
            for choice in choices:
                self.board.set(coord, choice)
                self.print_stats()
                if self.board.is_valid() and not self.already_tried(coord, choice):
                    yield True
                else:
                    self.board.set(coord, None)
            yield False


    def _fill_coords(self, coordinates):
        return True
        workers = []
        for coord in coordinates:
            workers.append(self.work(coord))

        while True:
            for worker in workers:
                worker.next()

        for row in self.squares:
            for col in row:
                result.append(l(col))

        # get coordinates
        if not coordinates:
            return True
        choices = list(xrange(1, self.board.dimension))
        #shuffle(choices)
        coord = coordinates.pop()
        print coord

        taken = self.board.col_set(coord.col).union(
                self.board.row_set(coord.row)
        )

        good_choices = set(choices).difference(taken)
        for choice in sorted(list(good_choices)):
            self.i_try = self.i_try + 1
            self.board.set(coord, choice)
            # print "coord: " + str(coord)
            # print "choice: " + str(choice)
            if self.board.is_valid() and not self.already_tried(coord, choice):
                success = self._fill_coords(coordinates)
                if success:
                    return True
                # if success:
                    # return True

            # something didn't work out, undo the move and try the next coordinate
            # undo move
            self.board.set(coord, None)
            self.print_stats()

        # we failed to place for this coordinate
        coordinates.insert(0, coord)
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
