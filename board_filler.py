from random import shuffle

def fill(self, board):
    """
    Pick inner square
        * calculate possible inner square permutations
        * iterate through perms and check for row col validitity
            * if valid choice is found, recurse into next inner square
    """
    for row, col, dim in board.inner_squares():
        numbers = list(xrange(board.inner_square_dimension))
        shuffle(numbers)
        for perm in numbers:
            if valid_state(board, inner_square):
                return
