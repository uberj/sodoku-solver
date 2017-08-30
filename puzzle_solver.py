import sys
import pdb
from coordinate import Coordinate
from square import Square
from board_reader import BoardReader
from board_filler import BoardFiller
from board import Board

def with_coords(choices):
    for row_idx, row in enumerate(choices):
        for col_idx, col in enumerate(row):
            if row[col_idx] is None:
                mutable = True
            else:
                mutable = False
            row[col_idx] = Square(
                    choice=col,
                    coordinate=Coordinate(row_idx, col_idx),
                    mutable=mutable
            )
    return choices

if __name__ == "__main__":
    # print squares
    reader = None
    if len(sys.argv) == 1:
        reader = BoardReader.from_fd(sys.stdin)
    else:
        reader = BoardReader.from_fnames(sys.argv[1:])
    board = Board(3, 9, squares=list(with_coords(reader.list_squares()[0])))
    print "Game board:"
    print board
    board_filler = BoardFiller(
            board,
            shuffle_choices=True,
            shuffle_squares=True,
            stats_on=False
    )
    assert board_filler.fill()
    print "Solution:"
    print board
