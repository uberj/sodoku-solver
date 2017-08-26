import unittest
from board import Board
from board_filler import valid_state

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

    test_board = [
        [1, 2, 3,    4, 5, 6,   7, 8, 9]
        [4, 5, 6,    7, 8, 9,   1, 2, 3]
        [7, 8, 9,    1, 2, 3,   4, 5, 6]

        [9, 1, 2,    3, 4, 5,   6, 7, 8]
        [3, 4, 5,    6, 7, 8,   9, 1, 2]
        [6, 7, 8,    9, 1, 2,   3, 4, 5]

        [8, 9, 1,    2, 3, 4,   5, 6, 7]
        [2, 3, 4,    5, 6, 7,   8, 9, 1]
        [5, 6, 7,    8, 9, 1,   2, 3, 4]
    ]

    def test_valid_state(self):
        board = Board(3, 9)

        board.squares = [
                [None, None, None,  4, 5, 6,   7, 8, 9]
                [None, None, None,  7, 8, 9,   1, 2, 3]
                [None, None, None,  1, 2, 3,   4, 5, 6]

                [9, 1, 2,    3, 4, 5,   6, 7, 8]
                [3, 4, 5,    6, 7, 8,   9, 1, 2]
                [6, 7, 8,    9, 1, 2,   3, 4, 5]

                [8, 9, 1,    2, 3, 4,   5, 6, 7]
                [2, 3, 4,    5, 6, 7,   8, 9, 1]
                [5, 6, 7,    8, 9, 1,   2, 3, 4]
        ]

        self.assertTrue(
                valid_state(board, (0, 0, 3) [1, 2, 3, 4, 5, 6, 7, 8, 9])
        )
        self.assertFalse(
                valid_state(board, (0, 0, 3) [2, 1, 3, 4, 5, 6, 7, 8, 9])
        )





if __name__ == '__main__':
    unittest.main()

