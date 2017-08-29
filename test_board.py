import unittest
from coordinate import Coordinate
from square import Square
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

    squares_with_nones = lambda (_): [
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
        board = Board(3, 9, squares=self.with_coords(list(self.squares_with_nones())))

        # test none's are gone
        self.assertEquals(self.to_values(board.col_set(Coordinate(0,0))), set([9, 3, 6, 8, 2, 5]))
        self.assertEquals(self.to_values(board.row_set(Coordinate(0,0))), set([4, 5, 6, 7, 8, 9]))
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        square_0_0 = board.get(Coordinate(0,0))
        self.assertEquals(board.square_choices(square_0_0, choices), [1])

        square_0_1 = board.get(Coordinate(0,1))
        self.assertEquals(board.square_choices(square_0_1, choices), [2])

        square_0_2 = board.get(Coordinate(0,2))
        self.assertEquals(board.square_choices(square_0_2, choices), [3])

        square_1_0 = board.get(Coordinate(1,0))
        self.assertEquals(board.square_choices(square_1_0, choices), [4])

        square_1_1 = board.get(Coordinate(1,1))
        self.assertEquals(board.square_choices(square_1_1, choices), [5])

        square_1_2 = board.get(Coordinate(1,2))
        self.assertEquals(board.square_choices(square_1_2, choices), [6])

        square_2_0 = board.get(Coordinate(2,0))
        self.assertEquals(board.square_choices(square_2_0, choices), [7])

        square_2_1 = board.get(Coordinate(2,1))
        self.assertEquals(board.square_choices(square_2_1, choices), [8])

        square_2_2 = board.get(Coordinate(2,2))
        self.assertEquals(board.square_choices(square_2_2, choices), [9])

        square_3_3 = board.get(Coordinate(3,3))
        self.assertEquals(board.square_choices(square_3_3, choices), [])

    def to_values(self, squares):
        return set(filter(lambda el: (el), map(lambda s: s.choice, squares)))

    def with_coords(self, choices):
        for row_idx, row in enumerate(choices):
            for col_idx, col in enumerate(row):
                row[col_idx] = Square(
                        choice=col,
                        coordinate=Coordinate(row_idx, col_idx))
        return choices


    def test_col_set(self):
        board = Board(3, 9, squares=self.with_coords(self.test_board()))
        self.assertEquals(self.to_values(board.col_set(Coordinate(0, 0))), set([1, 4, 7, 9, 3, 6, 8, 2, 5]))
        self.assertEquals(self.to_values(board.col_set(Coordinate(1, 1))), set([2, 5, 8, 1, 4, 7, 9, 3, 6]))
        self.assertEquals(self.to_values(board.col_set(Coordinate(8, 8))), set([9, 3, 6, 8, 2, 5, 7, 1, 4]))

    def test_row_set(self):
        board = Board(3, 9, squares=self.with_coords(self.test_board()))
        self.assertEquals(self.to_values(board.row_set(Coordinate(0, 0))), set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEquals(self.to_values(board.row_set(Coordinate(1, 1))), set([4, 5, 6, 7, 8, 9, 1, 2, 3]))
        self.assertEquals(self.to_values(board.row_set(Coordinate(8, 8))), set([5, 6, 7, 8, 9, 1, 2, 3, 4]))

    def test_is_valid_row_dupe(self):
        board = Board(3, 9, squares=self.with_coords(self.test_board()))
        self.assertTrue(board.is_valid())
        board.set(Coordinate(0, 0), board.get(Coordinate(5, 0)).choice)
        self.assertFalse(board.is_valid())

    def test_is_valid_col_dupe(self):
        board = Board(3, 9, squares=self.with_coords(self.test_board()))
        self.assertTrue(board.is_valid())
        board.set(Coordinate(0, 0), board.get(Coordinate(0, 5)).choice)
        self.assertFalse(board.is_valid())

    def test_is_valid_inner_square_dupe(self):
        board = Board(3, 9, squares=self.with_coords(self.test_board()))
        self.assertTrue(board.is_valid())
        board.set(Coordinate(0, 0), board.get(Coordinate(0, 1)).choice)
        self.assertFalse(board.is_valid())

    def test_is_valid_sparse(self):
        board = Board(3, 9, squares=self.with_coords(self.sparse_board()))
        self.assertTrue(board.is_valid())

    def test_board_hash(self):
        board = Board(3, 9, squares=self.with_coords(list(self.squares_with_nones())))
        # BoardFiller(board).fill()
        # print board


    no_random_board = lambda (_): [
            [1,  2,  3,  4,  5,  6,  7,  8,  9],
            [4,  5,  6,  7,  8,  9,  1,  2,  3],
            [7,  8,  9,  1,  2,  3,  4,  5,  6],
            [2,  1,  4,  3,  6,  5,  8,  9,  7],
            [3,  6,  5,  8,  9,  7,  2,  1,  4],
            [8,  9,  7,  2,  1,  4,  3,  6,  5],
            [5,  3,  1,  6,  4,  2,  9,  7,  8],
            [6,  4,  2,  9,  7,  8,  5,  3,  1],
            [9,  7,  8,  5,  3,  1,  6,  4,  2]]

    def test_no_random_fill(self):
        board = Board(3, 9)
        BoardFiller(board).fill()
        the_board = []
        for row in board.squares:
            the_board.append(map(lambda s: s.choice, row))


    def test_random_fill(self):
        board = Board(3, 9)
        board_filler = BoardFiller(
                board,
                shuffle_choices=True,
                shuffle_squares=True
        )
        self.assertTrue(board_filler.fill())
        print board
        self.assertEquals(0, board_filler.none_count)
        self.assertTrue(board.is_valid())

if __name__ == '__main__':
    unittest.main()
