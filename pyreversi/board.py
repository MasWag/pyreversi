from enum import auto, Flag
from typing import List, Optional, Dict, Tuple

from pyreversi.piece import Piece, NormalPiece, Players


class Direction(Flag):
    Up = auto()
    Down = auto()
    Left = auto()
    Right = auto()
    UpLeft = auto()
    UpRight = auto()
    DownLeft = auto()
    DownRight = auto()


move_direction: Dict[Direction, Tuple[int, int]] = {
    Direction.Up: (0, -1),
    Direction.Down: (0, 1),
    Direction.Left: (-1, 0),
    Direction.Right: (1, 0),
    Direction.UpLeft: (-1, -1),
    Direction.UpRight: (1, -1),
    Direction.DownLeft: (-1, 1),
    Direction.DownRight: (1, 1),
}


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board: List[Optional[Piece]] = [None for _ in range(size * size)]
        self.turn = Players.Black

    def place(self, x: int, y: int, piece_class: type(Piece) = NormalPiece):
        valid_direction = self.valid(x, y, self.turn)
        if valid_direction == Direction(False):
            raise ValueError("Invalid move")

        self.board[x + y * self.size] = piece_class(self.turn)
        for direction in Direction:
            if direction not in valid_direction:
                continue
            (current_x, current_y) = (x + move_direction[direction][0], y + move_direction[direction][1])
            while self.board[current_x + current_y * self.size].owner != self.turn:
                self.board[current_x + current_y * self.size].reverse()
                (current_x, current_y) = (current_x + move_direction[direction][0], current_y + move_direction[direction][1])
        self.turn = Players.White if self.turn == Players.Black else Players.Black

    def valid_range(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def valid(self, x: int, y: int, player: Players) -> Direction:
        result = Direction(False)
        if not self.valid_range(x, y):
            return result
        if self.board[x + y * self.size] is not None:
            return result
        for direction in Direction:
            (current_x, current_y) = (x + move_direction[direction][0], y + move_direction[direction][1])
            if not self.valid_range(current_x, current_y):
                continue
            if self.board[current_x + current_y * self.size] is None:
                continue
            if self.board[current_x + current_y * self.size].owner == player:
                continue
            (current_x, current_y) = (current_x + move_direction[direction][0],
                                      current_y + move_direction[direction][1])
            while self.valid_range(current_x, current_y):
                if self.board[current_x + current_y * self.size] is None:
                    break
                if self.board[current_x + current_y * self.size].owner == player:
                    result |= direction
                (current_x, current_y) = (current_x + move_direction[direction][0],
                                          current_y + move_direction[direction][1])

        return result

    def str_render(self):
        def to_str(piece: Optional[Piece]):
            if piece is None:
                return '_'
            elif piece.owner == Players.Black:
                return 'B'
            else:
                return 'W'

        board_in_str = [to_str(piece) for piece in self.board]
        result = ''
        for y in range(self.size):
            result += ' '.join(board_in_str[y * self.size:y * self.size + self.size])
            result += '\n'

        return result


class EvenSizeBoard(Board):
    def __init__(self, size: int):
        if size % 2 != 0:
            raise ValueError("Even size board is only supported for even size")
        super().__init__(size)
        self.board[self.size // 2 - 1 + (self.size // 2 - 1) * self.size] = NormalPiece(Players.Black)
        self.board[self.size // 2 - 1 + (self.size // 2) * self.size] = NormalPiece(Players.White)
        self.board[self.size // 2 + (self.size // 2 - 1) * self.size] = NormalPiece(Players.White)
        self.board[self.size // 2 + (self.size // 2) * self.size] = NormalPiece(Players.Black)
