import unittest
from board import Board

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


if __name__ == '__main__':
    unittest.main()

