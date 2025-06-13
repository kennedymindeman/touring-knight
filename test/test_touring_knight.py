from src.touring_knight import Board


def test_place_knight() -> None:
    board = Board(rows=5, cols=5)
    assert board.rows == 5
    assert board.cols == 5
