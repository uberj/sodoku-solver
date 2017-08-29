from random import shuffle
from itertools import permutations, chain
from board import Board
import pdb
import sys
import time
import md5

class BoardFiller(object):
    dupe_count = 0
    i_try = 0
    none_count = 99999
    best_none_count = 9999
    seen_hashes = set()
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
        squares = list(self.all_squares())
        if self.shuffle_squares:
            shuffle(squares)
        return self._fill_squares(squares)

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

    def choose_next_square(self, squares):
        for num_choices in xrange(0, self.board.dimension + 1):
            if self.shuffle_squares:
                shuffle(squares)
            for j, square in enumerate(squares):
                if len(self.square_choices(square)) == num_choices:
                    return squares[j], squares[0:j] + squares[j+1:]
        return squares[0], squares[:1]

    def _fill_squares(self, squares):
        if not squares:
            return True
        square, to_try_next = self.choose_next_square(squares)
        choices = self.square_choices(square)
        for choice in choices:
            square.choice = choice
            if self.leaves_no_choices_for_others(square):
                continue

            self.print_stats()

            if self.shuffle_squares:
                shuffle(to_try_next)
            success = self._fill_squares(to_try_next)

            if success:
                return True

        # None of squares choices worked. undo and let the caller know to try
        # their next choice
        square.choice = None
        return False

    def leaves_no_choices_for_others(self, square):
        is_candidate = lambda s: s.coordinate != square.coordinate and s.choice is None
        neighbors = filter(is_candidate, self.board.game_set(square.coordinate))
        for neighbor_square in neighbors:
            if not self.square_choices(neighbor_square):
                return True
        return False

    def already_tried(self):
        board_hash = md5.md5(" ".join(self.board.map(lambda el: str(el.choice)))).hexdigest()
        if board_hash in self.seen_hashes:
            return True
        self.seen_hashes.add(board_hash)
        return False

    def print_stats(self):
        if self.already_tried():
            self.dupe_count = self.dupe_count + 1
        self.none_count = len(filter(
            lambda el: (el is None), self.board.map(lambda el: (el.choice))))
        self.best_none_count = min(
                self.none_count,
                self.best_none_count 
        )
        self.i_try = self.i_try + 1
        if (self.i_try) % 1000 == 0:
            print self.board
            print "Num tries: " + str(self.i_try)
            print "Dupe count: " + str(self.dupe_count)
            print "None count: " + str(self.none_count)
            print "Best none count: " + str(self.best_none_count)

if __name__ == "__main__":
    board = Board(3, 9)
    assert BoardFiller(
            board,
            shuffle_choices=True,
            shuffle_squares=True
    ).fill()
    assert board.is_valid()
    print board
