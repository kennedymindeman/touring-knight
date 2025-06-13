from src.touring_knight import (
    Board,
    KnightAlreadyPresentException,
    InvalidPositionException,
    NoKnightOnBoardException,
)
import pytest


def test_make_board() -> None:
    board = Board(rows=5, cols=5)
    assert board.rows == 5
    assert board.cols == 5


def test_is_valid_position() -> None:
    board = Board(rows=5, cols=5)
    assert board.is_valid_position(1, 1)
    assert board.is_valid_position(0, 0)
    assert not board.is_valid_position(5, 5)


def test_place_knight() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(1, 1)
    assert board.knight_position == (1, 1)


def test_double_place_knight() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(1, 1)
    with pytest.raises(KnightAlreadyPresentException):
        board.place_knight(2, 2)


def test_invalid_knight_placement() -> None:
    board = Board(rows=5, cols=5)
    with pytest.raises(InvalidPositionException):
        board.place_knight(5, 5)


def test_number_of_possible_moves_in_corner() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(0, 0)
    assert len(board.get_possible_knight_moves()) == 2


def test_number_of_possible_moves_in_center() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(2, 2)
    assert len(board.get_possible_knight_moves()) == 8


def test_moveing_non_existent_knight() -> None:
    board = Board(rows=5, cols=5)
    with pytest.raises(NoKnightOnBoardException):
        board.get_possible_knight_moves()
