import unittest
from coordinate import Coordinate
import pdb
from board import Board
from board_filler import BoardFiller

class BoardTest(unittest.TestCase):
    def test_inner_squares_size(self):
        board = Board(3, 9)
        inner_squares = board.inner_squares()
        self.assertEquals(9, len(list(inner_squares)))

    def test_inner_squares_indexes(self):
        board = Board(3, 9)
        inner_squares = list(board.inner_squares())
        self.assertEquals((0, 0, 3), inner_squares[0])
        self.assertEquals((0, 3, 3), inner_squares[1])
        self.assertEquals((0, 6, 3), inner_squares[2])

        self.assertEquals((3, 0, 3), inner_squares[3])
        self.assertEquals((3, 3, 3), inner_squares[4])
        self.assertEquals((3, 6, 3), inner_squares[5])

        self.assertEquals((6, 0, 3), inner_squares[6])
        self.assertEquals((6, 3, 3), inner_squares[7])
        self.assertEquals((6, 6, 3), inner_squares[8])

    test_board = lambda (_): [
        [1, 2, 3,    4, 5, 6,   7, 8, 9],
        [4, 5, 6,    7, 8, 9,   1, 2, 3],
        [7, 8, 9,    1, 2, 3,   4, 5, 6],

        [9, 1, 2,    3, 4, 5,   6, 7, 8],
        [3, 4, 5,    6, 7, 8,   9, 1, 2],
        [6, 7, 8,    9, 1, 2,   3, 4, 5],

        [8, 9, 1,    2, 3, 4,   5, 6, 7],
        [2, 3, 4,    5, 6, 7,   8, 9, 1],
        [5, 6, 7,    8, 9, 1,   2, 3, 4]
    ]

    squares_with_nones = [
            [None, None, None,  4, 5, 6,   7, 8, 9],
            [None, None, None,  7, 8, 9,   1, 2, 3],
            [None, None, None,  1, 2, 3,   4, 5, 6],

            [9, 1, 2,    3, 4, 5,   6, 7, 8],
            [3, 4, 5,    6, 7, 8,   9, 1, 2],
            [6, 7, 8,    9, 1, 2,   3, 4, 5],

            [8, 9, 1,    2, 3, 4,   5, 6, 7],
            [2, 3, 4,    5, 6, 7,   8, 9, 1],
            [5, 6, 7,    8, 9, 1,   2, 3, 4]
    ]

    sparse_board = lambda (_): [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, 5, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]
    ]

    def test_valid_state(self):
        test_board_with_nones = Board(3, 9, squares=list(self.squares_with_nones))
        self.assertTrue(
                BoardFiller(test_board_with_nones).valid_inner_state((0, 0, 3), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        )
        self.assertFalse(
                BoardFiller(test_board_with_nones).valid_inner_state((0, 0, 3), [2, 1, 3, 4, 5, 6, 7, 8, 9])
        )

        # test none's are gone
        self.assertEquals(test_board_with_nones.col_set(0), set([9, 3, 6, 8, 2, 5]))
        self.assertEquals(test_board_with_nones.row_set(0), set([4, 5, 6, 7, 8, 9]))

    def test_col_set(self):
        board = Board(3, 9, squares=self.test_board())
        self.assertEquals(board.col_set(0), set([1, 4, 7, 9, 3, 6, 8, 2, 5]))
        self.assertEquals(board.col_set(1), set([2, 5, 8, 1, 4, 7, 9, 3, 6]))
        self.assertEquals(board.col_set(8), set([9, 3, 6, 8, 2, 5, 7, 1, 4]))

    def test_row_set(self):
        board = Board(3, 9, squares=self.test_board())
        self.assertEquals(board.row_set(0), set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEquals(board.row_set(1), set([4, 5, 6, 7, 8, 9, 1, 2, 3]))
        self.assertEquals(board.row_set(8), set([5, 6, 7, 8, 9, 1, 2, 3, 4]))

    def test_is_valid_row_dupe(self):
        board = Board(3, 9, squares=self.test_board())
        self.assertTrue(board.is_valid())
        board.set(Coordinate(0, 0), board.get(Coordinate(5, 0)))
        self.assertFalse(board.is_valid())

    def test_is_valid_col_dupe(self):
        board = Board(3, 9, squares=self.test_board())
        self.assertTrue(board.is_valid())
        board.set(Coordinate(0, 0), board.get(Coordinate(0, 5)))
        self.assertFalse(board.is_valid())

    def test_is_valid_inner_square_dupe(self):
        board = Board(3, 9, squares=self.test_board())
        self.assertTrue(board.is_valid())
        board.set(Coordinate(0, 0), board.get(Coordinate(0, 1)))
        self.assertFalse(board.is_valid())

    def test_is_valid_sparse(self):
        board = Board(3, 9, squares=self.sparse_board())
        self.assertTrue(board.is_valid())

    def test_board_hash(self):
        board = Board(3, 9)
        BoardFiller(board).fill()
        print board

    def test_fill(self):
        board = Board(3, 9)
        #BoardFiller(board).fill()
        #print board

if __name__ == '__main__':
    unittest.main()
