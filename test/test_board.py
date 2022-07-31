import unittest

from pyreversi.board import EvenSizeBoard, Direction
from pyreversi.piece import Players


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = EvenSizeBoard(8)
        self.assertEqual(board.size, 8)
        initial_board = """_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ B W _ _ _
_ _ _ W B _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
"""
        self.assertEqual(board.str_render(), initial_board)

    def test_valid(self):
        board = EvenSizeBoard(8)
        self.assertEqual(board.valid(4, 2, Players.Black), Direction.Down)
        self.assertEqual(board.valid(4, 2, Players.White), Direction(False))

    def test_valid_move(self):
        board = EvenSizeBoard(8)
        board.place(4, 2)
        expected_board = """_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ B _ _ _
_ _ _ B B _ _ _
_ _ _ W B _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
"""
        self.assertEqual(board.str_render(), expected_board)

    def test_place_multiple(self):
        board = EvenSizeBoard(8)
        board.place(4, 2)
        board.place(5, 2)
        board.place(5, 3)
        board.place(5, 4)
        board.place(6, 3)
        board.place(2, 2)
        board.place(2, 3)
        expected_pre_board = """_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ W _ B W _ _
_ _ B B B B B _
_ _ _ W W W _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
"""
        self.assertEqual(board.str_render(), expected_pre_board)
        board.place(4, 1)
        expected_post_board = """_ _ _ _ _ _ _ _
_ _ _ _ W _ _ _
_ _ W _ W W _ _
_ _ B B W B B _
_ _ _ W W W _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
"""
        self.assertEqual(board.str_render(), expected_post_board)


if __name__ == '__main__':
    unittest.main()
