from abc import ABC
from enum import auto, Enum


class Players(Enum):
    Black = auto()
    White = auto()


class Piece(ABC):
    """
    Abstract class of pieces
    """
    owner: Players

    def __init__(self, owner: Players):
        self.owner = owner

    def reverse(self):
        pass


class NormalPiece(Piece):
    """
    The normal pieces of Reversi
    """

    def reverse(self):
        if self.owner == Players.Black:
            self.owner = Players.White
        else:
            self.owner = Players.Black


class OppositePiece(NormalPiece):
    """
    The normal pieces of Reversi but the initial owner is the opposite
    """

    def __init__(self, owner: Players):
        super().__init__(owner)
        self.owner = Players.White if self.owner == Players.Black else Players.Black


class NoReversePiece(Piece):
    """
    Special pieces that cannot be reversed
    """
    pass


class OppositeNoReversePiece(Piece):
    """
    Special pieces that cannot be reversed + the initial owner is the opposite
    """
    def __init__(self, owner: Players):
        super().__init__(owner)
        self.owner = Players.White if self.owner == Players.Black else Players.Black

