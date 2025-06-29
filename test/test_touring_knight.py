from src.touring_knight import (
    Board,
    InvalidKnightMove,
    InvalidPositionException,
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
    with pytest.raises(InvalidKnightMove):
        board.place_knight(2, 2)


def test_invalid_knight_placement() -> None:
    board = Board(rows=5, cols=5)
    with pytest.raises(InvalidPositionException):
        board.place_knight(5, 5)


def test_number_of_possible_moves_in_corner() -> None:
    board = Board(rows=5, cols=5)
    assert len(board.get_possible_knight_moves(0, 0)) == 2


def test_number_of_possible_moves_in_center() -> None:
    board = Board(rows=5, cols=5)
    assert len(board.get_possible_knight_moves(2, 2)) == 8


def test_next_moves_from_corner() -> None:
    board = Board(rows=5, cols=5)
    possible_knight_moves = board.get_possible_knight_moves(0, 0)
    assert (1, 2) in possible_knight_moves
    assert (2, 1) in possible_knight_moves


def test_move_knight_from_center() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(2, 2)
    board.place_knight(1, 0)
    assert board.knight_position == (1, 0)


def test_move_knight_from_center_to_invalid_tile() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(2, 2)
    with pytest.raises(InvalidKnightMove):
        board.place_knight(2, 0)


def test_move_knight_from_center_visits_tile() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(2, 2)
    board.place_knight(1, 0)
    assert (1, 0) in board.visited


def test_place_knight_visits_tile() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(1, 1)
    assert (1, 1) in board.visited


def test_valid_moves_after_moving_to_corner() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(1, 2)
    possible_knight_moves = board.get_possible_knight_moves(0, 0)
    assert (1, 2) not in possible_knight_moves


def test_no_tiles_visited_before_knight_placed() -> None:
    board = Board(rows=5, cols=5)
    assert not board.visited


def test_best_move_to_corner() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(2, 1)
    assert board.get_valid_moves_ordered_by_cost()[0] == (0, 0)


def test_board_not_solved_on_instantiation() -> None:
    board = Board(rows=5, cols=5)
    assert not board.solved()


def test_top_of_move_stack_has_move() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(0, 0)
    board.place_knight(1, 2)
    assert board.move_stack[-1] == (1, 2)


def test_knight_placement_is_on_stack() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(0, 0)
    assert board.move_stack[-1] == (0, 0)


def test_move_stack_starts_empty() -> None:
    board = Board(rows=5, cols=5)
    assert not board.move_stack


def test_move_stack_is_length_1_after_placement() -> None:
    board = Board(rows=5, cols=5)
    board.place_knight(1, 1)
    assert len(board.move_stack) == 1
