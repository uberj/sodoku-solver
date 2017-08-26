from random import shuffle

def fill(self, board):
    """
    Pick inner square
        * calculate possible inner square permutations
        * iterate through perms and check for row col validitity
            * if valid choice is found, recurse into next inner square
    """
    for inner_square in board.inner_squares():
        numbers = list(xrange(board.inner_square_dimension))
        shuffle(numbers)
        for perm in numbers:
            if valid_state(board, inner_square, numbers):
                return

def valid_state(board, inner_square, numbers):
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

