from src.touring_knight import Board


def test_place_knight() -> None:
    board = Board(rows=5, cols=5)
    assert board.rows == 5
    assert board.cols == 5


def test_is_valid_position() -> None:
    board = Board(rows=5, cols=5)
    assert board.is_valid_position(1, 1)
    assert board.is_valid_position(0, 0)
    assert not board.is_valid_position(5, 5)
