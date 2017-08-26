from random import shuffle
from itertools import permutations

i_try = 0

def fill(board):
    """
    Pick inner square
        * calculate possible inner square permutations
        * iterate through perms and check for row col validitity
            * if valid choice is found, recurse into next inner square
    """
    coordinates = board.all_square_coordinates()
    shuffle(coordinates)
    _fill_one_coord(board, coordinates)

def get_perms(cur_square, board):
    # figure out which inner square permutations we should try
    # don't do elimitation right now, optimize later
    numbers = list(xrange(board.inner_square_dimension * board.inner_square_dimension))
    return permutations(numbers)

def _fill_one_coord(board, coordinates):
    # get coordinates
    if not coordinates:
        return True
    choices = list(xrange(1, board.dimension))
    for coord in coordinates:
        choices_so_far = set()
        shuffle(choices)
        to_try = set(coordinates)
        to_try.remove(coord)
        for choice in choices:
            global i_try
            i_try = i_try + 1
            board.set(coord, choice)
            if board.is_valid():
                success = _fill_one_coord(board, to_try)
                if success:
                    return True

            # something didn't work out, undo the move and try the next coordinate
            # undo move
            board.set(coord, None)
            if i_try % 10000 == 0:
                print board
                print "num Nones: " + str(len(filter(lambda el: (el),
                    board.map(lambda el: (el)))))
    return False

def valid_inner_state(board, inner_square, numbers):
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

