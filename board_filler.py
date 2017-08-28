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
    choices = []

    def __init__(
            self,
            board,
            shuffle_choices=False,
            shuffle_squares=False
    ):
        self.board = board
        self.choices = list(xrange(1, self.board.dimension + 1))
        self.shuffle_squares = shuffle_squares
        self.shuffle_choices = shuffle_choices

    def fill(self):
        """
        Pick inner square
            * calculate possible inner square permutations
            * iterate through perms and check for row col validitity
                * if valid choice is found, recurse into next inner square
        """
        squares = list(self.all_squares())
        if self.shuffle_squares:
            shuffle(squares)
        self._fill_squares(squares)

    def all_squares(self):
        for row in self.board.squares:
            for square in row:
                yield square

    def square_choices(self, square):
        taken = filter(lambda el: (el),
                map(lambda s: s.choice, self.board.game_set(square.coordinate)))
        choices = list(set(self.choices).difference(taken))
        if self.shuffle_choices:
            shuffle(choices)
        return choices

    def _fill_squares(self, squares):
        if not squares:
            return True
        square = squares[0]
        choices = self.square_choices(square)
        for choice in choices:
            square.choice = choice
            self.print_stats()
            success = self._fill_squares(squares[1:])
            if success:
                return True
        # None of squares choices worked. undo and let the caller know to try
        # their next choice
        square.choice = None
        return False

    def already_tried(self, coord, choice):
        board_hash = md5.md5(" ".join(self.board.map(lambda el: str(el.choice)))).hexdigest()
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
            none_count = len(filter(lambda el: (el.choice), self.board.map(lambda el: (el))))
            self.best_none_count = min(
                    none_count,
                    self.best_none_count 
            )
            print "None count: " + str(none_count)
            print "Best none count: " + str(self.best_none_count)
