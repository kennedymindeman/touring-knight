from src.touring_knight import (
    BackTrackException,
    KnightTourSolver,
    InvalidKnightMove,
    InvalidPositionException,
)
import pytest


def test_make_knight_tour_solver() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert knight_tour_solver.rows == 5
    assert knight_tour_solver.cols == 5


def test_is_valid_position() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert knight_tour_solver.is_valid_position(1, 1)
    assert knight_tour_solver.is_valid_position(0, 0)
    assert not knight_tour_solver.is_valid_position(5, 5)


def test_place_knight() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(1, 1)
    assert knight_tour_solver.knight_position == (1, 1)


def test_double_place_knight() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(1, 1)
    with pytest.raises(InvalidKnightMove):
        knight_tour_solver.place_knight(2, 2)


def test_invalid_knight_placement() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    with pytest.raises(InvalidPositionException):
        knight_tour_solver.place_knight(5, 5)


def test_number_of_possible_moves_in_corner() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert len(knight_tour_solver.get_possible_knight_moves(0, 0)) == 2


def test_number_of_possible_moves_in_center() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert len(knight_tour_solver.get_possible_knight_moves(2, 2)) == 8


def test_next_moves_from_corner() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    possible_knight_moves = knight_tour_solver.get_possible_knight_moves(0, 0)
    assert (1, 2) in possible_knight_moves
    assert (2, 1) in possible_knight_moves


def test_move_knight_from_center() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(2, 2)
    knight_tour_solver.place_knight(1, 0)
    assert knight_tour_solver.knight_position == (1, 0)


def test_move_knight_from_center_to_invalid_tile() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(2, 2)
    with pytest.raises(InvalidKnightMove):
        knight_tour_solver.place_knight(2, 0)


def test_move_knight_from_center_visits_tile() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(2, 2)
    knight_tour_solver.place_knight(1, 0)
    assert (1, 0) in knight_tour_solver.visited


def test_place_knight_visits_tile() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(1, 1)
    assert (1, 1) in knight_tour_solver.visited


def test_valid_moves_after_moving_to_corner() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(1, 2)
    possible_knight_moves = knight_tour_solver.get_possible_knight_moves(0, 0)
    assert (1, 2) not in possible_knight_moves


def test_no_tiles_visited_before_knight_placed() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert not knight_tour_solver.visited


def test_best_move_to_corner() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(2, 1)
    assert knight_tour_solver.get_valid_moves_ordered_by_cost()[0] == (0, 0)


def test_knight_tour_solver_not_solved_on_instantiation() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert not knight_tour_solver.solved()


def test_top_of_move_stack_has_move() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(0, 0)
    knight_tour_solver.place_knight(1, 2)
    assert knight_tour_solver.move_stack[-1] == (1, 2)


def test_knight_placement_is_on_stack() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(0, 0)
    assert knight_tour_solver.move_stack[-1] == (0, 0)


def test_move_stack_starts_empty() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert not knight_tour_solver.move_stack


def test_move_stack_is_length_1_after_placement() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(1, 1)
    assert len(knight_tour_solver.move_stack) == 1


def test_backtrack_on_initialized_knight_tour_solver() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    with pytest.raises(BackTrackException):
        knight_tour_solver.backtrack()


def test_backtracking_after_placement_stack_length() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(0, 0)
    knight_tour_solver.backtrack()
    assert len(knight_tour_solver.move_stack) == 0


def test_position_after_backtracking_to_empty_knight_tour_solver() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(0, 0)
    knight_tour_solver.backtrack()
    assert not knight_tour_solver.knight_position


def test_position_after_backtracking_to_previous_move() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(0, 0)
    knight_tour_solver.place_knight(2, 1)
    knight_tour_solver.backtrack()
    assert knight_tour_solver.knight_position == (0, 0)


def test_backtracking_after_placement_visited_length() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(0, 0)
    knight_tour_solver.backtrack()
    assert len(knight_tour_solver.visited) == 0


def test_backtracking_after_move_visted_length() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    knight_tour_solver.place_knight(0, 0)
    knight_tour_solver.place_knight(2, 1)
    knight_tour_solver.backtrack()
    assert len(knight_tour_solver.visited) == 1


def test_5x5_solvable() -> None:
    knight_tour_solver = KnightTourSolver(rows=5, cols=5)
    assert knight_tour_solver.solve()


def test_3x4_solvable() -> None:
    knight_tour_solver = KnightTourSolver(rows=3, cols=4)
    assert knight_tour_solver.solve()


def test_3x5_solvable() -> None:
    knight_tour_solver = KnightTourSolver(rows=3, cols=5)
    assert not knight_tour_solver.solve()
