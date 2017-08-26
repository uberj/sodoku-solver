from random import shuffle
from itertools import permutations


class BoardFiller(object):
    i_try = 0
    best_none_count = 9999
    def fill(self, board):
        """
        Pick inner square
            * calculate possible inner square permutations
            * iterate through perms and check for row col validitity
                * if valid choice is found, recurse into next inner square
        """
        coordinates = board.all_square_coordinates()
        shuffle(coordinates)
        _fill_one_coord(board, coordinates)

    def _fill_one_coord(self, board, coordinates):
        # get coordinates
        if not coordinates:
            return True
        choices = list(xrange(1, board.dimension))
        for coord in coordinates:
            shuffle(choices)
            to_try = set(coordinates)
            to_try.remove(coord)
            for choice in choices:
                i_try = i_try + 1
                board.set(coord, choice)
                if board.is_valid():
                    success = _fill_one_coord(self, board, to_try)
                    if success:
                        return True

                # something didn't work out, undo the move and try the next coordinate
                # undo move
                board.set(coord, None)
                if i_try % 10000 == 0:
                    print board
                    global best_none_count 
                    none_count = len(filter(lambda el: (el), board.map(lambda el: (el))))
                    best_none_count = min(
                            none_count,
                            best_none_count 
                    )
                    print "None count: " + str(none_count)
                    print "Best none count: " + str(best_none_count)
        return False

    def valid_inner_state(self, board, inner_square, numbers):
        """
        See if numbers are valid in inner_sqare given board state `board`

        @param board: is the current state
        @param inner_square: is where we are looking to validate numbers
        @param numbers: the proposed new state to go into inner_square 
        """
        start_row, start_col, dim = inner_square
        for i, row_idx in enumerate(xrange(start_row, start_row + dim)):
            existing_row_set = board.row_set(row_idx)
            proposed_row_set = set()
            for i in xrange(i * dim, (i + 1) * dim):
                proposed_row_set.add(numbers[i])

            if len(existing_row_set.intersection(proposed_row_set)) != 0:
                return False

        for i, col_idx in enumerate(xrange(start_col, start_col + dim)):
            existing_col_set = board.col_set(col_idx)
            proposed_col_set = set()
            for i in xrange(i, len(numbers), dim):
                proposed_col_set.add(numbers[i])

            if len(existing_col_set.intersection(proposed_col_set)) != 0:
                return False

        return True

